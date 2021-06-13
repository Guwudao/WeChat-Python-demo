import itchat
import sys
from itchat.content import *
from WeChatAnalytics import Analytics
from WeChatAction import WeChatAction
from xml.dom.minidom import parseString

# itchat.send_msg("this is a test message", toUserName="filehelper")

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()
chat_rooms = itchat.get_chatrooms(update=True)
# print(chat_rooms)
# return u'@%s\u2005%s' % (msg['ActualNickName'], reply_message)


def chatRoomAnalytics():
    for room in chat_rooms:
        print(room["NickName"])

# 获取微信所有群
# chatRoomAnalytics()

# 好友分析+词云图
# Analytics.wechat_friends_analysis(friends)
# Analytics.wechat_signature_words(friends)
#
# Analytics.file_classify("png", "PNG")
# Analytics.file_classify("html", "HTML")


@itchat.msg_register([MAP, CARD, NOTE, SHARING])
def wechat_service(msg):
    print("接收到了MAP, CARD, NOTE, SHARING类的信息")
    print(msg)

    if msg.type == "Map":
        try:
            print("接收到了MAP消息")
            itchat.send_msg("识别到了地图类型消息，正在自动提取地址", toUserName=msg.fromUserName)
            address = msg["Content"].split(":")[0]
            # print(address)

            dom = parseString(msg["OriContent"])
            print(type(dom))
            item_list = dom.documentElement.getElementsByTagName("location")
            longitude = item_list[0].getAttribute("y")
            latitude = item_list[0].getAttribute("x")
            address_info = f"地址：{address}，经度：{longitude}，维度：{latitude}"

            if len(address) > 0:
                itchat.send_msg(address_info, toUserName=msg.fromUserName)
            else:
                itchat.send_msg("地址提取失败", toUserName=msg.fromUserName)
        except Exception as map_error:
            error_msg = "地图解析错误：", map_error
            print(error_msg)
            itchat.send_msg(error_msg, toUserName=msg.fromUserName)
    elif msg.type == "Note":
        if msg["MsgType"] == 10000 and "红包" in msg["Content"]:
            itchat.send_msg("谢谢老板的红包[玫瑰]", toUserName=msg.fromUserName)
        if msg["MsgType"] == 10000 and "拍了拍" in msg["Content"]:
            itchat.send_msg("小心的拍，拍伤了要赔钱的[旺柴]", toUserName=msg.fromUserName)


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print(msg)

    if msg['ToUserName'] == 'filehelper':
        print("此消息发给文件助手: {}".format(msg.text))
        return

    print(msg["User"]["NickName"])
    block_list = ["小槡", "CTT", "JJ"]
    block = shouldBeBlockedMessage(msg.user["NickName"], msg.text, *block_list)
    if block: return

    if msg["HasProductId"] != 0:
        return "我是个么得感情的复读机器人 -- 但我并不打算复读微信商店提供的表情，不信你可以换一个"
    elif msg["MsgType"] == 47:
        # 表情
        msg.download(msg.fileName)
        type_symbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        itchat.send_msg("看我反弹大法！！！", toUserName=msg.fromUserName)
        return '@%s@%s' % (type_symbol, msg.fileName)
    elif msg["MsgType"] == 3:
        # 图片
        print("收到一张图片")


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # print(msg)

    try:
        if msg['ToUserName'] == 'filehelper':
            print("此消息发给文件助手: {}".format(msg.text))
            return

        block_list = ["小槡", "CTT", "JJ", "估唔到"]
        block = shouldBeBlockedMessage(msg["User"]["NickName"], msg.text, *block_list)
        # print("text block :", block, msg["User"]["NickName"])
        if block:
            return

        myself = itchat.get_friends()[0]["UserName"]
        if myself == msg["ToUserName"]:
            if isinstance(msg.text, str):
                print("{} ---------> {}".format(msg["User"]["NickName"], msg.text))

                return WeChatAction.command_action(msg.text)

                # result = re.match(r"(.*)[，,](.*)[，,](.*)[，,](.*)[，,](.*)", msg.text)
                #
                # if result:
                #     try:
                #         p = Person(*result.groups())
                #     except Exception:
                #         return "我是个么得感情的复读机 -- 但我并不打算复读这个"
                #     # print(p.get_body_fat)
                #     itchat.send_msg(p.get_body_fat, toUserName=msg.fromUserName)
                # else:
                #     return "我是个么得感情的复读机111:\n {}".format(msg.text)
            else:
                return "我是个么得感情的复读机:\n {}".format(msg)
    except Exception as e:
        s = sys.exc_info()
        print("Text reply error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
        print("text_reply error: ", e)


@itchat.msg_register(TEXT, isGroupChat=True)
def text_group_reply(msg):
    jade_members = ["林俊杰", "张广洋", "谢毅滦", "陈洋平", "戴国明", "唐小兵", "刘旭斌", "何志伟", "杨元生", "文逸俊", "黄文斌", "李彬特", "叶超", "郑永祥", "梁敏瑜", "曾昊", "于顺燊", "凌俊杰", "江克非", "郑绵毅"]
    wash_members = ['离婚分一半', '@@@', '吓\n得\n我\n昵\n称\n都\n空中旋转劈叉了', '军佬屌仔三米长，仲识分叉', '霸王别鸽', '罗平滢', 'JJ']

    # print(msg)

    # @我消息
    # if msg.isAt:
    #     msg.user.send("假装已收到@我的消息，本条为自动回复")

    try:
        # print(msg["User"])
        print("群聊【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))

        chat_room_members = msg["User"]["MemberList"]
        allow_reply_list = ["吃，都可以吃", "骑洗衣机去地铁站", "【兄弟姐妹】", "Jade", "测试群"]
        allow = shouldBeBlockedMessage(msg["User"]["NickName"], msg.text, *allow_reply_list, isGroup=True)
        if allow:

            if msg["User"]["NickName"] == "Jade":
                # print("chat_room_members: ", chat_room_members)
                if "#接龙" in msg.text:
                    remind_str = WeChatAction.jade_auto_reminder(chat_room_members, jade_members, msg.text)
                    print("【Jade】测试提醒名单：{}".format(remind_str))
                    itchat.send_msg(remind_str, toUserName=msg.fromUserName)

            elif msg["User"]["NickName"] == "骑洗衣机去地铁站":
                # print("chat_room_members: ", chat_room_members)
                if "#接龙" in msg.text:
                    remind_str = WeChatAction.jade_auto_reminder(chat_room_members, wash_members, msg.text)
                    print("【骑洗衣机去地铁站】测试提醒名单：{}".format(remind_str))
                    itchat.send_msg(remind_str, toUserName=msg.fromUserName)

            elif msg["User"]["NickName"] == "测试群":
                pass

            # else:
            #     content = WeChatAction.bot_auto_reply(msg.text)
            #     itchat.send_msg(content, toUserName=msg.fromUserName)
    except Exception as e:
        s = sys.exc_info()
        print("Group error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
        print("group error: ", e)


def shouldBeBlockedMessage(nickname, text, *args, isGroup=False) -> bool:
    block = False
    for arg in args:
        block = block or (nickname == arg)

    # 根据昵称过滤需要屏蔽的对象
    if block and not isGroup:
        print("自己人，别乱来: {} ---> {}".format(nickname, text))

    return block


itchat.run()
