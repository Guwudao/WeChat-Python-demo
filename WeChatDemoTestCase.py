from unittest import TestCase
from WeChatFeatureToggle import WeChatFeatureToggle
from WeChatAction import WeChatAction


class WeChatDemoTestCase(TestCase):
    chat_room_member = [
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@29bde775f477d23c870e8f8bfb5afaf9",
            "NickName": "ViAnNa-黄英",
            "AttrStatus": 122983,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": "yin"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@6e42fbfebf4a1bf047fef9a108f6d25b",
            "NickName": "winter 李彬特",
            "AttrStatus": 16882495,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "李彬特 winter",
            "KeyWord": "for"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@a8e53ac9a9c7632d79d7a844ef207c7a",
            "NickName": "戴国明",
            "AttrStatus": 16980071,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "戴国明-MING",
            "KeyWord": "min"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@826978e47c47a477c8e3ad8cf12bc64312d791a1f803fa4bab9a41d33a2bc4c1",
            "NickName": "Harvey-黄文斌",
            "AttrStatus": 17012669,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "黄文斌_Harvey",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@5afe58cf92512cc7700340a29daa487b",
            "NickName": "估唔到",
            "AttrStatus": 121957,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "林俊杰 - Jackie",
            "KeyWord": "kil"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@4d15cbcaf524e38d22400990964ed042b2e91a9bbf55d5fbe79413c5278ea220",
            "NickName": "张广洋 Ternence",
            "AttrStatus": 233575,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "张广洋-Ternence",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@1020cc7910d6c4afa10c7ab9d3a82af617d62134f5b659bba1bc93e9fce3d1d7",
            "NickName": "Carl-陈洋平",
            "AttrStatus": 233829,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "陈洋平-Carl",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@ea5fd403d5f0bfe7456f618f32d42029588bc610f8f6a6d536757b5f085786dd",
            "NickName": "Sheldon Xie",
            "AttrStatus": 4427877,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "谢毅滦–Sheldon",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@af9355d056188ad9eec151ca6d5637b6a3a6e3f6b9f609ccdd054226407ce792",
            "NickName": "何志伟Daniel",
            "AttrStatus": 17007357,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "何志伟Daniel",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@dccfd70680f9a047462c36fb6b938883",
            "NickName": "Caesar文逸俊",
            "AttrStatus": 33657383,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "文逸俊 - Caesar",
            "KeyWord": "pko"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@148ea75a9d575d86594f40ba811be2ab",
            "NickName": "刘旭斌",
            "AttrStatus": 100391,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "刘旭斌Daniel",
            "KeyWord": "kod"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@e9c03412002169b00d92158a996935486a7b11a8023aee907daf7495be07f153",
            "NickName": "唐小兵",
            "AttrStatus": 102501,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "唐小兵 Leo",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@3d6ad0d1e69fadf0cb50e97c0689c653b6dbb34c9a570a8df6f67390ee6e6ae4",
            "NickName": "郑永祥 Michael",
            "AttrStatus": 33788773,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "郑永祥-Michael",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@5bb738f2b465fcd42a168877ff5b048211bccc676d14dccbb3fcb21847bc18db",
            "NickName": "lanmon 梁敏瑜",
            "AttrStatus": 98407,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "梁敏瑜 lanmon",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@0e73f601217ccad9330b8dedcf4c0199",
            "NickName": "叶超 Charles Java",
            "AttrStatus": 33658919,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "叶超-Charles",
            "KeyWord": "cs5"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@cd76ec220a50bd23da10873cddba8f56",
            "NickName": "凌俊杰 iOS",
            "AttrStatus": 114791,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "凌俊杰-Jason",
            "KeyWord": "lin"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@31d7e41a12eca85c7308fec865162f3d09229092d502145b00d03d6aea0eed1a",
            "NickName": "Anson曾昊",
            "AttrStatus": 111869,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "曾昊 Anson",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@0db4a94d989c0f79758a28570cf913d7",
            "NickName": "Leslie 江克非 SM",
            "AttrStatus": 33786303,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "江克非-Leslie",
            "KeyWord": "les"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@9f401e6e922ca61108b3823b566f30ee3afb39b596f81a431930c061e806463d",
            "NickName": "于顺燊 iOS",
            "AttrStatus": 102437,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "于顺燊-Justin",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@6aa2242678de26d05c51722923b7e1d6",
            "NickName": "郑绵毅Manny",
            "AttrStatus": 37847935,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": "man"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@fdcd413958faf36fc71fe9e169f9b6d246bddb2fc4b7cfd9d854b8583e54048b",
            "NickName": "Java 杨元生",
            "AttrStatus": 102501,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "杨元生-Yeson",
            "KeyWord": "yan"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@b1c67ae05c8d5d0d533149719a58faf6",
            "NickName": "Daisy苏倩怡RM ",
            "AttrStatus": 231527,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": "dai"
        }
    ]

    def test_analysis(self):
        toggle = WeChatFeatureToggle.instance()
        analysis = toggle.analysis

        self.assertFalse(analysis.isAllEnabled)
        self.assertFalse(analysis.sexAnalysis)
        self.assertFalse(analysis.barCity)
        self.assertFalse(analysis.barProvince)
        self.assertFalse(analysis.pieCity)
        self.assertFalse(analysis.pieProvince)
        self.assertFalse(analysis.geoProvince)
        self.assertFalse(analysis.pyechartsWordCloud)
        self.assertFalse(analysis.pilWordCloud)

    def test_wechatCommonGroupFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        common = toggle.group.common
        self.assertEqual(common.expectedList, ["摸铃校友群", "骑洗衣机去地铁站", "【兄弟姐妹】", "Jade", "测试群", "Our Group"])
        self.assertTrue(common.queue)
        self.assertFalse(common.imageReturn)
        self.assertTrue(common.mapAnalysis)
        self.assertTrue(common.envelope)
        self.assertFalse(common.autoReply)
        self.assertTrue(common.atMeReply)

    def test_wechatTestGroupFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        test = toggle.group.test
        self.assertEqual(test.expectedList, [])
        self.assertTrue(test.queue)
        self.assertTrue(test.imageReturn)
        self.assertTrue(test.mapAnalysis)
        self.assertTrue(test.envelope)
        self.assertFalse(test.autoReply)
        self.assertTrue(test.atMeReply)

    def test_wechatJadeFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        jade = toggle.group.jade
        self.assertEqual(jade.expectedList, ["林俊杰", "张广洋", "谢毅滦", "陈洋平", "戴国明", "唐小兵", "刘旭斌", "何志伟",
                                             "杨元生", "文逸俊", "黄文斌", "李彬特", "郑永祥", "梁敏瑜", "曾昊",
                                             "于顺燊", "凌俊杰", "江克非", "郑绵毅"], "expect list should be equal")
        self.assertTrue(jade.queue)
        self.assertFalse(jade.imageReturn)
        self.assertTrue(jade.mapAnalysis)
        self.assertTrue(jade.envelope)
        self.assertFalse(jade.autoReply)
        self.assertFalse(jade.atMeReply)

    def test_wechatWasherFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        washer = toggle.group.washer
        self.assertEqual(washer.expectedList,
                         ["离婚分一半", "@@@", "吓\n得\n我\n昵\n称\n都\n空中旋转劈叉了", "军佬屌仔三米长，仲识分叉", "霸王别鸽",
                          "罗平滢", "JJ"], "expect list should be equal")
        self.assertTrue(washer.queue)
        self.assertFalse(washer.imageReturn)
        self.assertTrue(washer.mapAnalysis)
        self.assertFalse(washer.envelope)
        self.assertFalse(washer.autoReply)
        self.assertFalse(washer.atMeReply)

    def test_brotherAndSisterFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        bns = toggle.group.brotherAndSister
        self.assertEqual(bns.expectedList, [], "expect list should be equal")
        self.assertFalse(bns.queue)
        self.assertFalse(bns.imageReturn)
        self.assertTrue(bns.mapAnalysis)
        self.assertTrue(bns.envelope)
        self.assertFalse(bns.autoReply)
        self.assertTrue(bns.atMeReply)


    def test_wechatCommonPersonalFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        common = toggle.personal.common
        self.assertTrue(common.imageReturn)
        self.assertTrue(common.mapAnalysis)
        self.assertFalse(common.envelope)
        self.assertFalse(common.autoReply)

    def test_weChatJJFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        jj = toggle.personal.jj
        self.assertFalse(jj.imageReturn)
        self.assertTrue(jj.mapAnalysis)
        self.assertTrue(jj.envelope)
        self.assertFalse(jj.autoReply)

    def test_weChatReminderLessThanTen(self):
        toggle = WeChatFeatureToggle.instance()
        jade_members = toggle.group.jade.expectedList
        new_msg = """
                    #接龙
                    6月12日welink健康打卡

                    1. 林俊杰 - Jackie
                    2. 江克非-Leslie
                    3. 戴国明-MING
                    4. 张广洋-Ternence
                    5. 何志伟Daniel
                    6. 黄文斌_Harvey
                    7. 刘旭斌Daniel
                    8. 杨元生-Yeson
                    9. 谢毅滦–Sheldon
                    10. 李彬特 winter
                    """
        reminder = """ 6月12日welink健康打卡 
@陈洋平-Carl 
@文逸俊 - Caesar 
@唐小兵 Leo 
@郑永祥-Michael 
@梁敏瑜 lanmon 
@凌俊杰-Jason 
@曾昊 Anson 
@于顺燊-Justin 
@郑绵毅Manny 
未打卡人数还剩 9 人"""

        result = WeChatAction.jade_auto_reminder(self.chat_room_member, jade_members, new_msg)
        self.assertEqual(result, reminder)

    def test_weChatReminderMoreThanTen(self):

        toggle = WeChatFeatureToggle.instance()
        jade_members = toggle.group.jade.expectedList
        new_msg = """
                    #接龙
                    6月12日welink健康打卡
            
                    1. 林俊杰 - Jackie
                    2. 江克非-Leslie
                    3. 戴国明-MING
                    4. 张广洋-Ternence
                    5. 何志伟Daniel
                    6. 黄文斌_Harvey
                    7. 刘旭斌Daniel
                    8. 杨元生-Yeson
                    """
        reminder = None

        result = WeChatAction.jade_auto_reminder(self.chat_room_member, jade_members, new_msg)
        self.assertEqual(result, reminder)

    def test_weChatReminderComplete(self):
        toggle = WeChatFeatureToggle.instance()
        jade_members = toggle.group.jade.expectedList
        msg = """
            #接龙
            6月15日welink健康打卡

                1. 林俊杰 - Jackie
                2. 凌俊杰-Jason
                3. 黄文斌_Harvey
                4. 何志伟Daniel
                5. 文逸俊 - Caesar
                6. 叶超-Charles
                7. 张广洋-Ternence
                8. 于顺燊-Justin
                9. 曾昊 Anson
                10. 刘旭斌Daniel
                11. 戴国明-MING
                12. 杨元生-Yeson
                13. 郑永祥-Michael
                14. 郑绵毅-Manny
                15. 江克非-Leslie
                16. 谢毅滦–Sheldon
                17. 李彬特 winter
                18. 陈洋平-Carl
                19. 唐小兵-Leo
                20. 梁敏瑜-Lanmon
        """
        reminder = "恭喜大家完成本次接龙！！！"
        result = WeChatAction.jade_auto_reminder(self.chat_room_member, jade_members, msg)
        self.assertEqual(result, reminder)

    def test_weChatActionGetTitle(self):
        msg = """#接龙
                6月12日welink健康打卡

                1. 林俊杰 - Jackie
                2. 江克非-Leslie
                3. 戴国明-MING
                4. 张广洋-Ternence
                5. 何志伟Daniel
                6. 黄文斌_Harvey
                7. 刘旭斌Daniel
                8. 杨元生-Yeson
                9. 谢毅滦–Sheldon
                """
        title = " 6月12日welink健康打卡 " + "\n"
        result = WeChatAction.get_title(msg)
        self.assertEqual(result, title)

    def test_reminder(self):
        toggle = WeChatFeatureToggle.instance()
        jade_members = toggle.group.jade.expectedList
        msg = """
#接龙
6月21日welink健康打卡

1. 林俊杰 - Jackie
2. 于顺燊-Justin
3. 何志伟Daniel
4. 李彬特 winter
5. 郑永祥-Michael
6. 陈洋平-Carl
7. 文逸俊 - Caesar
8. 凌俊杰-Jason
                """

        result = WeChatAction.jade_auto_reminder(self.chat_room_member, jade_members, msg)
        print(result)

    def test_our_group(self):
        group_nickname_list = ['Jackie 林俊杰', 'Wave严其龙', 'Phoenix', 'Kevin 梁思羽', '郑永祥Michael', 'Sheldon 谢毅滦', 'Ternence张广洋', 'Harvey', 'Adrian', 'Felix Fang', 'Sheldon曾超龙', '彭伟涛', 'Kolor 陈家乐', 'JackCode ', 'Kyle 余翼', '覃淇韩', 'Charles YE', '蔡日雄', 'Jason- 凌俊杰', 'JKF Leslie', '苏倩怡Daisy', 'Avater', 'Gami', 'Driven-卢平清', '王权斌', 'jack谢祎龙', 'Hamy', 'Cloud李易承', '阮焯城', '杨成业', '郭明健_iOS', 'Rosh', '黄江胜', 'JIM曾俊杰', 'Lynn 林聪', '蔡淑珍']

        group_display_name_list = ['Kyle.C', '一碌蔗', 'mobius', 'Sandy志杰', '易风', 'KNOX', 'F.H²⁰²¹', 'Draven', 'jan', 'Socus', 'ZW', '麦田', '陈红洋', 'lanmon', '斌', 'Caesar', '星夜', 'Vico Ye', 'Edwin', 'Frank_Zhong', '夏锐东', '金鱼', '方方方。。。方颖欢', 'xx', 'Kid', 'Juyee·zzy', '傍晚吃酒看花', 'zion¹⁹⁹¹', 'Sun', '曾慶龍', 'Boris', '唐', 'Manny', 'oldfish燊', 'Anson', 'ViAnNa', 'WB', '猫君2.0', 'Housem Mark', '雪花', '俏如来', '詹前力 LIVEN', '奕', 'seanhuang', '梓帆', '火炉烫小铁匠', '樊朵', 'blingbling', '小欣', '夜风奇', 'nineSean']

        print(len(group_nickname_list))
        print(len(group_display_name_list))
