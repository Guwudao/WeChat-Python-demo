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
        self.atMeReply = args[0]["atMeReply"]
        super().__init__(*args)


class CommonPerson(Common):
    def __init__(self, *args):
        super().__init__(*args)


class Group:
    def __init__(self,
                 common: CommonGroup,
                 test: CommonGroup,
                 ourGroup: CommonGroup,
                 dhrGroup: CommonGroup,
                 jade: CommonGroup,
                 washer: CommonGroup,
                 brotherAndSister: CommonGroup):

        self.common = common
        self.test = test
        self.ourGroup = ourGroup
        self.dhrGroup = dhrGroup
        self.jade = jade
        self.washer = washer
        self.brotherAndSister = brotherAndSister


class Personal():
    def __init__(self, common: CommonPerson, jj: CommonPerson):
        self.common = common
        self.jj = jj


class Analysis():
    def __init__(self, *args):
        self.isAllEnabled = args[0]["isAllEnabled"]
        self.sexAnalysis = args[0]["sexAnalysis"]
        self.barCity = args[0]["barCity"]
        self.barProvince = args[0]["barProvince"]
        self.pieCity = args[0]["pieCity"]
        self.pieProvince = args[0]["pieProvince"]
        self.geoProvince = args[0]["geoProvince"]
        self.pyechartsWordCloud = args[0]["pyechartsWordCloud"]
        self.pilWordCloud = args[0]["pilWordCloud"]


def object_hook(dic):
    # print(dic)
    keys = dic.keys()

    if "jade" and "washer" in keys:
        common = CommonGroup(dic["common"])
        test = CommonGroup(dic["test"])
        jade = CommonGroup(dic["jade"])
        washer = CommonGroup(dic["washer"])
        brotherAndSister = CommonGroup(dic["brotherAndSister"])
        ourGroup = CommonGroup(dic["ourGroup"])
        dhrGroup = CommonGroup(dic["dhrGroup"])
        return {"common": common,
                "test": test,
                "ourGroup": ourGroup,
                "dhr": dhrGroup,
                "jade": jade,
                "washer": washer,
                "brotherAndSister": brotherAndSister
                }

    if "common" and "jj" in keys:
        common = CommonPerson(dic["common"])
        jj = CommonPerson(dic["jj"])
        return {"common": common, "jj": jj}

    if "isAllEnabled" in keys:
        return Analysis(dic)

    if "feature" in keys:
        feature_dic = dic["feature"]
        group_dic = feature_dic["group"]
        personal_dic = feature_dic["personal"]
        group = Group(
            group_dic["common"],
            group_dic["test"],
            group_dic["ourGroup"],
            group_dic["dhr"],
            group_dic["jade"],
            group_dic["washer"],
            group_dic["brotherAndSister"]
        )
        personal = Personal(personal_dic["common"], personal_dic["jj"])
        feature = WeChatFeatureToggle(group, personal, feature_dic["analysis"])
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

    def __init__(self, group: Group, personal: Personal, analysis: Analysis):
        self.group = group
        self.personal = personal
        self.analysis = analysis


if __name__ == '__main__':
    toggle = WeChatFeatureToggle.instance()
    print(toggle.group.common.__dict__)