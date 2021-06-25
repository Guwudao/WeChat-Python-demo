from unittest import TestCase
from WeChatFeatureToggle import WeChatFeatureToggle
from WeChatAction import WeChatAction


class WeChatDemoTestCase(TestCase):
    jade_chat_room_member = [
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

    our_group_chat_room_member = [
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@15dc02d81d38de278f47447f296597a0",
            "NickName": "Kyle.C",
            "AttrStatus": 67903,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Kyle 程珺",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@1b4195e9cdaa2814dad24c30f1a85138",
            "NickName": "估唔到",
            "AttrStatus": 121957,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "林俊杰 Jackie",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@597031bec88f8e4246aad695c41043ef",
            "NickName": "Wave",
            "AttrStatus": 231525,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "严其龙Wave",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@204b28e25e4bc9b3bc832074a319799a68d99ee78db683b7bcdde20294d3cbb0",
            "NickName": "一碌蔗",
            "AttrStatus": 50565221,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "罗文轩 Hins W X Luo",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@d819bb0541d34a3ea99e47da5bfe3dcdd081f1ae653b0140b92ed68e24af23bb",
            "NickName": "我是婷婷🐾",
            "AttrStatus": 50430309,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "伍楚婷＋Phoenix",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@ba911bc2b5a167b9a692d28bd6119f7d",
            "NickName": "mobius",
            "AttrStatus": 102783,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "秦宗健 Ajian",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@42b1d60737c9a85a09bcddf04ad91e236ede4b69f70eace8e36e48c28af7fc73",
            "NickName": "Sandy志杰",
            "AttrStatus": 102757,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "志杰+Sandy",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@77629b52941d2203c4eb082e00fc6b3b65e230269fa077a1bc4267a119dc2f4f",
            "NickName": "易风",
            "AttrStatus": 107751,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "刘远明 Nicky",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@0214a3d9f3c28333867bdca826e5a300",
            "NickName": "KNOX",
            "AttrStatus": 50563007,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "曹伟江-KNOX",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@5b1c5717a4e99bb7a019b6e895f7836a",
            "NickName": "F.H²⁰²¹",
            "AttrStatus": 233573,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "樊华Leon",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@9701f7d11738387481471a53798c38d59745c2a6b6c9e089f7f4959f41c50cd1",
            "NickName": "花丶蛤西",
            "AttrStatus": 4285,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Kevin 梁思羽",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@3e2b81fefec13f4b6173b67d96e33e12",
            "NickName": "Draven",
            "AttrStatus": 33661031,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "梁斌文Draven",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@7a00ff127d2454098be329c67a91face",
            "NickName": "jan",
            "AttrStatus": 99175,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "冼静 Jane",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@9688872d749c2a6a69fd79b844a786f1",
            "NickName": "Socus",
            "AttrStatus": 16980071,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "戴国明-Ming",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@e1a157de2900024a01d54af3e8728798d22e97944c3f07efeef61ea8082b15bf",
            "NickName": "阿祥",
            "AttrStatus": 33788773,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "郑永祥Michael",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@98c83b6b6cf12712ce875ed9b27d70943e6f24ac2c43e442c1c84e48d9f82f1c",
            "NickName": "Sheldon Xie",
            "AttrStatus": 4427877,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Sheldon 谢毅滦",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@c29002b42a70783188a569fc82e70f62c7c0a5d39fb1d895575815894a6a0a32",
            "NickName": "ZW",
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
            "UserName": "@73791a5db7265f97a507a23ea410f1e1",
            "NickName": "麦田",
            "AttrStatus": 16882495,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "李彬特 winter",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@60323638bfd0bfb94e38d508b1df923a9044f3d169b871ac5d9c44d1b93d9ed3",
            "NickName": "洋子",
            "AttrStatus": 233575,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Ternence张广洋",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@a93004be49a017773c60d0d9f12c435dc92c5d06f574c26afffcf54f80c8f045",
            "NickName": "陈红洋",
            "AttrStatus": 233829,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "陈洋平—Carl",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@6042d2d339c4700f9f50df4056ca0b5d5801f33250e97134108352b271909e16",
            "NickName": "lanmon",
            "AttrStatus": 98407,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "lanmon梁敏瑜",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@590aa920143e512962eef1aff0577b1eb174dc95546a14ade527a5bc7fa0a337",
            "NickName": "H",
            "AttrStatus": 17012669,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "黄文斌-Harvey",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@0f0715296c832971ed05511e01fbd86f",
            "NickName": "斌",
            "AttrStatus": 100391,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "刘旭斌Daniel",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@cf9baf3321da45032f144fc611545217",
            "NickName": "Caesar",
            "AttrStatus": 33657383,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "文逸俊 Caesar",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@796ff3cbd45452ab1b4932a1459600cca24123f34a070c4e1f9dba1ced6b0b84",
            "NickName": "星夜",
            "AttrStatus": 102501,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Leo 唐小兵",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@2e311ee000a43f4153dbba949b10348e",
            "NickName": "Vico Ye",
            "AttrStatus": 202855,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@a18e2ba8165e8b4d1890d360aeb96a5e",
            "NickName": "Eightree Wei",
            "AttrStatus": 234623,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "韦溢泉Adrian",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@e234969d6282ac1153d8cfd1bb40caf44541ca94f3eb3a0c30b29d00b91da121",
            "NickName": "😊🎉",
            "AttrStatus": 102781,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "方向 Felix",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@c448ff9a34046838910843b8aef6de203480f3e57ae19c5b032eeaf4f674afbf",
            "NickName": "Edwin",
            "AttrStatus": 200767,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "朱雄伟 Edwin",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@9ff3f9e39a9f0ec96bbab2204ebbffb0",
            "NickName": "Frank_Zhong",
            "AttrStatus": 33665127,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Frank 钟灵",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@09b4c79e0a0cb8d7253debd1aa91af651610d596e8e0c71abdfc4435ecad98a6",
            "NickName": "小凳子",
            "AttrStatus": 103525,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "曾超龙_Sheldon",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@2a67b3fd15d6180dae15190cba8631b291d843a5c3f551dbbdb7a5eb133b6d26",
            "NickName": "Stefan",
            "AttrStatus": 109735,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "彭伟涛-Stefan",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@cd02bbe1914c4f4334d2104506012178",
            "NickName": "夏锐东",
            "AttrStatus": 234471,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@f3a3ee8dd1a6d3f06e25d26ca2c9db0eaa7f71879e75120ba86eabd3f9479b5d",
            "NickName": "🐮",
            "AttrStatus": 242559,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Kolor 陈家乐",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@fceaf666753be84098407f5d47fda1846ff48efed057c462d95a4106c2eabd99",
            "NickName": "刘洪威",
            "AttrStatus": 100677,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "刘洪威 JackCode ",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@91f5e198927ac3030d6d5499d1060a6e1bd7d6ec18841e12205f698da37cf7dc",
            "NickName": "金鱼",
            "AttrStatus": 167975,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "李锦宇-joke",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@ccad6bd815ccdd868fd5992c2fb53db8b0543a1bb80f7d4ec6ba5a6fe449b5df",
            "NickName": "方方方。。。方颖欢",
            "AttrStatus": 33653061,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "方颖欢 Huan",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@e3082649f6f9275e8d14ef16c5b51b666ae3e906bc8af7e82da9db9b985e0f3f",
            "NickName": "xx",
            "AttrStatus": 33790269,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Alison",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@dc2af4c827b69d4d9caeac643dfc4605",
            "NickName": "😂😂😂😂😂",
            "AttrStatus": 104549,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Kyle 余翼",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@c590c732d1ef88b358f4d1998a43817f5af367a903d41dda3044ef45e9911c84",
            "NickName": "Ā白玫瑰,依旧是床前明🌙 光",
            "AttrStatus": 16879741,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "覃淇韩",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@29c625ad92843e309a793de30cec0c0f",
            "NickName": "Kid",
            "AttrStatus": 75047,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "刘嘉奇Kid",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@692ea3f3d326e6144b594be8b359c357",
            "NickName": "Juyee·zzy",
            "AttrStatus": 98751,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Juyee 朱宇",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@b10bffb4fc4e7d263821c67194472807694529f0f0594ab1164f3624b0e36757",
            "NickName": "傍晚吃酒看花",
            "AttrStatus": 236325,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "叶庭强-jack",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@6fac387f93fa198cd47b2ce6f6327b34",
            "NickName": "zion¹⁹⁹¹",
            "AttrStatus": 200831,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "zion 徐治安",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@198088b3bed3e6105ce1b0d3b26571d1b6177726ddd43a073e092c56720fd16b",
            "NickName": "Sun",
            "AttrStatus": 2147582053,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "孙健强-Joey",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@b2301bead9bc34edbc90c3212b6f3dcb",
            "NickName": "曾慶龍",
            "AttrStatus": 4280615,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "曾慶龍max",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@0a9f4a9b953edbfd0f1ff6a5ff7ef449b9e7697bbf9d73f081d352e77e012b20",
            "NickName": "Boris",
            "AttrStatus": 102501,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "黄波-Boris",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@b804260ce41d9ecb7aac5f16bf80605e",
            "NickName": "唐",
            "AttrStatus": 102439,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "唐友华-tom",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@db305cc4363b7866a9de1341308261d0462e8f8398de80add315124c488d6c49",
            "NickName": "子厘车",
            "AttrStatus": 72741,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "蔡日雄Symbol",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@2cb1f92a4e58930b36d86ab26da15133",
            "NickName": "Manny",
            "AttrStatus": 37847935,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "郑绵毅-Manny",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@d626a6e47cf9884fd5c0fcaf3e2c6dbc",
            "NickName": "凌傑",
            "AttrStatus": 114791,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Jason- 凌俊杰",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@60413fc4a47965ea5f14f867b410ed8f",
            "NickName": "JKF",
            "AttrStatus": 33786303,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "江克非 Leslie",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@de0938b1075ab1e6770a2b939bf21fb4fbef43f86aeca05d033e5dbc271ef064",
            "NickName": "oldfish燊",
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
            "UserName": "@ed83c253cb74a53c3437ee3ec4da3db90aab1b51e3980af6792656cc1d7e9af5",
            "NickName": "Anson",
            "AttrStatus": 111869,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "曾昊Anson",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@3b425e856f0be59673b84e8df9e3887d",
            "NickName": "Daisy.🍒",
            "AttrStatus": 231527,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "苏倩怡Daisy",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@4c5eedd1bc0420eca1677e249a0e49b7",
            "NickName": "ViAnNa",
            "AttrStatus": 122983,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@f5a427105f8a293e2f6eeceeee7d91a0",
            "NickName": "WB",
            "AttrStatus": 110631,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "徐鹏_Westbrook",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@11024c4f1c590459acbbdc4c32bdb7369977a7406cf96df55088435b943d3b68",
            "NickName": "Excetion",
            "AttrStatus": 33796581,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "王伟达-Avater",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@257bf4631830ff276bb51da3c440cbc61b1915716d50bc97d80dadca6bdafd05",
            "NickName": "Sharon❇",
            "AttrStatus": 233509,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "胡嘉敏-gami",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@6a2091ec354ab249cce90bf417ee084f22fb8f3a50acc816656f7fa6912d7680",
            "NickName": "猫君2.0",
            "AttrStatus": 104549,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "龚定显captain",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@566384ae78090485012f1eb6cee9b35809668182741f4768ff69b6882d79f750",
            "NickName": "Two steps from hell",
            "AttrStatus": 231717,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Driven-卢平清",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@fbf8494744c2b97ff280f7649eabaac3bf23acc513d3b925248bff264691f892",
            "NickName": "Housem Mark",
            "AttrStatus": 135205,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "马仲豪 Housem Mark",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@f457f4103dacbb55d78b5655362777fba9d5e18487c8e4fcbd0be1ee9bb9847e",
            "NickName": "Kyunban.Wong",
            "AttrStatus": 233887,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "王权斌-Sam",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@e68e94a12c59a623b9e7cbef9127a4dd7ace65ec285c3cdecd45f4507fc603bd",
            "NickName": "yilong",
            "AttrStatus": 233509,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "jack谢祎龙",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@a9e2f9bec6cf2df5c09c01c26c4a8ee59a2a4808655fb00ccc065532a8689aa1",
            "NickName": "雪花",
            "AttrStatus": 102501,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "杨元生",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@2767041250619316f7c7a10549b1cf727839d1cb1c0b5dc47af5f9e4155c4a2e",
            "NickName": "HAMY",
            "AttrStatus": 104485,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "高海梅 Hamy",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@cb83c9f1a502ff1d47d1c648ecbdbd49",
            "NickName": "半藏",
            "AttrStatus": 50565223,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Cloud李易承",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@b042ab2b28a2a068e6b33a3e4d59039f0dee1a6798a062a82bd6a41b9c5d1e85",
            "NickName": "俏如来",
            "AttrStatus": 102757,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "刘建军-Thnaos",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@efb1707788cc8faa3f7d7525088f5340000d7cc585c7837e8c8782293ce9204c",
            "NickName": "詹前力 LIVEN",
            "AttrStatus": 33657189,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@23203729d064db16c27e9550885209bd86a43d4934369d8930af3429496c50e4",
            "NickName": "吴织咩嘢城",
            "AttrStatus": 100773,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "阮焯城",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@4f3cd73b3cd1a1088ba4a51ce08bd7921e0e3eb74011ee77b2356df4f3ea8a63",
            "NickName": "杨小过",
            "AttrStatus": 229669,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "杨成业－Curry",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@4094a9032879063489aab4c225a4542d",
            "NickName": "Joy",
            "AttrStatus": 4315239,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Joy_郭明健",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@24cab2173484ebc32c613f6223a78752bdfd998c1be185c82735b67790e5dfc0",
            "NickName": "Done.🦁🦁",
            "AttrStatus": 102845,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "丁小双 Rosh",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@372df83b8ec85e9ce42260d01be546b7",
            "NickName": "胜哥",
            "AttrStatus": 232871,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "黄江胜",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@502c4914b960accdca77edf20aa11f67001a9543e5128198f1dc37a45a444e72",
            "NickName": "奕",
            "AttrStatus": 4301925,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "陈奕Yee",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@d26fdcd1a2956d88dd16fb9d44782bd2",
            "NickName": "seanhuang",
            "AttrStatus": 33753277,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "黄少强-seanhuang",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@8fcfdbcc6e0cf7f2d6612aaa162d08fd",
            "NickName": "JIM俊",
            "AttrStatus": 233575,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "JIM曾俊杰",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@167687b808a596c86e574cecc9bf414efa9bece652a643f9e1fca3e21caa83db",
            "NickName": "梓帆",
            "AttrStatus": 233829,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "周梓帆-Jerry",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@2aaddca95f1d42fbd4e5685b4cf2feed147a54a51afb3cb5f6082f35e01d86ba",
            "NickName": "火炉烫小铁匠",
            "AttrStatus": 102589,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "张冲_Mack",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@7bf421c8f21364be0d029d3bd1a45089d3d1fcaf623717f55139a5e0ea400779",
            "NickName": "樊朵",
            "AttrStatus": 102845,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@ffccf5a07ee9e1026e35e061dc49a1b6d994b0fbc015a91951e810525d79574c",
            "NickName": "blingbling",
            "AttrStatus": 99261,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "叶杏芳 Crystal",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@c543f5d7fd4cb85dc3df22986bd90454",
            "NickName": "小欣",
            "AttrStatus": 229813,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "叶颖欣june",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@6e9919bac3c8725df7d29d28960c20b8",
            "NickName": "o0／聪0o",
            "AttrStatus": 115135,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "林聪 Lynn",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@eddf664c6525fa692ed5b5b1a7fffe43f82db77493cc678cab017b89d2e213e4",
            "NickName": "珍珍",
            "AttrStatus": 100389,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "蔡淑珍 Kathy",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@9fc379de471ece5ee1f8b73cce2e141d2451dd9442cea3fd7a97d5b1c962284c",
            "NickName": "夜风奇",
            "AttrStatus": 102589,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "周楠 Victoria",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@af05305763802387a9f9d58c3e3aaff4",
            "NickName": "nineSean",
            "AttrStatus": 33788095,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "赖霄-Sean",
            "KeyWord": ""
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
        self.assertTrue("摸铃校友群" in common.expectedList)
        self.assertFalse("网银交付部大群" in common.expectedList)
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

    def test_wechatTestOurGroupFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        ourGroup = toggle.group.ourGroup
        self.assertEqual(ourGroup.expectedList, ["曾超龙", "罗文轩", "伍楚婷", "徐鹏", "林俊杰", "曹伟江", "张广洋", "严其龙", "朱雄伟",
					"钟灵", "樊华", "夏锐东", "叶志扬", "秦宗健", "梁斌文", "李锦宇", "李彬特", "戴国明", "黄文斌", "程珺",
					"梁思羽", "陈洋平", "何志伟", "叶庭强", "刘远明", "刘嘉奇", "冼静", "谢毅滦", "常志杰", "文逸俊", "刘洪威",
					"彭伟涛", "刘旭斌", "唐小兵", "余翼", "黄艳", "陈家乐", "梁敏瑜", "郑永祥", "唐友华", "覃淇韩", "凌俊杰",
					"方颖欢", "曾慶龍", "蔡日雄", "孙健强", "郑绵毅", "王伟达", "黄波", "江克非", "龚定显", "于顺燊",
					"徐治安", "胡嘉敏", "罗兴惠", "马仲豪", "曾昊", "卢平清", "王权斌", "谢祎龙", "詹前力", "刘建军", "杨元生",
					"高海梅", "郭明健", "杨成业", "李易承", "叶颖欣", "阮焯城", "丁小双", "曾俊杰", "黄少强", "陈奕",
					"黄江胜", "张冲", "周梓帆", "林聪", "蔡淑珍", "赖霄", "周楠"])
        print(len(ourGroup.expectedList))
        self.assertTrue(len(ourGroup.expectedList) == 80)
        self.assertTrue(ourGroup.queue)
        self.assertFalse(ourGroup.imageReturn)
        self.assertFalse(ourGroup.mapAnalysis)
        self.assertFalse(ourGroup.envelope)
        self.assertFalse(ourGroup.autoReply)
        self.assertFalse(ourGroup.atMeReply)


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
        
    def test_ourGroupReminder(self):
        toggle = WeChatFeatureToggle.instance()
        group_members = toggle.group.ourGroup.expectedList
        msg = """
            #接龙
6月24日welink健康打卡

1. 林俊杰 Jackie
2. 常志杰Sandy
3. 严其龙 Wave
4. 赖霄-Sean
5. 戴国明-Ming
6. 张冲_Mack
7. 罗兴惠 Kris
8. 伍楚婷＋Phoenix
9. 陈洋平—Carl
10. 叶颖欣june
11. 黄少强-seanhuang
12. 覃淇韩
13. 曾俊杰
14. 郭明健 Joy
15. 郑永祥Michael
16. 陈奕Yee
17. 樊华Leon
18. 周楠 Victoria
19. 于顺燊-Justin
20. 林聪 Lynn
21. 何志伟Daniel
22. 江克非 Leslie
23. 李锦宇
24. 谢祎龙jack
25. 杨成业－Curry
26. 刘远明 Nicky
27. 蔡淑珍 Kathy
28. 冼静 Jane
29. 阮焯城 Sans
30. Cloud李易承
31. 刘旭斌Daniel
32. Kolor 陈家乐
33. 黄波-Boris
34. 曹伟江-KNOX
35. 杨元生_Yeson
36. 周梓帆-Jerry
37. Ternence张广洋
38. 孙健强-Joey
39. Kyle 余翼
40. 方颖欢 Huan
41. Frank 钟灵
42. 高海梅 Hamy
43. 刘洪威JackCode
44. Jason- 凌俊杰
45. 丁小双 Rosh
46. 夏锐东_Ray
47. 罗文轩 Hins W X Luo
48. 彭伟涛-Stefan
49. 詹前力 LIVEN
50. 曾慶龍max
51. 黄江胜 Jason
52. Alison_黄艳
53. 曾超龙_Sheldon
54. Sheldon 谢毅滦
55. 郑绵毅-Manny
56. zion 徐治安
57. 黄文斌-Harvey
58. 蔡日雄Symbol
59. 胡嘉敏-gami
60. Kevin 梁思羽
61. 王伟达-Avater
62. 文逸俊 Caesar
63. 曾昊Anson
64. 朱雄伟 Edwin
65. 秦宗健 Ajian
66. 龚定显captain
67. Kyle 程珺
68. 李彬特 winter
69. 王权斌-Sam
70. 刘建军-Thnaos
        """
        result = WeChatAction.auto_reminder(self.our_group_chat_room_member, group_members, msg, 60)
        print("-" * 100)
        # print(result)
        # print(len(result))
        if result:
            if len(result):
                print("result: ", result)

    def test_weChatJadeReminderLessThanTen(self):
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

        result = WeChatAction.auto_reminder(self.jade_chat_room_member, jade_members, new_msg)
        self.assertEqual(result, reminder)

    def test_weChatJadeReminderMoreThanTen(self):

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

        result = WeChatAction.auto_reminder(self.jade_chat_room_member, jade_members, new_msg)
        self.assertEqual(result, reminder)

    def test_weChatJadeReminderComplete(self):
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
        result = WeChatAction.auto_reminder(self.jade_chat_room_member, jade_members, msg)
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

        result = WeChatAction.auto_reminder(self.jade_chat_room_member, jade_members, msg)
        print(result)

    def test_our_group(self):
        group_display_name_list = ['Kyle 程珺', '林俊杰 Jackie', '严其龙 Wave', '罗文轩 Hins W X Luo', '伍楚婷＋Phoenix', '秦宗健 Ajian', '志杰Sandy', '刘远明 Nicky', '曹伟江-KNOX', '樊华Leon', 'Kevin 梁思羽', '梁斌文Draven', '冼静 Jane', '戴国明-Ming', '郑永祥Michael', 'Sheldon 谢毅滦', '何志伟Daniel', '李彬特 winter', 'Ternence张广洋', '陈洋平—Carl', 'lanmon梁敏瑜', '黄文斌-Harvey', '刘旭斌Daniel', '文逸俊 Caesar', 'Leo 唐小兵', '朱雄伟 Edwin', 'Frank 钟灵', '曾超龙_Sheldon', '彭伟涛-Stefan', 'Kolor 陈家乐', '刘洪威JackCode ', '李锦宇-joke', '方颖欢 Huan', 'Alison_黄艳', 'Kyle 余翼', '覃淇韩', '刘嘉奇Kid', '叶庭强-jack', 'zion 徐治安', '孙健强-Joey', '曾慶龍max', '黄波-Boris', '唐友华-tom', '蔡日雄Symbol', '郑绵毅-Manny', 'Jason- 凌俊杰', '江克非 Leslie', '于顺燊-Justin', '曾昊Anson', '徐鹏_Westbrook', '王伟达-Avater', '胡嘉敏-gami', '龚定显captain', 'Driven-卢平清', '马仲豪 Housem Mark', '王权斌-Sam', '谢祎龙jack', '杨元生_Yeson', '高海梅 Hamy', 'Cloud李易承', '刘建军-Thnaos', '阮焯城 Sans', '杨成业－Curry', '郭明健 Joy', '丁小双 Rosh', '黄江胜 Jason', '陈奕Yee', '黄少强-seanhuang', 'JIM曾俊杰', '周梓帆-Jerry', '张冲_Mack', '叶颖欣june', '林聪 Lynn', '蔡淑珍 Kathy', '周楠 Victoria', '赖霄-Sean']

        group_nickname_list = ['Vico Ye', '夏锐东', '詹前力 LIVEN']

        name = ['曾超龙', '罗文轩', '伍楚婷', '徐鹏', '曹伟江', '严其龙', '朱雄伟', '钟灵', '樊华', '夏锐东', '叶志扬', '秦宗健', '梁斌文', '李锦宇', '程珺', '梁思羽', '叶庭强', '刘远明', '刘嘉奇', '冼静', '志杰', '刘洪威', '彭伟涛', '余翼', '黄艳', '陈家乐', '唐友华', '覃淇韩', '方颖欢', '曾庆龙', '蔡日雄', '孙健强', '王伟达', '黄波', '龚定显', '徐治安', '胡嘉敏', '罗兴惠', '马仲豪', '卢平清', '王权斌', '谢祎龙', '詹前力', '刘建军', '高海梅', '郭明健', '杨成业', '李易承', '叶颖欣', '阮焯城', '丁小双', '曾俊杰', '黄少强', '陈奕', '黄江胜', '张冲', '周梓帆', '林聪', '蔡淑珍', '赖霄', '周楠']

        # print(len(group_display_name_list))
        # print(len(group_nickname_list))
        # print(len(name))

        # print(20 % 4 == 0)
        # print(19 % 4 == 0)
        # print(18 % 4 == 0)
        # print(17 % 4 == 0)
        # print(16 % 4 == 0)
