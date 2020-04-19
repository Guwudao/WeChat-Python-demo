import itchat
from itchat.content import *

from lxml import etree

from TuringBot import TuringBot
from PersonBodyFat import Person
import TeamClockIn
from WeChatAnalytics import Analytics



# itchat.send_msg("this is a test message", toUserName="filehelper")

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()

Analytics.wechat_friends_analysis(friends)
Analytics.wechat_signature_words(friends)


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
            # else:
            #     content = TuringBot.automatic_reply(msg.text)
            #     print("机器人：%s" % content)
            #     if content == "请求次数超限制!":
            #         return "我变成个么得感情的复读机了:\n {}".format(msg.text)
            #     else:
            #         itchat.send_msg(content, toUserName=msg["FromUserName"])
            #         return
            #     # print(msg["User"]["NickName"] == "JJ")
            #
            #         result = re.match(r"(.*)[，,](.*)[，,](.*)[，,](.*)[，,](.*)", content)
            #
            #         if result:
            #             try:
            #                 p = Person(*result.groups())
            #             except Exception:
            #                 return "我是个么得感情的复读机 -- 但我并不打算复读这个"
            #             # print(p.get_body_fat)
            #             itchat.send_msg(p.get_body_fat, toUserName=msg["FromUserName"])
            #         else:
            #             return "我是个么得感情的复读机111:\n {}".format(msg.text)

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


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):

    print("群聊【{}】 : {} : {}".format(msg["User"]["NickName"], msg["ActualNickName"], msg.text))
    # print(msg.user["NickName"])

    group_nick_name = msg.user["NickName"]
    if group_nick_name == "吃，都可以吃" or group_nick_name == "【兄弟姐妹】":
        content = TuringBot.automatic_reply(msg.text)
        print("机器人：%s" % content)
        if content == "请求次数超限制!":
            return "我变成个么得感情的复读机了:\n {}".format(msg.text)
        else:
            itchat.send_msg(content, toUserName=msg["FromUserName"])


# file_classify("png", "PNG")
# file_classify("html", "HTML")
itchat.run()
