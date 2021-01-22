import TeamClockIn
from TuringBot import TuringBot

# new_msg = """
# #接龙
# timesheet完成打卡接龙
#
# 1. 林俊杰 - Jackie
# 2. 洋子-Ternence
# 3. 谢毅滦–Sheldon
# 4. 陈洋平 Carl
# 5. 戴国明-MING
# 6. 唐小兵 snow
# 7. 刘旭斌 Daniel
# 8. 何志伟Daniel
# 9. 吴小广-Clifton
# 10. 文逸俊 - Caesar
# 11. 黄文斌_Harvey
# 12. 李彬特 winter
# """

class WeChatAction:

    @classmethod
    def command_action(cls, content, func=None) -> str:

        if "#接龙" in content:
            return cls.solitaire(content)
        # else:
        #     return WeChatAction.bot_auto_reply(content)

    @staticmethod
    def solitaire(content) -> str:
        team_list, amount = TeamClockIn.unclock_list(content)
        if len(team_list) > 0:
            return "未打卡：{}, 打卡总人数为{}".format(team_list, str(amount))
        else:
            return "打卡已全部完成，打卡人数为{}".format(str(amount))

    @staticmethod
    def bot_auto_reply(content) -> str:
        content = TuringBot.automatic_reply(content)
        print("机器人：%s" % content)
        if content == "请求次数超限制!":
            return "我变成个么得感情的复读机了:\n {}".format(content)
        else:
            return content

    @staticmethod
    def jade_auto_reminder(chat_room_members, expect_member_list, message):
        print("expect_member_list: ", expect_member_list)

        try:
            displayName_list, no_displayName_list = [], []

            for member in chat_room_members:
                # print("nick name ---> ", member["NickName"])
                if len(member["DisplayName"]) > 0:
                    # print(member["DisplayName"])
                    displayName_list.append(member["DisplayName"])
                else:
                    no_displayName_list.append(member["NickName"])

            print("displayName_list: ", displayName_list)
            print("no_displayName_list:, ", no_displayName_list)

            reminder_list = []
            for member in expect_member_list:
                if member not in message:
                    reminder_list.append(member)

            print("提醒总名单数组：{}".format(reminder_list))

            reminder_str = ""
            # for displayName in displayName_list:
            #     for reminder in reminder_list:
            #         if reminder in displayName:
            #             reminder_str = reminder_str + "@" + displayName + "\n"
            #             # u'@%s\u2005' % displayName
            #
            # for nickname in no_displayName_list:
            #     for reminder in reminder_list:
            #         if reminder in nickname:
            #             reminder_str = reminder_str + "@" + nickname + "\n"

            for display_name, nickname in zip(displayName_list, no_displayName_list):
                for reminder in reminder_list:
                    if reminder in displayName:
                        reminder_str = reminder_str + (u'@%s\u2005' % displayName) + " "
                    if reminder in nickname:
                        reminder_str = reminder_str + (u'@%s\u2005' % nickname) + " "

            print("reminder_str: {}".format(reminder_str))
            if len(reminder_str) > 0:
                return reminder_str
            else:
                return "恭喜老板们完成本次接龙！！！"
        except Exception as e:
            return "reminder error occur:, %s" % (e)
