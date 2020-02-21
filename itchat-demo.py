import itchat
from itchat.content import *

from pyecharts.charts import Bar, Pie, Map, WordCloud
from pyecharts.options import InitOpts, TitleOpts, ToolboxOpts, VisualMapOpts
from pyecharts.render import make_snapshot

# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
import re
import jieba
import os
import shutil
from lxml import etree

from TuringBot import TuringBot
from PersonBodyFat import Person
import TeamClockIn
from PIL import Image
import wordcloud
import numpy as np


# itchat.send_msg("this is a test message", toUserName="filehelper")

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()


def wechat_signature_words():
    all_word_list = []
    final_words = {}
    for friend in friends:
        words = jieba.cut(friend["Signature"])
        for w in list(words):
            res = re.match(r"([\u4e00-\u9fa5]+)", w)
            if res:
                all_word_list.append(w)

    # print(all_word_list)

    for w in all_word_list:
        if w not in final_words.keys():
            final_words[w] = 0

        final_words[w] += 1

    sort_words = sorted(final_words.items(), key=lambda x: x[1], reverse=True)
    print(words)

    chart_wc = (
        WordCloud(init_opts=InitOpts(page_title="微信签名词云"))
        .add("签名词云", sort_words, word_size_range=[20, 100], shape="triangle")
        .set_global_opts(title_opts=TitleOpts(title="微信签名词云", pos_left="140px"),
                         toolbox_opts=ToolboxOpts(is_show=True))
        # .render("signature.html")
    )
    make_snapshot(snapshot, chart_wc.render("signature.html"), "signature.png")

    img = Image.open("IMG_7946.JPG")
    mask = np.array(img)
    wc = wordcloud.WordCloud(font_path="simsun.ttc",
                             background_color="white",
                             stopwords={"自己", "一个"},
                             # max_words=100,
                             mask=mask)
    wc.generate(" ".join(all_word_list))
    wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
    wc.to_file("word_cloud.png")


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
    tuple_province_list = wechat_information_refine("Province", 4, True)

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

    bar_province = (
                        Bar()
                        .add_xaxis(provinces)
                        .add_yaxis("微信好友省份统计", province_count)
                        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True))
                   )
    make_snapshot(snapshot, bar_province.render("bar_province.html"), "bar_province.png")

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
            print("{} ---------> {}".format(msg["User"]["NickName"], msg.text))

            if "#接龙" in msg.text:
                team_list, amount = TeamClockIn.unclock_list(msg.text)
                if len(team_list) > 0:
                    return "未打卡：{}, 打卡总人数为{}".format(team_list, str(amount))
                else:
                    return "打卡已全部完成，打卡人数为{}".format(str(amount))
            else:
                content = TuringBot.automatic_reply(msg.text)
                print("机器人：%s" % content)
                if content == "请求次数超限制!":
                    return "我变成个么得感情的复读机了:\n {}".format(msg.text)
                else:
                    itchat.send_msg(content, toUserName=msg["FromUserName"])
                    return
                # print(msg["User"]["NickName"] == "JJ")

                    result = re.match(r"(.*)[，,](.*)[，,](.*)[，,](.*)[，,](.*)", content)

                    if result:
                        try:
                            p = Person(*result.groups())
                        except Exception:
                            return "我是个么得感情的复读机 -- 但我并不打算复读这个"
                        # print(p.get_body_fat)
                        itchat.send_msg(p.get_body_fat, toUserName=msg["FromUserName"])
                    else:
                        return "我是个么得感情的复读机111:\n {}".format(msg.text)

        elif msg.type == "Picture":

            # 处理收到的图片和表情
            # print(msg["Content"])
            # print("--"*40)
            # html_lxml = etree.HTML(msg["Content"])
            # cdnurl = html_lxml.xpath("//emoji/@cdnurl")
            # print(cdnurl)
            #
            # itchat.send_msg(cdnurl[0], toUserName=msg["FromUserName"])
            return "我是个么得感情的复读机 -- 但我并不打算复读这个"
        else:
            return "我是个么得感情的复读机:\n {}".format(msg)


def file_classify(file_type, des_path):

    file_list = []
    for file in os.listdir():
        suffix = file.split(".")[-1]
        if suffix == file_type:
            file_list.append(file)

    if not os.path.exists(des_path):
        os.mkdir(des_path)
        print("create dir success")
    else:
        cur_path = os.path.join(os.getcwd(), des_path)
        # print(cur_path)
        os.chdir(cur_path)
        for f in file_list:
            if os.path.exists(f):
                os.remove(f)

    # print("file list: %s" % file_list)
    os.chdir(os.path.pardir)
    for f in file_list:
        shutil.move(f, des_path)




# wechat_signature_words()
# wechat_friends_analysis()
# file_classify("png", "PNG")
# file_classify("html", "HTML")
itchat.run()
