import TeamClockIn
from TuringBot import TuringBot

class WeChatAction:

    @classmethod
    def command_action(cls, content, func=None) -> str:

        if "#接龙" in content:
            return WeChatAction.solitaire(content)
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

