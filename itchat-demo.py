import itchat
from itchat.content import *
from lxml import etree
from WeChatAnalytics import Analytics
from WeChatAction import WeChatAction
import json

# itchat.send_msg("this is a test message", toUserName="filehelper")

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()
chat_rooms = itchat.get_chatrooms(update=True)
start_time = 0
send_msg, toUsrName = "", ""
# print(chat_rooms)

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


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):

    if msg['ToUserName'] == 'filehelper':
        print("此消息发给文件助手: {}".format(msg.text))
        return

    block_list = ["CTT", "JJ", "小槡"]
    block = is_nickname_available(msg.user["NickName"], msg.text, *block_list)
    if block: return

    if not msg["Content"]:
        return "我是个么得感情的复读机 -- 但我并不打算复读这个"
    else:
        msg.download(msg.fileName)
        type_symbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        itchat.send_msg("看我反弹大法！！！", toUserName=msg["FromUserName"])
        return '@%s@%s' % (type_symbol, msg.fileName)


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    if msg['ToUserName'] == 'filehelper':
        print("此消息发给文件助手: {}".format(msg.text))
        return

    block_list = ["CTT", "JJ", "小槡"]
    block = is_nickname_available(msg["User"]["NickName"], msg.text, *block_list)
    print("text block :", block)
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



import time
from threading import Timer
from datetime import datetime

def time_reminder():
    print("倒计时：{}".format(datetime.now().strftime("%H:%M:%S")))
    print("start_time：{}".format(start_time))
    print("--" * 30)

    interval = time.time() - start_time

    if interval > 20:
        print("倒计时到了 {} {}".format(send_msg, toUsrName))
        itchat.send_msg(send_msg, toUserName=toUsrName)
        return

    # if (interval // 60) >= 1:
    #     print("倒计时一分钟到了")

    timer = Timer(5, time_reminder)
    timer.start()


@itchat.msg_register(TEXT, isGroupChat=True)
def text_group_reply(msg):

    # print(msg["User"])
    print("群聊【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))

    allow_reply_list = ["吃，都可以吃", "骑洗衣机去地铁站", "【兄弟姐妹】", "Jade", "测试群"]
    allow = is_nickname_available(msg["User"]["NickName"], msg.text, True, *allow_reply_list)
    if allow:

        if "#接龙" in msg.text:
            # print(msg)
            jade_members = ["林俊杰", "洋子", "谢毅滦", "陈洋平", "戴国明", "唐小兵", "刘旭斌", "何志伟", "吴小广", "文逸俊", "黄文斌", "李彬特"]
            wash_members = ['离婚分一半', '@@@', '吓\n得\n我\n昵\n称\n都\n空中旋转劈叉了', '军佬屌仔三米长，仲识分叉', '霸王别鸽', '罗平滢', 'JJ']

            chat_room_members = msg["User"]["MemberList"]
            # print(chat_room_members)
            remind_str = ""
            if msg["User"]["NickName"] == "Jade":
                remind_str = WeChatAction.jade_auto_reminder(chat_room_members, jade_members, msg.text)
            elif msg["User"]["NickName"] == "骑洗衣机去地铁站":
                remind_str = WeChatAction.jade_auto_reminder(chat_room_members, wash_members, msg.text)


            print("测试提醒名单：{}".format(remind_str))

            itchat.send_msg(remind_str, toUserName=msg["FromUserName"])
        # else:
        #     content = WeChatAction.bot_auto_reply(msg.text)
        #     itchat.send_msg(content, toUserName=msg["FromUserName"])


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
        if chatroom is None: return CHATROOM_MSG
        r = itchat.add_member_into_chatroom(chatroom['UserName'], [friend])
        if r['BaseResponse']['ErrMsg'] == '请求成功':
            status = r['MemberList'][0]['MemberStatus']
            itchat.delete_member_from_chatroom(chatroom['UserName'], [friend])
            return { 3: u'该好友已经将你加入黑名单。',
                4: u'该好友已经将你删除。', }.get(status,
                u'该好友仍旧与你是好友关系。')
        else:
            return u'无法获取好友状态，预计已经达到接口调用限制。'

@itchat.msg_register(itchat.content.CARD)
def get_friend(msg):
    print("itchat.content.CARD itchat.content.CARD itchat.content.CARD itchat.content.CARD itchat.content.CARD")
    if msg['ToUserName'] != 'filehelper': return
    friendStatus = get_friend_status(msg['RecommendInfo'])
    itchat.send(friendStatus, 'filehelper')

# itchat.send(HELP_MSG, 'filehelper')
itchat.run()
