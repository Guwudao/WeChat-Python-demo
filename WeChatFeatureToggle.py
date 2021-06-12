import json


class Common:
    pass
    # def __init__(self, *args):
        # self.imageReturn = args[0]["imageReturn"]
        # self.mapAnalysis = args[0]["mapAnalysis"]
        # self.envelope = args[0]["envelope"]
        # self.autoReply = args[0]["autoReply"]


class CommonGroup(Common):

    def __init__(self, *args):
        self.expectList = args[0]["expectList"]
        self.queue = args[0]["queue"]
        self.imageReturn = args[0]["imageReturn"]
        self.mapAnalysis = args[0]["mapAnalysis"]
        self.envelope = args[0]["envelope"]
        self.autoReply = args[0]["autoReply"]
        # super().__init__(args)


class CommonPerson:

    def __init__(self, *args):
        self.imageReturn = args[0]["imageReturn"]
        self.mapAnalysis = args[0]["mapAnalysis"]
        self.envelope = args[0]["envelope"]
        self.autoReply = args[0]["autoReply"]


class Group:
    def __init__(self, jade: CommonGroup, washer: CommonGroup):
        self.jade = jade
        self.washer = washer


class Personal():
    def __init__(self, common: CommonPerson, jj: CommonPerson):
        self.common = common
        self.jj = jj


class WeChatFeatureToggle:

    def __init__(self, group: Group, personal: Personal):
        self.group = group
        self.personal = personal


def object_hook(dic):
    # print(dic)
    keys = dic.keys()


    if "jade" and "washer" in keys:
        jade = CommonGroup(dic["jade"])
        washer = CommonGroup(dic["washer"])
        return {"jade": jade, "washer": washer}


    if "common" and "jj" in keys:
        common = CommonPerson(dic["common"])
        jj = CommonPerson(dic["jj"])
        return {"common": common, "jj": jj}

    if "feature" in keys:
        print(dic)
        feature_dic = dic["feature"]
        group = Group(feature_dic["group"]["jade"], feature_dic["group"]["washer"])
        personal = Personal(feature_dic["personal"]["common"], feature_dic["personal"]["jj"])
        feature = WeChatFeatureToggle(group, personal)
        return feature

    return dic


if __name__ == '__main__':
    with open("WeChatFeatureToggle.json", "r", encoding="utf-8") as f:
        content = f.read()

        result = json.loads(content, object_hook=object_hook)
        print("-" * 100)
        print(result)

        print(result.group.jade.expectList)
        print(result.group.jade.queue)
        print(result.group.jade.imageReturn)
        print(result.group.jade.mapAnalysis)
        print(result.group.jade.envelope)
        print(result.group.jade.autoReply)
        print("-" * 50)
        print(result.group.washer.expectList)
        print(result.group.washer.queue)
        print(result.group.washer.imageReturn)
        print(result.group.washer.mapAnalysis)
        print(result.group.washer.envelope)
        print(result.group.washer.autoReply)
        print("-" * 50)
        print(result.personal.common.imageReturn)
        print(result.personal.common.mapAnalysis)
        print(result.personal.common.envelope)
        print(result.personal.common.autoReply)
        print("-" * 50)
        print(result.personal.jj.imageReturn)
        print(result.personal.jj.mapAnalysis)
        print(result.personal.jj.envelope)
        print(result.personal.jj.autoReply)