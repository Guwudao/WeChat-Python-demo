import itchat
import sys
import time
import re
import os
import json
from itchat.content import *
from WeChatAnalytics import Analytics
from WeChatAction import WeChatAction
from WeChatFeatureToggle import WeChatFeatureToggle as wx


def recall_message_handle(msg, is_group, group_name=""):
    # print(msg)
    msg_rev_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 消息发送人
    try:
        friends = itchat.search_friends(userName=msg["FromUserName"])

        if friends:
            msg_from = itchat.search_friends(userName=msg["FromUserName"])["NickName"]
        else:
            msg_from = msg["ActualNickName"]
    except Exception as e:
        print("search friend error: ", e)
        msg_from = "微信官方账号"

    # 消息id
    msg_id = msg["MsgId"]
    # 发送消息的时间
    msg_send_time = msg["CreateTime"]
    # 消息内容
    msg_content = None
    # 消息链接
    msg_url = None
    # 是否群消息
    msg_is_group = is_group
    # 群名称
    msg_group_name = group_name

    # 文本或者好友邀请
    if msg["Type"] in ["Text", "Friends"]:
        msg_content = msg["Text"]
        # print("[文本/好友邀请]: %s" % msg_content)

    # 语言,附件，视频，图片
    elif msg["Type"] in ["Recording", "Attachment", "Video", "Picture"]:
        msg_content = msg["FileName"]
        # 保存文件
        msg["Text"](str(msg_content))
        # print("[语言/附件/视频/图片]: %s" % msg_content)

    # 名片
    elif msg["Type"] == "Card":
        msg_content = msg["RecommendInfo"]["NickName"] + "的名片，"
        if msg["RecommendInfo"]["Sex"] == 1:
            msg_content += "性别男。"
        else:
            msg_content += "性别女。"
        # print("[推荐名片]:%s" % msg_content)

    # 位置
    elif msg["Type"] == "Map":
        x, y, location = re.search \
            ("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg["OriContent"]).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度:" + x.__str__() + ", 经度:" + y.__str__()
        else:
            msg_content = r"" + location
        # print("[位置]：%s" % msg_content)

    # 分享的
    elif msg["Type"] == "Sharing":
        msg_content = msg["Text"]
        msg_url = msg["Url"]
        # print("[分享]: %s" % msg_content)

    face_package = msg_content

    # 更新msg_info字典
    msg_info.update(
        {
            msg_id: {
                "msg_from": msg_from,
                "msg_send_time": msg_send_time,
                "msg_rev_time": msg_rev_time,
                "msg_type": msg["Type"],
                "msg_content": msg_content,
                "msg_url": msg_url,
                "msg_is_group": msg_is_group,
                "msg_group_name": msg_group_name
            }
        }
    )
    # print("&" * 100)
    # print(msg_info)


@itchat.msg_register([MAP, CARD, SHARING], isGroupChat=True)
def wechat_service(msg):
    recall_message_handle(msg, is_group=True, group_name=msg.user["NickName"])
    print("接收到了群聊 MAP, CARD, SHARING类的信息")
    # print(msg)

    allow_reply_list = toggle.group.common.expectedList
    allow = shouldBeBlockedMessage(msg["User"]["NickName"], msg.text, *allow_reply_list, isGroup=True)
    if not allow: return

    if msg.type == "Map" and toggle.group.common.mapAnalysis:
        print("检测到群MAP消息【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))
        itchat.send_msg("识别到了地图类型消息，正在自动提取地址", toUserName=msg.fromUserName)

        result = WeChatAction.map_analysis(msg)
        itchat.send_msg(result, toUserName=msg.fromUserName)

    elif msg.type == "Sharing":
        print("群分享消息【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))


@itchat.msg_register([MAP, CARD, NOTE, SHARING])
def wechat_service(msg):
    recall_message_handle(msg, is_group=False)
    print("接收到了MAP, CARD, NOTE, SHARING类的信息")
    # print(msg)

    if msg.type == "Map":
        print("接收到了MAP消息")
        itchat.send_msg("识别到了地图类型消息，正在自动提取地址", toUserName=msg.fromUserName)

        result = WeChatAction.map_analysis(msg)
        itchat.send_msg(result, toUserName=msg.fromUserName)

    elif msg.type == "Note":
        if msg["MsgType"] == 10000 and "红包" in msg["Content"]:
            itchat.send_msg("谢谢老板的红包[玫瑰]", toUserName=msg.fromUserName)
        if msg["MsgType"] == 10000 and "拍了拍" in msg["Content"]:
            itchat.send_msg("小心的拍，拍伤了要赔钱的[旺柴]", toUserName=msg.fromUserName)


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    recall_message_handle(msg, is_group=False)
    # print(msg)

    if msg["ToUserName"] == "filehelper":
        print("此消息发给文件助手: {}".format(msg.text))
        return

    print(msg["User"]["NickName"])
    block_list = ["小槡", "CTT", "JJ"]
    block = shouldBeBlockedMessage(msg.user["NickName"], msg.text, *block_list)
    if block: return

    if msg["HasProductId"] != 0:
        return "我是个微信机器人 -- 但我并不版权微信商店提供的表情，不信你可以换一个"
    elif msg["MsgType"] == 47:
        # 表情
        msg.download(msg.fileName)
        type_symbol = {
            PICTURE: "img",
            VIDEO: "vid", }.get(msg.type, "fil")
        itchat.send_msg("检测到图片表情，看我反弹机器人[旺柴]", toUserName=msg.fromUserName)
        return "@%s@%s" % (type_symbol, msg.fileName)
    elif msg["MsgType"] == 3:
        # 图片
        print("收到一张图片")


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    recall_message_handle(msg, is_group=False)
    # print(msg)

    try:
        if msg["ToUserName"] == "filehelper":
            print("此消息发给文件助手: {}".format(msg.text))
            return

        block_list = ["小槡", "CTT", "JJ", "估唔到"]
        block = shouldBeBlockedMessage(msg["User"]["NickName"], msg.text, *block_list)
        if block:
            return

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
        print(json.dumps(msg, indent=4, ensure_ascii=False))
        print("Text reply error '%s' happened on line %d" % (e, s[2].tb_lineno))


@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def text_group_reply(msg):
    recall_message_handle(msg, is_group=True, group_name=msg.user["NickName"])
    # print(msg)

    chat_room_members = msg["User"]["MemberList"]
    allow_reply_list = toggle.group.common.expectedList
    allow = shouldBeBlockedMessage(msg["User"]["NickName"], msg.text, *allow_reply_list, isGroup=True)

    if msg.type == "Text":
        print("群聊【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))
        if not allow: return

        try:
            if msg["User"]["NickName"] == "Jade":
                if "#接龙" in msg.text and toggle.group.jade.queue:
                    jade_members = toggle.group.jade.expectedList
                    remind_str = WeChatAction.jade_auto_reminder(chat_room_members, jade_members, msg.text)
                    print("【Jade】接龙提醒名单：{}".format(remind_str))
                    if remind_str:
                        itchat.send_msg(remind_str, toUserName=msg.fromUserName)

            elif msg["User"]["NickName"] == "摸铃校友群":
                if msg.isAt and toggle.group.common.atMeReply:
                    msg.user.send("假装已收到@我的消息，本条为自动回复[玫瑰]")

            elif msg["User"]["NickName"] == "骑洗衣机去地铁站":
                if "#接龙" in msg.text and toggle.group.washer.queue:
                    wash_members = toggle.group.washer.expectedList
                    remind_str = WeChatAction.jade_auto_reminder(chat_room_members, wash_members, msg.text)
                    print("【骑洗衣机去地铁站】测试提醒名单：{}".format(remind_str))
                    if len(remind_str):
                        itchat.send_msg(remind_str, toUserName=msg.fromUserName)

            elif msg["User"]["NickName"] == "【兄弟姐妹】":
                # @我消息
                if msg.isAt and toggle.group.brotherAndSister.atMeReply:
                    msg.user.send("假装已收到@我的消息，本条为自动回复[玫瑰]")

            elif msg["User"]["NickName"] == "测试群":
                if msg.isAt:
                    msg.user.send("假装已收到@我的消息，本条为自动回复[玫瑰]")

            elif msg["User"]["NickName"] == "Our Group":
                displayName_list, nickName_list = [], []
                for member in chat_room_members:
                    # print("nick name ---> ", member["NickName"])
                    if len(member["DisplayName"]):
                        # print(member["DisplayName"])
                        displayName_list.append(member["DisplayName"])
                    else:
                        nickName_list.append(member["NickName"])

                print(displayName_list)
                print("-" * 100)
                print(nickName_list)

            # else:
            #     content = WeChatAction.bot_auto_reply(msg.text)
            #     itchat.send_msg(content, toUserName=msg.fromUserName)
        except Exception as e:
            print(json.dumps(msg, indent=4, ensure_ascii=False))
            s = sys.exc_info()
            print("Group error '%s' happened on line %d" % (e, s[2].tb_lineno))

    elif msg.type == "Picture":
        if not allow: return

        print("收到群图片【{}】 : {}".format(msg.user["NickName"], msg["ActualNickName"]))
        if msg["User"]["NickName"] == "【兄弟姐妹】":
            if toggle.group.brotherAndSister.imageReturn:
                group_image_return(msg)

        elif msg["User"]["NickName"] == "测试群":
            if toggle.group.test.imageReturn:
                group_image_return(msg)

    elif msg.type == "Video":
        print("收到群视频【{}】 : {}".format(msg.user["NickName"], msg["ActualNickName"]))


def group_image_return(msg):
    if msg["HasProductId"] != 0:
        # print("我是个么得感情的复读机器人 -- 但我并不打算复读微信商店提供的表情，不信你可以换一个")
        itchat.send_msg("检测到微信商店提供的表情\n\n我是复读机器人\n\n但我并没有版权复读这个[旺柴]", toUserName=msg.fromUserName)
    elif msg["MsgType"] == 47:
        # 表情
        msg.download(msg.fileName)
        itchat.send_msg("检测到图片表情，看我反弹大法[旺柴]", toUserName=msg.fromUserName)
        itchat.send_image(msg.fileName, toUserName=msg.fromUserName)
    elif msg["MsgType"] == 3:
        # 图片
        print("收到一张图片")


# 监听是否有消息撤回(NOTE)并进行相应操作
@itchat.msg_register([NOTE], isFriendChat=True, isGroupChat=True, isMpChat=True)
def send_msg_(msg):
    # print(msg)
    global face_package

    try:
        if "撤回了一条消息" in msg["Content"]:
            print("拦截到撤回了一条消息")
            # re匹配最后一次撤回消息的id
            recall_msg_id = re.search(r"<msgid>(.*?)</msgid>", msg["Content"]).group(1)
            # 读取msg_info中该id对应的消息
            recall_msg = msg_info.get(recall_msg_id)
            print("[撤回]: %s" % recall_msg)

            # 撤回的是表情包
            if len(recall_msg_id) < 11:
                itchat.send_file(face_package, toUserName=myself)
                os.remove(face_package)
            else:
                if recall_msg.get("msg_is_group"):
                    msg_body = "——拦截到一条群消息撤回——\n群名称：" + recall_msg.get("msg_group_name") + \
                               "\n撤回人：" + recall_msg.get("msg_from") + \
                               "\n内容为：" + recall_msg.get("msg_content")
                else:
                    msg_body = "——拦截到一条个人消息撤回——\n[" + recall_msg.get(
                        "msg_from") + "] 撤回了一条" + recall_msg.get("msg_type") + \
                               "消息\n" + recall_msg.get("msg_rev_time") + "\n内容为：" + recall_msg.get("msg_content")

                if recall_msg["msg_type"] == "Sharing":
                    msg_body = msg_body + "\n就是这个链接：" + recall_msg.get("msg_url")

                # 将撤回的消息(msg_body)发送给自己
                itchat.send(msg_body, toUserName=myself)

                # 有文件的话也要将文件发送
                if recall_msg["msg_type"] in ["Recording", "Attachment", "Video", "Picture"]:
                    file = "@fil@%s" % (recall_msg["msg_content"])
                    itchat.send(msg=file, toUserName=myself)
                    os.remove(recall_msg["msg_content"])

                # 一次撤回信息查看后删除msg_info字典中的信息
                msg_info.pop(recall_msg_id)

        if msg["MsgType"] == 10000 and "红包" in msg["Content"]:
            print("群红包消息【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))
            itchat.send_msg("卧槽！红包！检测到了红包！[旺柴]", toUserName=msg.fromUserName)

        if msg["MsgType"] == 10000 and "拍了拍" in msg["Content"]:
            print("群拍一拍消息【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))
            itchat.send_msg("小心的拍，拍伤了要赔钱的[旺柴]", toUserName=msg.fromUserName)

    except Exception as e:
        s = sys.exc_info()
        print(json.dumps(msg, indent=4, ensure_ascii=False))
        print("[ERROR] recall message block error '%s' happened on line %d" % (e, s[2].tb_lineno))


def shouldBeBlockedMessage(nickname, text, *args, isGroup=False) -> bool:
    block = False
    for arg in args:
        block = block or (nickname == arg)

    # 根据昵称过滤需要屏蔽的对象
    if block and not isGroup:
        print("自己人，别乱来: {} ---> {}".format(nickname, text))

    return block


if __name__ == '__main__':

    itchat.auto_login(hotReload=True)
    itchat.show_mobile_login()
    friends = itchat.get_friends()
    myself = itchat.get_friends()[0]["UserName"]
    # chat_rooms = itchat.get_chatrooms(update=True)

    # 存放接受消息的信息
    msg_info = {}

    # 好友分析 + 词云图
    toggle = wx.instance()
    if toggle.analysis.isAllEnabled:
        Analytics.wechat_friends_analysis(friends)
        Analytics.wechat_signature_words(friends)

        Analytics.file_classify("png", "PNG")
        Analytics.file_classify("html", "HTML")

    itchat.run()
