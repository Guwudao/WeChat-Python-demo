import itchat
from itchat.content import *
import requests
from lxml import etree
from pyecharts.charts import Bar, Pie, Geo, Map
from pyecharts.options import InitOpts, TitleOpts, ToolboxOpts, VisualMapOpts
from pyecharts.render import make_snapshot

# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
import re
import jieba

# itchat.send_msg("this is a test message", toUserName="filehelper")


class Person:

    def __init__(self, name, age, height, weight, gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

        try:
            if isinstance(age, str):
                self.age = int(age)

            if isinstance(height, str):
                self.height = float(height)
                if self.height > 10:
                    self.height = self.height / 100

            if isinstance(weight, str):
                self.weight = float(weight)

            if gender in ("男", "女"):
                self.gender = 1 if gender == "男" else 0

        except Exception:
            raise Exception("请输入正确格式")

    @property
    def get_body_fat(self):
        bmi = self.weight / (self.height * self.height)
        body_fat = (1.2 * bmi + 0.23 * self.age - 0.54 - 10.8 * self.gender) / 100

        body_fat_scop = ((0.25, 0.28), (0.15, 0.18))
        min_fat, max_fat = body_fat_scop[self.gender]

        result = "正常"
        if body_fat < min_fat:
            result = "偏瘦"
        elif body_fat > max_fat:
            result = "偏胖"
        print("BMI = %f" % bmi, "体脂率 = %f" % body_fat)

        result_str = "{} 您好，您的体脂率是{}, 正常体脂率的范围是{} - {}, 您的体型属于{}".format(self.name, body_fat, min_fat, max_fat, result)
        return result_str


itchat.auto_login(hotReload=True)
friends = itchat.get_friends()


def wechat_signature_words():
    word_list = []
    for friend in friends:
        res = re.match(r"([\u4e00-\u9fa5]+)", friend["Signature"])
        if res:
            word = jieba.cut(res.groups(1))
            print(list(word))
            # for w in list(word):
            #     word_list.append(w)

    print(word_list)


def wechat_information_refine(key, filter_count, reverse) -> []:
    information, count = [], []

    for friend in friends:
        info = friend[key]

        if info not in information:
            information.append(info)
            count.append(0)

    info_length = len(count)

    for friend in friends:
        for i in range(info_length):
            if friend[key] == information[i]:
                count[i] += 1

    temp_list = [(i, j) for i, j in zip(information, count) if j >= filter_count]
    temp_list.sort(key=lambda x: x[1], reverse=reverse)

    # print(temp_list)
    return temp_list


def wechat_friends_analysis():
    # print(itchat.get_friends()[1])

    provinces, province_count, cities, city_count = [], [], [], []

    tuple_city_list = wechat_information_refine("City", 3, True)
    tuple_province_list = wechat_information_refine("Province", 3, True)

    sex_title = ["未知", "男", "女"]
    remark_sex_count = [0, 0, 0]
    no_remark_sex_count = [0, 0, 0]

    for friend in friends:
        sex = friend["Sex"]
        if len(friend["RemarkName"]):
            remark_sex_count[sex] += 1
        else:
            no_remark_sex_count[sex] += 1

    for i, j in tuple_province_list:
        if not len(i):
            i = "未知"
        provinces.append(i)
        province_count.append(j)

    for i, j in tuple_city_list:
        if not len(i):
            i = "未知"
        cities.append(i)
        city_count.append(j)

    # print(cities, city_count)
    # print(provinces, province_count)

    page_title = "好友性别数据统计"
    bar_sex = Bar(init_opts=InitOpts(page_title=page_title))
    bar_sex.add_xaxis(sex_title)
    bar_sex.add_yaxis("有备注", remark_sex_count)
    bar_sex.add_yaxis("无备注", no_remark_sex_count)
    bar_sex.set_global_opts(title_opts=TitleOpts(title="微信好友性别数据统计", pos_left=60))
    bar_sex.render("sex.html")

    bar_city = Bar()
    bar_city.add_xaxis(cities)
    bar_city.add_yaxis("微信好友地区数据统计", city_count)
    bar_city.set_global_opts(toolbox_opts=ToolboxOpts(is_show=True))
    bar_city.render("city.html")

    city_data_list = [(i, j) for i, j in zip(cities, city_count)]
    pie_city = (
                Pie(init_opts=InitOpts(
                                       page_title="微信好友城市分析",
                                       width="1400px",
                                       height="800px",
                                       ))
                .add(
                     data_pair=city_data_list,
                     series_name="微信好友分布",
                     # radius=["25%", "75%"],
                     # rosetype="radius"
                     )
                .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True, pos_top="50px"),
                                 title_opts=TitleOpts(title="微信好友城市分析", pos_top="80px", pos_left="10px"))
                # .render("pie_city.html")
                )
    make_snapshot(snapshot, pie_city.render("pie_city.html"), "pie_city.png")

    province_data_list = [(i, j) for i, j in zip(provinces, province_count)]
    pie_province = (
                    Pie(init_opts=InitOpts(
                        page_title="微信好友省份分析",
                        width="1200px",
                        height="800px",
                    ))
                    .add(
                        data_pair=province_data_list,
                        series_name="微信好友分布",
                        radius=["25%", "75%"],
                        rosetype="Mapping"
                    )
                    .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True, pos_top="60px"),
                                     title_opts=TitleOpts(title="微信好友省份分析", pos_top="60px", pos_left="50px"))
                    # .render("pie_province.html")
                    )
    make_snapshot(snapshot, pie_province.render("pie_province.html"), "pie_province.png")

    province_geo = (
                    Map(init_opts=InitOpts(page_title="微信好友分布"))
                    .add("微信好友分布geo图", tuple_province_list, "china")
                    .set_global_opts(
                        title_opts=TitleOpts(title="微信好友分布分布", pos_left="30px"),
                        visualmap_opts=VisualMapOpts(max_=200, is_piecewise=True))
                    # .render("geo_province.html")
                    )
    make_snapshot(snapshot, province_geo.render("geo_province.html"), "geo_province.png")


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):

    if msg["User"]["NickName"] == "CTT" or msg["User"]["NickName"] == "JJ1" or msg["User"]["NickName"] == "fat fish":
        # print("自己人，别乱来")
        print("{} ---> {}".format(msg["User"]["NickName"], msg))
        return

    print(msg)

    if not msg["Content"]:
        return "我是个么得感情的复读机 -- 但我并不打算复读这个"
    else:
        msg.download(msg.fileName)
        type_symbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        itchat.send_msg("看我图片反弹大法！！！", toUserName=msg["FromUserName"])
        return '@%s@%s' % (type_symbol, msg.fileName)


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    # 根据昵称过滤需要屏蔽的对象
    if msg.user["NickName"] == "CTT" or msg.user["NickName"] == "JJ1" or msg.user["NickName"] == "fat fish":
        # print("自己人，别乱来")
        print("{} ---> {}".format(msg["User"]["NickName"], msg.text))
        return

    myself = itchat.get_friends()[0]["UserName"]
    if myself == msg["ToUserName"]:
        if isinstance(msg.text, str):
            content = TuringBot.automatic_reply(msg.text)
            print("{} ---> {}".format(msg["User"]["NickName"], msg.text))
            print("机器人：%s" % content)
            if content == "请求次数超限制!":
                return "我变成个么得感情的复读机了:\n {}".format(msg.text)
            else:
                itchat.send_msg(content, toUserName=msg["FromUserName"])

            # print(msg["User"]["NickName"] == "JJ")
            #
            # result = re.match(r"(.*)[，,](.*)[，,](.*)[，,](.*)[，,](.*)", content)
            #
            # if result:
            #     try:
            #         p = Person(*result.groups())
            #     except Exception:
            #         return "我是个么得感情的复读机 -- 但我并不打算复读这个"
            #     # print(p.get_body_fat)
            #     itchat.send_msg(p.get_body_fat, toUserName=msg["FromUserName"])
            # else:
            #     print(msg)
            #     return "我是个么得感情的复读机:\n {}".format(msg.text)

        elif msg.type == "Picture":

            # 处理收到的图片和表情
            print(msg["Content"])
            print("--"*40)
            html_lxml = etree.HTML(msg["Content"])
            cdnurl = html_lxml.xpath("//emoji/@cdnurl")
            print(cdnurl)

            itchat.send_msg(cdnurl[0], toUserName=msg["FromUserName"])
            return "我是个么得感情的复读机 -- 但我并不打算复读这个"
        else:
            return "我是个么得感情的复读机:\n {}".format(msg)


class TuringBot:

    url = "http://openapi.tuling123.com/openapi/api/v2"

    signal_thread = "0e4dc4f3608b4da38dbbac4c746b6428"
    not_robot_key = "7714085bddd24e7aa77b071d8eaec5db"

    @classmethod
    def automatic_reply(cls, text):

        parameter_json = {
                            "reqType": 0,
                            "perception": {
                                "inputText": {
                                    "text": text
                                }
                            },
                            "userInfo": {
                                "apiKey": cls.not_robot_key,
                                "userId": "single"
                            }
                        }

        response = requests.post(cls.url, json=parameter_json)
        return response.json()["results"][0]["values"]["text"]


wechat_signature_words()
# wechat_friends_analysis()
# itchat.run()
