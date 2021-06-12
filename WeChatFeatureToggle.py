import json


class CommonGroup:

    def __init__(self, expectList, queue, img, mapAnalysis, envelope, auto):
        self.expectList = expectList
        self.queue = queue
        self.imageReturn = img
        self.mapAnalysis = mapAnalysis
        self.envelope = envelope
        self.autoReply = auto


class CommonPerson:
    def __init__(self, img, mapAnalysis, envelope, auto):
        self.imageReturn = img
        self.mapAnalysis = mapAnalysis
        self.envelope = envelope
        self.autoReply = auto


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
        jade_dic = dic["jade"]
        jade = CommonGroup(jade_dic["expectList"], jade_dic["queue"], jade_dic["imageReturn"],
                     jade_dic["mapAnalysis"], jade_dic["envelope"], jade_dic["autoReply"])

        washer_dic = dic["washer"]
        washer = CommonGroup(washer_dic["expectList"], washer_dic["queue"], washer_dic["imageReturn"],
                       washer_dic["mapAnalysis"], washer_dic["envelope"], washer_dic["autoReply"])

        return {"jade": jade, "washer": washer}


    if "common" and "jj" in keys:
        common_dic = dic["common"]
        common = CommonPerson(common_dic["imageReturn"], common_dic["mapAnalysis"], common_dic["envelope"], common_dic["autoReply"])

        jj_dic = dic["jj"]
        jj = CommonPerson(jj_dic["imageReturn"], jj_dic["mapAnalysis"], jj_dic["envelope"], jj_dic["autoReply"])
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

        print(result.group.jade.queue)
        print(result.group.jade.imageReturn)
        print(result.group.jade.mapAnalysis)
        print(result.group.jade.envelope)
        print(result.group.jade.autoReply)
        print("-" * 50)
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