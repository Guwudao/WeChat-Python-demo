import TeamClockIn
import sys
import re
import json
import itchat
from TuringBot import TuringBot
from xml.dom.minidom import parseString
from datetime import datetime
from WeChatFeatureToggle import WeChatFeatureToggle as wx


class WeChatAction:

    @staticmethod
    def group_chat_handle(msg):
        toggle = wx.instance()
        chat_room_members = msg["User"]["MemberList"]
        is_available = msg.user["NickName"] in toggle.group.common.expectedList

        if msg.type == "Text":
            print("群聊【{}】 : {} : {}".format(msg.user["NickName"], msg["ActualNickName"], msg.text))
            if not is_available: return

            try:
                if msg["User"]["NickName"] == "Jade":
                    if "#接龙" in msg.text and toggle.group.jade.queue:
                        jade_members = toggle.group.jade.expectedList
                        remind_str = WeChatAction.auto_reminder(chat_room_members, jade_members, msg.text)
                        print("【Jade】接龙提醒名单：{}".format(remind_str))
                        if remind_str:
                            itchat.send_msg(remind_str, toUserName=msg.fromUserName)

                elif msg["User"]["NickName"] == "摸铃校友群":
                    if msg.isAt and toggle.group.common.atMeReply:
                        msg.user.send("假装已收到@我的消息，本条为自动回复[玫瑰]")

                elif msg["User"]["NickName"] == "骑洗衣机去地铁站":
                    if msg.isAt and toggle.group.brotherAndSister.atMeReply:
                        msg.user.send("假装已收到@我的消息，本条为自动回复[玫瑰]")

                    if "#接龙" in msg.text and toggle.group.washer.queue:
                        wash_members = toggle.group.washer.expectedList
                        remind_str = WeChatAction.auto_reminder(chat_room_members, wash_members, msg.text)
                        print("【骑洗衣机去地铁站】测试提醒名单：{}".format(remind_str))
                        if len(remind_str):
                            msg.user.send_msg(remind_str, toUserName=msg.fromUserName)

                elif msg["User"]["NickName"] == "【兄弟姐妹】":
                    # @我消息
                    if msg.isAt and toggle.group.brotherAndSister.atMeReply:
                        msg.user.send("假装已收到@我的消息，本条为自动回复[玫瑰]")

                elif msg["User"]["NickName"] == "测试群":
                    if msg.isAt:
                        msg.user.send("假装已收到@我的消息，本条为自动回复[玫瑰]")

                elif msg["User"]["NickName"] == "Our Group":
                    if "#接龙" in msg.text and toggle.group.ourGroup.queue:
                        group_members = toggle.group.ourGroup.expectedList
                        remind_str = WeChatAction.auto_reminder(chat_room_members,
                                                                group_members,
                                                                msg.text,
                                                                remind_num=30,
                                                                is_frequency_reduce=True,
                                                                frequency=4)
                        if remind_str:
                            if len(remind_str):
                                msg.user.send_msg(remind_str, toUserName=msg.fromUserName)

                elif msg["User"]["NickName"] == "网银交付部大群":
                    pass
                    # print("接收到了 网银交付部大群 的消息")
                    # print("-" * 100)
                    # print(json.dumps(chat_room_members, indent=4, ensure_ascii=False))
                    # print("-" * 100)
                    #
                    # displayName_list, nickName_list = [], []
                    # for member in chat_room_members:
                    #     if len(member["DisplayName"]):
                    #         displayName_list.append(member["DisplayName"])
                    #     else:
                    #         nickName_list.append(member["NickName"])
                    #
                    # print(displayName_list)
                    # print("-" * 100)
                    # print(nickName_list)
                    # print("-" * 100)

                # else:
                #     content = WeChatAction.bot_auto_reply(msg.text)
                #     msg.user.send_msg(content, toUserName=msg.fromUserName)
            except Exception as e:
                print(json.dumps(msg, indent=4, ensure_ascii=False))
                s = sys.exc_info()
                print("Group error '%s' happened on line %d" % (e, s[2].tb_lineno))

        elif msg.type == "Picture":
            print("收到群图片【{}】 : {}".format(msg.user["NickName"], msg["ActualNickName"]))
            if not is_available: return

            if msg["User"]["NickName"] == "【兄弟姐妹】":
                if toggle.group.brotherAndSister.imageReturn:
                    WeChatAction.group_image_return(msg)

            elif msg["User"]["NickName"] == "测试群":
                if toggle.group.test.imageReturn:
                    WeChatAction.group_image_return(msg)

            elif msg["User"]["NickName"] == "Our Group":
                pass

        elif msg.type == "Video":
            print("收到群视频【{}】 : {}".format(msg.user["NickName"], msg["ActualNickName"]))

    @staticmethod
    def group_image_return(msg):
        if msg["HasProductId"] != 0:
            # print("我是个么得感情的复读机器人 -- 但我并不打算复读微信商店提供的表情，不信你可以换一个")
            msg.user.send_msg("检测到微信商店提供的表情\n\n我是复读机器人\n\n但我并没有版权复读这个[旺柴]", toUserName=msg.fromUserName)
        elif msg["MsgType"] == 47:
            # 表情
            msg.download(msg.fileName)
            msg.user.send_msg("检测到图片表情\n看我反弹大法[旺柴]", toUserName=msg.fromUserName)
            msg.user.send_image(msg.fileName, toUserName=msg.fromUserName)
        elif msg["MsgType"] == 3:
            # 图片
            print("收到一张图片")

    @classmethod
    def command_action(cls, content, func=None) -> str:

        if "#接龙" in content:
            return cls.solitaire(content)
        # else:
        #     return WeChatAction.bot_auto_reply(content)

    @staticmethod
    def solitaire(content):
        team_list, amount = TeamClockIn.unclock_list(content)
        if len(team_list):
            return "未打卡：{}, 打卡总人数为{}".format(team_list, str(amount))
        else:
            return "打卡已全部完成，打卡人数为{}".format(str(amount))

    @staticmethod
    def bot_auto_reply(content):
        content = TuringBot.automatic_reply(content)
        print("机器人：%s" % content)
        if content == "请求次数超限制!":
            return "我变成个么得感情的复读机了:\n {}".format(content)
        else:
            return content

    @staticmethod
    def map_analysis(msg):
        try:
            address = msg["Content"].split(":")[0]
            # print(address)

            dom = parseString(msg["OriContent"])
            print(type(dom))
            item_list = dom.documentElement.getElementsByTagName("location")
            longitude = item_list[0].getAttribute("y")
            latitude = item_list[0].getAttribute("x")
            address_info = f"地址：{address}，经度：{longitude}，维度：{latitude}"

            if len(address):
                return address_info
            else:
                return "地址提取失败"
        except Exception as map_error:
            error_msg = "地图解析错误：", map_error
            print(error_msg)
            return error_msg

    @staticmethod
    def auto_reminder(chat_room_members,
                      expect_member_list,
                      message,
                      remind_num=10,
                      is_frequency_reduce=False,
                      frequency=1):

        try:
            displayName_list, nickName_list = [], []

            for member in chat_room_members:
                if len(member["DisplayName"]):
                    displayName_list.append(member["DisplayName"])
                else:
                    nickName_list.append(member["NickName"])

            # print("displayName_list: ", displayName_list)
            # print("nickName_list:, ", nickName_list)

            reminder_list = []
            for member in expect_member_list:
                if member not in message:
                    reminder_list.append(member)

            # print("提醒总名单数组：{}".format(reminder_list))
            # print(len(reminder_list))

            reminder_str = WeChatAction.get_title(message)
            counter = 0
            rest_display, rest_nick = [], []

            for displayName in displayName_list:
                for reminder in reminder_list:
                    if reminder in displayName:
                        counter += 1
                        reminder_str = reminder_str + (u'@%s\u2005' % displayName) + "\n"
                        reminder_list.remove(reminder)
                        rest_display.append(displayName)

            for nickname in nickName_list:
                for reminder in reminder_list:
                    if reminder in nickname:
                        counter += 1
                        reminder_str = reminder_str + (u'@%s\u2005' % nickname) + "\n"
                        reminder_list.remove(reminder)
                        rest_nick.append(nickname)

            # print(counter)

            if counter == 0:
                return "恭喜大家完成本次接龙！！！"
            elif counter < remind_num:
                if is_frequency_reduce:
                    if counter % frequency == 0:
                        remaining = ("\n未接龙人数还剩 %s 人" % counter)
                        reminder_str += remaining
                        return reminder_str
                else:
                    remaining = ("\n未接龙人数还剩 %s 人" % counter)
                    reminder_str += remaining

                    # if len(reminder_list):
                    #     not_match = "\n\n以下同事名字未能匹配成功，请检查是否修改群备注：%s" % reminder_list
                    #     reminder_str += not_match
                    print("reminder_str: {}".format(reminder_str))
                    return reminder_str

        except Exception as e:
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % e)
            return ("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))

    @staticmethod
    def is_available_time(begin, end):
        begin_time = datetime.strptime(str(datetime.now().date()) + begin, "%Y-%m-%d%H:%M")
        end_time = datetime.strptime(str(datetime.now().date()) + end, "%Y-%m-%d%H:%M")
        now = datetime.now()

        return now >= begin_time and now <= end_time

    @staticmethod
    def get_title(message):
        try:
            reminder_str = ""
            remove_shifter = re.sub('\s+', " ", message)
            title = re.findall(r"#接龙(.*?)1. ", remove_shifter)
            if len(title):
                reminder_str = title[0] + "\n"
            return reminder_str
        except Exception as e:
            print("title parse error: ", e)
            return ""
