from unittest import TestCase
from WeChatFeatureToggle import WeChatFeatureToggle

class WeChatDemoTestCase(TestCase):

    def test_wechatJadeFeatureToggle(self):
        toggle = WeChatFeatureToggle()

        jade = toggle.group.jade
        self.assertEqual(jade.expectList, ["林俊杰", "张广洋", "谢毅滦", "陈洋平", "戴国明", "唐小兵", "刘旭斌", "何志伟", "杨元生", "文逸俊", "黄文斌", "李彬特", "叶超", "郑永祥", "梁敏瑜", "曾昊", "于顺燊", "凌俊杰", "江克非", "郑绵毅"], "expect list should be equal")
        self.assertTrue(jade.queue)
        self.assertFalse(jade.imageReturn)
        self.assertTrue(jade.mapAnalysis)
        self.assertTrue(jade.envelope)
        self.assertFalse(jade.autoReply)

    def test_wechatWasherFeatureToggle(self):
        toggle = WeChatFeatureToggle()

        washer = toggle.group.washer
        self.assertEqual(washer.expectList,
                         ["离婚分一半", "@@@", "吓\n得\n我\n昵\n称\n都\n空中旋转劈叉了", "军佬屌仔三米长，仲识分叉", "霸王别鸽", "罗平滢", "JJ"], "expect list should be equal")
        self.assertTrue(washer.queue)
        self.assertFalse(washer.imageReturn)
        self.assertTrue(washer.mapAnalysis)
        self.assertFalse(washer.envelope)
        self.assertFalse(washer.autoReply)

    def test_wechatCommonPersonalFeatureToggle(self):
        toggle = WeChatFeatureToggle()

        common = toggle.personal.common
        self.assertTrue(common.imageReturn)
        self.assertTrue(common.mapAnalysis)
        self.assertFalse(common.envelope)


    def test_wechatJJFeatureToggle(self):
        toggle = WeChatFeatureToggle()

        jj = toggle.personal.jj
        self.assertFalse(jj.imageReturn)
        self.assertTrue(jj.mapAnalysis)
        self.assertTrue(jj.envelope)
        self.assertFalse(jj.autoReply)