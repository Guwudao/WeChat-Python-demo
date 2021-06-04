import TeamClockIn
import sys
from TuringBot import TuringBot

new_msg = """
#接龙
timesheet完成打卡接龙

1. 林俊杰 - Jackie
2. 杨元生-Yeson
3. 唐小兵 Leo
4. 张广洋-Ternence
5. 文逸俊 - Caesar
6. 李彬特 winter
7. 何志伟Daniel
8. 谢毅滦–Sheldon
9. 江克非-Leslie
10. 郑永祥-Michael
11. 黄文斌_Harvey
12. 陈洋平-Carl
13. 叶超-Charles
14. 戴国明-MING
15. 于顺燊-Justin
16. 刘旭斌Daniel
17. 曾昊 Anson
18. 凌俊杰-Jason
"""

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
        if len(team_list) > 0:
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
        print("expect_member_list: ", expect_member_list)

        try:
            displayName_list, nickName_list = [], []

            for member in chat_room_members:
                # print("nick name ---> ", member["NickName"])
                if len(member["DisplayName"]) > 0:
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

            reminder_str = ""
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
            if len(reminder_str) > 0:
                left = ("未打卡人数还剩 %s 人" % counter)
                reminder_str += left
                return reminder_str
            else:
                return "恭喜大家完成本次接龙！！！"
        except Exception as e:
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % (s[1],s[2].tb_lineno))


"""
displayName_list:  ['李彬特 winter', '戴国明-MING', '黄文斌_Harvey', '林俊杰 - Jackie', '张广洋-Ternence', '陈洋平', '谢毅滦–Sheldon', '何志伟Daniel', '文逸俊 - Caesar', '刘旭斌Daniel', '唐小兵 Leo', '郑永祥-Michael', '梁敏瑜 lanmon', '叶超-Charles', '凌俊杰-Jason', '曾昊 Anson', '江克非-Leslie', '于顺燊-Justin', '杨元生-Yeson']
nickName_list:,  ['ViAnNa-黄英', 'Manny郑绵毅', 'Daisy苏倩怡RM ']
"""

jade_members = ["林俊杰", "张广洋", "谢毅滦", "陈洋平", "戴国明", "唐小兵", "刘旭斌", "何志伟", "杨元生", "文逸俊", "黄文斌", "李彬特", "叶超", "郑永祥", "梁敏瑜", "曾昊", "于顺燊", "凌俊杰", "江克非", "郑绵毅"]


WeChatAction.jade_auto_reminder(jade_members, jade_members, new_msg)