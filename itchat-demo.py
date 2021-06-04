import itchat
from itchat.content import *
from WeChatAnalytics import Analytics
from WeChatAction import WeChatAction

# itchat.send_msg("this is a test message", toUserName="filehelper")

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()
chat_rooms = itchat.get_chatrooms(update=True)
start_time = 0
send_msg, toUsrName = "", ""
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
    # print(msg)

    if msg.type == "Map":
        print("接收到了MAP消息")
        itchat.send_msg("识别到了地图类型消息，正在自动提取地址", toUserName=msg["FromUserName"])
        address = msg["Content"].split(":")[0]
        # print(address)
        itchat.send_msg(address, toUserName=msg["FromUserName"])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print(msg)

    if msg['ToUserName'] == 'filehelper':
        print("此消息发给文件助手: {}".format(msg.text))
        return

    # block_list = ["CTT", "JJ", "小槡"]
    # block = is_nickname_available(msg.user["NickName"], msg.text, *block_list)
    # if block: return

    print(msg["HasProductId"] != 0)

    if msg["HasProductId"] != 0:
        print("批量制作的表情")
        return "我是个么得感情的复读机 -- 但我并不打算复读这个"
    elif msg["MsgType"] == 47: #表情
        msg.download(msg.fileName)
        type_symbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        itchat.send_msg("看我反弹大法！！！", toUserName=msg["FromUserName"])
        return '@%s@%s' % (type_symbol, msg.fileName)
    elif msg["MsgType"] == 3: #图片
        print("收到一张图片")


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    try:
        if msg['ToUserName'] == 'filehelper':
            print("此消息发给文件助手: {}".format(msg.text))
            return

        block_list = ["CTT", "JJ", "小槡"]
        block = is_nickname_available(msg["User"]["NickName"], msg.text, *block_list)
        print("text block :", block, msg["User"]["NickName"])
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
                #     itchat.send_msg(p.get_body_fat, toUserName=msg["FromUserName"])
                # else:
                #     return "我是个么得感情的复读机111:\n {}".format(msg.text)
            else:
                return "我是个么得感情的复读机:\n {}".format(msg)
    except Exception as e:
        print("text_reply error: ", e)


@itchat.msg_register(TEXT, isGroupChat=True)
def text_group_reply(msg):
    jade_members = ["林俊杰", "张广洋", "谢毅滦", "陈洋平", "戴国明", "唐小兵", "刘旭斌", "何志伟", "杨元生", "文逸俊", "黄文斌", "李彬特", "叶超", "郑永祥",
                    "梁敏瑜", "曾昊", "于顺燊", "凌俊杰", "江克非", "郑绵毅"]
    wash_members = ['离婚分一半', '@@@', '吓\n得\n我\n昵\n称\n都\n空中旋转劈叉了', '军佬屌仔三米长，仲识分叉', '霸王别鸽', '罗平滢', 'JJ']

    try:
        # print(msg["User"])
        print("群聊【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))

        allow_reply_list = ["吃，都可以吃", "骑洗衣机去地铁站", "【兄弟姐妹】", "Jade", "测试群"]
        allow = is_nickname_available(msg["User"]["NickName"], msg.text, True, *allow_reply_list)
        if allow:

            if msg["User"]["NickName"] == "Jade":
                if "#接龙" in msg.text:
                    chat_room_members = msg["User"]["MemberList"]
                    # print("chat_room_members: " + chat_room_members)
                    remind_str = ""
                    remind_str = WeChatAction.jade_auto_reminder(chat_room_members, jade_members, msg.text)
                    print("【Jade】测试提醒名单：{}".format(remind_str))
                    itchat.send_msg(remind_str, toUserName=msg["FromUserName"])

            elif msg["User"]["NickName"] == "骑洗衣机去地铁站":
                chat_room_members = msg["User"]["MemberList"]
                remind_str = WeChatAction.jade_auto_reminder(chat_room_members, wash_members, msg.text)
                print("【骑洗衣机去地铁站】测试提醒名单：{}".format(remind_str))
                itchat.send_msg(remind_str, toUserName=msg["FromUserName"])
            # else:
            #     content = WeChatAction.bot_auto_reply(msg.text)
            #     itchat.send_msg(content, toUserName=msg["FromUserName"])
    except Exception as e:
        print("group error: ", e)


def is_nickname_available(nickName, text, isGroup=False, *args) -> bool:
    block = False
    for arg in args:
        block = block or (nickName == arg)

    # 根据昵称过滤需要屏蔽的对象
    if block and not isGroup:
        print("自己人，别乱来: {} ---> {}".format(nickName, text))

    return block


CHATROOM_NAME = 'friend'
CHATROOM = None
HELP_MSG = u'''\
好友状态监测
* 发送名片将会返回好友状态
* 请确有名为%s的未使用的群聊
* 并将该群聊保存到通讯录
* 调用频率存在一定限制\
''' % CHATROOM_NAME
CHATROOM_MSG = u'''\
无法自动创建群聊，请手动创建
确保群聊名称为%s
请不要使用已经使用过的群聊
创建后请将群聊保存到通讯录\
''' % CHATROOM_NAME


def get_chatroom():
    global CHATROOM
    if CHATROOM is None:
        itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(CHATROOM_NAME)
        if chatrooms:
            return chatrooms[0]
        else:
            r = itchat.create_chatroom(itchat.get_friends()[1:4], topic=CHATROOM_NAME)
            if r['BaseResponse']['ErrMsg'] == '':
                CHATROOM = {'UserName': r['ChatRoomName']}
                return CHATROOM
    else:
        return CHATROOM


def get_friend_status(friend):
    ownAccount = itchat.get_friends(update=True)[0]
    if friend['UserName'] == ownAccount['UserName']:
        return u'检测到本人账号。'
    elif itchat.search_friends(userName=friend['UserName']) is None:
        return u'该用户不在你的好友列表中。'
    else:
        chatroom = CHATROOM or get_chatroom()
        if chatroom is None:
            return CHATROOM_MSG
        r = itchat.add_member_into_chatroom(chatroom['UserName'], [friend])
        if r['BaseResponse']['ErrMsg'] == '请求成功':
            status = r['MemberList'][0]['MemberStatus']
            itchat.delete_member_from_chatroom(chatroom['UserName'], [friend])
            return { 3: u'该好友已经将你加入黑名单。', 4: u'该好友已经将你删除。', }.get(status, u'该好友仍旧与你是好友关系。')
        else:
            return u'无法获取好友状态，预计已经达到接口调用限制。'


@itchat.msg_register(itchat.content.CARD)
def get_friend(msg):
    print("itchat.content.CARD itchat.content.CARD itchat.content.CARD itchat.content.CARD itchat.content.CARD")
    if msg['ToUserName'] != 'filehelper':
        return
    friendStatus = get_friend_status(msg['RecommendInfo'])
    itchat.send(friendStatus, 'filehelper')


# itchat.send(HELP_MSG, 'filehelper')
itchat.run()
