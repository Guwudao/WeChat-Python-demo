import TeamClockIn
import sys
import re
from TuringBot import TuringBot


class WeChatAction:

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
    def jade_auto_reminder(chat_room_members, expect_member_list, message):
        # print("expect_member_list: ", expect_member_list)

        try:
            displayName_list, nickName_list = [], []

            for member in chat_room_members:
                # print("nick name ---> ", member["NickName"])
                if len(member["DisplayName"]):
                    # print(member["DisplayName"])
                    displayName_list.append(member["DisplayName"])
                else:
                    nickName_list.append(member["NickName"])

            print("displayName_list: ", displayName_list)
            print("nickName_list:, ", nickName_list)

            reminder_list = []
            for member in expect_member_list:
                if member not in message:
                    reminder_list.append(member)

            print("提醒总名单数组：{}".format(reminder_list))

            reminder_str = WeChatAction.get_title(message)
            counter = 0
            for displayName in displayName_list:
                for reminder in reminder_list:
                    if reminder in displayName:
                        counter += 1
                        reminder_str = reminder_str + (u'@%s\u2005' % displayName) + "\n"

            for nickname in nickName_list:
                # print(nickname)
                for reminder in reminder_list:
                    if reminder in nickname:
                        counter += 1
                        reminder_str = reminder_str + (u'@%s\u2005' % nickname) + "\n"

            print("reminder_str: {}".format(reminder_str))
            if counter == 0:
                return "恭喜大家完成本次接龙！！！"
            else:
                left = ("未打卡人数还剩 %s 人" % counter)
                reminder_str += left
                return reminder_str

        except Exception as e:
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % e)
            return ("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))

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
