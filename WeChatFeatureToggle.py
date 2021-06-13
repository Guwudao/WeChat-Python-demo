import json


class Common:
    def __init__(self, *args):
        self.imageReturn = args[0]["imageReturn"]
        self.mapAnalysis = args[0]["mapAnalysis"]
        self.envelope = args[0]["envelope"]
        self.autoReply = args[0]["autoReply"]


class CommonGroup(Common):
    def __init__(self, *args):
        self.expectedList = args[0]["expectedList"]
        self.queue = args[0]["queue"]
        super().__init__(*args)


class CommonPerson(Common):
    def __init__(self, *args):
        super().__init__(*args)


class Group:
    def __init__(self, jade: CommonGroup, washer: CommonGroup):
        self.jade = jade
        self.washer = washer


class Personal():
    def __init__(self, common: CommonPerson, jj: CommonPerson):
        self.common = common
        self.jj = jj


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
        feature_dic = dic["feature"]
        group = Group(feature_dic["group"]["jade"], feature_dic["group"]["washer"])
        personal = Personal(feature_dic["personal"]["common"], feature_dic["personal"]["jj"])
        feature = WeChatFeatureToggle(group, personal)
        return feature

    return dic


class WeChatFeatureToggle:

    @classmethod
    def instance(cls):
        if not hasattr(WeChatFeatureToggle, "_instance"):
            with open("WeChatFeatureToggle.json", "r", encoding="utf-8") as f:
                content = f.read()

                WeChatFeatureToggle._instance = json.loads(content, object_hook=object_hook)
        return WeChatFeatureToggle._instance


    def __init__(self, group: Group, personal: Personal):
        self.group = group
        self.personal = personal
