from unittest import TestCase
from WeChatFeatureToggle import WeChatFeatureToggle
from WeChatAction import WeChatAction
from datetime import datetime


class WeChatDemoTestCase(TestCase):
    jade_chat_room_member = [
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@c2d0c9a20cc624c11d43b256ee0ca12f",
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
            "UserName": "@a149549513e62346cc06bf80b82b514b",
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
            "UserName": "@9f71bcbd2e3cfd8bd1342914ddf7e678",
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
            "UserName": "@9063d9f85470a97cb13391f6a352e9e030ed6297f530e95b97400887fc61fba3",
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
            "UserName": "@5a66d3ab151f244c51a0c0d971bbfecc",
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
            "UserName": "@c8262c0afa5c7c9a69634c1c33d009d14272f27f96ecc1c17fba1fe59764d2c3",
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
            "UserName": "@42442c705de312b4f27e906249463d05444de4b192d330af8723e88885c5fb34",
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
            "UserName": "@35223bb111b06f678ab86fd627fb98ff8cc3fa14ba0145231b989bd98349fd35",
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
            "UserName": "@b2cf464b8497ec416e4d9f7cfe7afe2407b6ca900a40f6b68d63eab429abfb2a",
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
            "UserName": "@905e83b17c23517c5f30bd0e25c7e956",
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
            "UserName": "@64fb0c4d3cb9115c982f45dbe6fe90fb",
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
            "UserName": "@13933949c493c4a75ecbd20db707fb7c2e262ed87391963d20756a0cd5e99405",
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
            "UserName": "@3a1c1fd4fc77a56392914963f9bcdd25d238f8990cdb603a2e456dc2e0dea433",
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
            "UserName": "@5f609d9f2e71df4494fc4ed7c41061a1",
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
            "UserName": "@2e70a3c4bb37014e8f2758f27cefab6f44608f397d054feafe2c170280f11688",
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
            "UserName": "@1a107b33c42aa3c658215141bc435c13",
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
            "UserName": "@9d45b62bd96e9036c542e03d8d00fd6b948452b1249958ed40123fb7ba6aa06e",
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
            "UserName": "@144ac8abb823f9aece4327d2c1aa385f",
            "NickName": "郑绵毅Manny",
            "AttrStatus": 37847935,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "郑绵毅-Manny",
            "KeyWord": "man"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@5558cfcb85adfbb6abd463fdee8eb3188b93a55e32a592d8e004a671d38b5f78",
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
            "UserName": "@07170c434992fd2550f33cf07f3b0186",
            "NickName": "Daisy苏倩怡RM ",
            "AttrStatus": 100455,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": "dai"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@3e0b81120314bd7aa6cf68a915bc90e0",
            "NickName": "nellie",
            "AttrStatus": 98495,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "Lanmon梁敏瑜",
            "KeyWord": "lia"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@8533f5d545d998eefa38d5def6d456f874da04eb6c18edc861fc29bd20e0a27a",
            "NickName": "蔡淑珍 Kathy PMO",
            "AttrStatus": 100389,
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
            "UserName": "@1243867e3b05eb509a9479bf4e475668",
            "NickName": "林聪 UK convergency iOS",
            "AttrStatus": 115135,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "林聪  Lynn",
            "KeyWord": "lc4"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@f2f73b9cda7cd58940ed469d9b2da11d",
            "NickName": "叶颖欣 UK convergency iOS",
            "AttrStatus": 229813,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": "lov"
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@7a3e22089576b61334012709ec1962481a61b09db9880b639973334f46ce609a",
            "NickName": "廖成龙 UK convergency iOS",
            "AttrStatus": 102501,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "廖成龙-Jacky",
            "KeyWord": ""
        },
        {
            "MemberList": [],
            "Uin": 0,
            "UserName": "@1e9696b5cce3aae34559b1f41b0c17c549e2471a6e6a977e94435e6ee9798093",
            "NickName": "樊朵 RM",
            "AttrStatus": 102845,
            "PYInitial": "",
            "PYQuanPin": "",
            "RemarkPYInitial": "",
            "RemarkPYQuanPin": "",
            "MemberStatus": 0,
            "DisplayName": "",
            "KeyWord": ""
        }
    ]

    our_group_chat_room_member = [
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@7eac72fe912dc373b89323a4dac7a730",
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
        "UserName": "@1d089773de9d4e8ad63081268507c0b6",
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
        "UserName": "@4f59f96f716b357e26cd6944b7141df6",
        "NickName": "Wave",
        "AttrStatus": 231525,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "严其龙 Wave",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5b9a7eb1769353d46c0d282f9115e05935d01799928b105be3eda7304a925d27",
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
        "UserName": "@c006c6f34f015b82bac072b99251b4f696bb1b0f38ec38f1e2397a283ef27660",
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
        "UserName": "@8476cd42477c600c653568cce483bb12",
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
        "UserName": "@c8d0f91d751f004f34cf3b3dc09cc8c323534c8ac842f7101b22ba89042ad23b",
        "NickName": "Sandy志杰",
        "AttrStatus": 102757,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "常志杰Sandy",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@800bd3c839ea64a8181a541f16664f96206d5bc8361537ed8463a93042acd661",
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
        "UserName": "@57ebd111bd38d9d6efe412cff5bd1940",
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
        "UserName": "@734cba06884e5f305dc60a3b79691110",
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
        "UserName": "@63ad4eabc19809a8c62c8cdaf886eabd36948bdd64e28725dc652cd32802c67a",
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
        "UserName": "@99894feb452df930cc354a51bca9b046",
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
        "UserName": "@af8d944352dcf6a69f00709b2214bdc0",
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
        "UserName": "@70ab754cafd2c3098449c0ee8261f930",
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
        "UserName": "@69681929cb9cb588110c8f1cb8fc0a8b9ccd02a3186b5f9207762a32a414aa46",
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
        "UserName": "@99b9062da983d99096d58c14879adb166e2ede01bfb1124784e59e6897531e89",
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
        "UserName": "@27540034d353fce06efaf1bcae031cabcbbd56561cfc7f4d98c9af3f4748f40b",
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
        "UserName": "@652bb464453dbf03f8456f2388282ca7",
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
        "UserName": "@6f4f6967195efa07b3c5f0c03580fc04fb359b7e4c4726a98fb0a0fb7d40122b",
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
        "UserName": "@54622abaf90ed22f8f7c2185020be82bcbfeb914f636bae13d2cf414c652e338",
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
        "UserName": "@3cd972f79ccc20c556592048535225fa768540a2ff1a4939b23299dfee37cb9a",
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
        "UserName": "@a36047e35b0d4e6d5f3dcccbb9d42266",
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
        "UserName": "@cd4a84916caac802714171918be1e02a",
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
        "UserName": "@218e45ad8a57bcd2cd5d7142635ac9de93a11e19425623186bdeebac25919020",
        "NickName": "星夜",
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
        "UserName": "@efce81bdeecf34315e80abf940a53d9b",
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
        "UserName": "@088905898531a4fe9799c1d87aa08948c92697b4b81dc44bef9bb805c565bb17",
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
        "UserName": "@a2e5f81b2daeaf0c81500ed8d965350a",
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
        "UserName": "@4248faacc8a957ba288ca05e69a13d4ec6e86dbb650d21c5d1487b4548bd93ea",
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
        "UserName": "@49c55fca5f5f731792c6b4ccee84339321cf8403edaa2b41905d50b61a6adbfd",
        "NickName": "Stefan",
        "AttrStatus": 109735,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "彭伟涛 Stefan",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5012ef7162113a7ff5f3611a09e1d487c2f8bdfeabf6c21051d2d922ea68c7d0",
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
        "UserName": "@dac4440048222c77b6191393d268af27ec77b283d3789c42048f201808d27b54",
        "NickName": "刘洪威",
        "AttrStatus": 100677,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "刘洪威JackCode ",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@55e84c73ec16a7dbc2845261b8b06c15636c61b2e2cf55f55db9a857bffbd367",
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
        "UserName": "@b2b28c7d5d92aaf90daca498d5513f2904d5968d4376a308abc5860875eb67bc",
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
        "UserName": "@619ff2f65613f7e0720cad4d16f80c76e3fc8817bc0f899d26f68aee045b30fc",
        "NickName": "xx",
        "AttrStatus": 33790269,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "Alison_黄艳",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@e53a69e45d43d082aa769466a5ef3db1",
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
        "UserName": "@c4c231a7bae9d36f5913556aa07d4424dbf974c79d648a690e09e744c1a22215",
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
        "UserName": "@88459d3737f57e0a40fb3944e230c2b7",
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
        "UserName": "@96db7d249388e82e37149ab469a5222b93ad3764d7d27f40fff384a94acc8253",
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
        "UserName": "@3e9cb2946f48481824281b47bc9905b0",
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
        "UserName": "@bffb762e3610463cced36e09d07b72b99e8d40268685b37681b8289a26076209",
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
        "UserName": "@ea02e78d7eef94f17a2bea905d461116",
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
        "UserName": "@7c5986ec5430b447d60d4ad8b0da906f5fc37f57b169a3688833500a30d04dc6",
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
        "UserName": "@055e776f687632b31e74c3086b1c5f03",
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
        "UserName": "@58e8b355ff227313b485903357de666141c65a4990afa90cd75acf8313a7bf33",
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
        "UserName": "@750e4ea1ffc43ac032ba68b3b0c68573",
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
        "UserName": "@7902a944aa0f622ba95ddcf2857756a0",
        "NickName": "凌傑",
        "AttrStatus": 114791,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "凌俊杰Jason",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@fa59d5fd1cd1a3d7f60339383784a412",
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
        "UserName": "@01c69dc2f89a3e2b606b68c6423e3005878b025f785f03fdfa5079e5b47eef11",
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
        "UserName": "@d7fe41f096a073dd46f8fe48c53f5ff954ed43c56fc835fb72d64d313e609018",
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
        "UserName": "@4e9275a8970845082bd3ab306e49ece9",
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
        "UserName": "@65a1884495460a3bfb4ec4884d2baf97",
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
        "UserName": "@2ee716bcdc5edb5a9b396381f9412456",
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
        "UserName": "@213d9b43c96ecc32815b6f9eb294a469ef1f320ea29158cee60fe7eaa90248be",
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
        "UserName": "@5aba59079518a3172f9cc698c1d1b35c290d143c0fb7ec478bc04fa67848c0f8",
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
        "UserName": "@7e593ea37dd44d90201f64c3667458dcfcfc01bf0e48f3e61e15c8fca96c17f9",
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
        "UserName": "@5efeb528d5c6190f13dd95e7f512c68625efb85e3580258728e53f367246d470",
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
        "UserName": "@88271229dcb4027a04bd04a07e44f131a83938e0207cbba2444cef2182132019",
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
        "UserName": "@1d35f50ae0bb3ff5d7f668e72c46c9b5c0fc8134c115be1e00c52fad1bfac9f4",
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
        "UserName": "@fc7ac295e1999a95265569f97ae2089f8179cd6c0bbdd7738d7738aaf1c7c76a",
        "NickName": "yilong",
        "AttrStatus": 233509,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "谢祎龙jack",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c696bd58a84131905e638911067767fe75862361ed6890fe5057bbaa10d6dbfc",
        "NickName": "雪花",
        "AttrStatus": 102501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "杨元生_Yeson",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c98421f3d7af8f95d0001515dccc13d5f99a2399e3836834ae5619b27db24172",
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
        "UserName": "@6968b333a925d17b50361d029aaf2fc8",
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
        "UserName": "@56b3a86ec6ffe4aeab1c71322cdbe56e3d41d2e2466f3f3ec7d3ecf94e929b90",
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
        "UserName": "@f67f3e7c8a33c31639bf7e328d8f2eab625dcb243150af510315c89ec8b7822c",
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
        "UserName": "@3c369b9e9481b72aad8d26f7032ba0133ab9d56b199d52ea12d814da9cdc8fba",
        "NickName": "吴织咩嘢城",
        "AttrStatus": 100773,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "阮焯城 Sans",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@02a5fa8dbdf512db3cdb5f68ef0e1a56e230ec0719bf687b21a5b574de4f7461",
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
        "UserName": "@1eecfb8b1a28df80eaff7eec25c9f54d",
        "NickName": "国家二级烧烤运动员",
        "AttrStatus": 4315239,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "郭明健 Joy",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@7a252a2392ee40926887e7195ba76881d8784e666112b64219354348de068616",
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
        "UserName": "@86cd7063bd033eb8a8319dcb49d877f2",
        "NickName": "胜哥",
        "AttrStatus": 232871,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "黄江胜 Jason",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5b21ce21332c3dbda8b29f46e32a9b564446e3000a2e505b133210ac3d4c602f",
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
        "UserName": "@81fb99ab10d4b683fba38d41a27b7a5a",
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
        "UserName": "@097672ce795a29df71b71870dfe37a12",
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
        "UserName": "@90bb18495c443a60d17c68987c5bf625a20b4aee33f023de28b6bcf5edce077d",
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
        "UserName": "@463d631d8728ff9ba12b50e37cdfa569a97696954fc3394102e0f54ccfba2d5b",
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
        "UserName": "@cd44c6b9bb213633f7a279a8452fa6c687c4ebc5982cb560112dd77daa64f2bd",
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
        "UserName": "@7f3300782f06418b15b08123243b443df9a789325645d5739d352af5dd6be08f",
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
        "UserName": "@81dd71ea71e0892b081dda760ba96d06",
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
        "UserName": "@a1bfa2544c7dd97ca0c51f0fd6b1e6c9",
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
        "UserName": "@1d313e7265bdfe619f709197078200a3f7f15e67c429a51160fe4d43f2d6b0a1",
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
        "UserName": "@c565af3eac438413672b8db79507666cc2a0a95fed16ae3d9e324ed3fc6c7086",
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
        "UserName": "@acc61930896f6c31e07800388f2adb37",
        "NickName": "nineSean",
        "AttrStatus": 33788095,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "赖霄-Sean",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@3010d26471aec08377bfa57b28c6dfeb11df8f3cbbb5586c4df9ab562634b604",
        "NickName": "Kris",
        "AttrStatus": 102759,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "罗兴惠 Kris",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@758af85ebb1da38fc5182b25cd2355f7",
        "NickName": "nellie",
        "AttrStatus": 98495,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "Lanmon梁敏瑜",
        "KeyWord": ""
    }
]

    dhr_group_chat_room_member = [
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@14f050e70638684a3a40bbdbd43aa4a9",
        "NickName": "Kyle 程珺",
        "AttrStatus": 67903,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-程珺Kyle",
        "KeyWord": "q83"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@87aa88fa85b54609df2bd4307e97b42e",
        "NickName": "估唔到",
        "AttrStatus": 121957,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "kil"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@2998296ab7c2581fd7e6ba36b3384461",
        "NickName": "Yo！",
        "AttrStatus": 50536807,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安- 李宏超 Hosea ",
        "KeyWord": "sum"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@24a38963caa21db8e9e345825f41addc",
        "NickName": "陈少轩 Hins",
        "AttrStatus": 99367,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-陈少轩-Hins",
        "KeyWord": "Hin"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@610bfad6efb7270a793f1a77ce7f60db84f6537442a7d9afcf851e4022cd74cf",
        "NickName": "苗苗喵淼",
        "AttrStatus": 242021,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-徐苗淼-Bunny",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@6cc839c0ca9ab52ba33017cbb176ab6e",
        "NickName": "404",
        "AttrStatus": 118653,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-屈欢Bernice",
        "KeyWord": "gua"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@e1bef53fd4fa80fa10a553ea974736726083265ca80fec71d4443de13b85dc55",
        "NickName": "樊朵 RM",
        "AttrStatus": 102845,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-樊朵Fancy",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@4ff77bcd1b361ad25ebc02744fe48362",
        "NickName": "Patrick",
        "AttrStatus": 33758501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-夏睦平Patrick",
        "KeyWord": "xia"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@fa977989827437267a262eb341ff9819",
        "NickName": "莎莎",
        "AttrStatus": 107261,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "kan"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@bd8f0015eb278d036a507212600661dc",
        "NickName": "严其龙",
        "AttrStatus": 231525,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-严其龙 Wave",
        "KeyWord": "yan"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@ab3544e93a5710a0d97c3cfe1e7c603fd2aeffffc54cc38b6ecdb90a8488758d",
        "NickName": "Sandy李凯",
        "AttrStatus": 196965,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-李凯Sandy",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@e05597b815ab7c9aafc3f18db343af1f",
        "NickName": "Jeffrey 林健卜",
        "AttrStatus": 2181273703,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-林健卜-Jeff",
        "KeyWord": "los"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@cfdb1811ad733cbf8c1f989ea9c1ea4d1db56bcab4f8853095bd45e78e3cbc36",
        "NickName": "louis",
        "AttrStatus": 33656933,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州 刘昌旭 louis",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@56785a4ed650251b9d41182afbcd1af0a83db832512d079c46b860be8dc4acd6",
        "NickName": "longdream丹",
        "AttrStatus": 233637,
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
        "UserName": "@c8905575bf0ecefa519b7639a3079f0fd881c9140027628a941c6403c53e8ce1",
        "NickName": "Lee",
        "AttrStatus": 200741,
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
        "UserName": "@80b665afeb7e25103492825e353c5561",
        "NickName": "Barbapapa",
        "AttrStatus": 33659263,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-韩啸Shaun",
        "KeyWord": "hxv"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@030bff84b1fd5f4ba173ba22e5b06d05",
        "NickName": "BeiBeiLewis",
        "AttrStatus": 4294695,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "zhu"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@13bfbc41593545438d1f88f704aa0911e989376a957d7376fea8b04e427df0c1",
        "NickName": "Kiss dream",
        "AttrStatus": 241767,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "wan"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@895f7f038ae7611e92b7736e8a1ab4641ed2d577ae0fc31280fe725f81ba0879",
        "NickName": "Bruce",
        "AttrStatus": 16885631,
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
        "UserName": "@e1ef98e6e070c852fce5b8461960355dbcaa4ced233760ae1b19e32bb195cf50",
        "NickName": "Ashur强曦",
        "AttrStatus": 198845,
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
        "UserName": "@8a8aedd974f453a28f1368f150e170bb",
        "NickName": "xiaoqingwaing",
        "AttrStatus": 102591,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-校婷Tifa",
        "KeyWord": "che"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5db399f5061524c3ce964d88bd402f9b096d6ef640537b24ea2fe6408f47d3bf",
        "NickName": "木夕",
        "AttrStatus": 102501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-李向东-Devin",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@4a7b46b2e417ed4d71e9f146aebea027",
        "NickName": "Kitty",
        "AttrStatus": 111743,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "xa5"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@7080da5d76742c839555f03803be5b66112455bb8f4152f803e6fbd6b8c833b1",
        "NickName": "丫头",
        "AttrStatus": 233509,
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
        "UserName": "@b68e975eb6556f438d11c2849d12bfd63deb76aad91381d178895c6ee2b02a9b",
        "NickName": "刘晶",
        "AttrStatus": 231613,
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
        "UserName": "@ba832d2f84bec217fa199bbb87c7e7b678c327ce58f05853b0efccde34264a07",
        "NickName": "裴明明(Eric.Pei)",
        "AttrStatus": 102437,
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
        "UserName": "@31afc7f732c2a7fa8a6361990def8e8e",
        "NickName": "匆匆",
        "AttrStatus": 98341,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-古靓丽Kevin",
        "KeyWord": "Dat"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c5d22cd488ab414678d99a3a3f7b0f8026f4b9d5f0f73cd000aa149af1667781",
        "NickName": "何志伟Daniel",
        "AttrStatus": 17007357,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-何志伟-Daniel",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5f71feaef73397b4bbdab743e01fc234",
        "NickName": "Lord",
        "AttrStatus": 98559,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-王磊eason",
        "KeyWord": "wl2"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@2aa6871418e9d21e5ad224b8fc63ae78",
        "NickName": "浮一大白",
        "AttrStatus": 236031,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "xia"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@8ce0aa3ef8dbc38ed072a9a558fad397610d14a24598f58d3ffadf9f084edaa3",
        "NickName": "朝朝暮暮",
        "AttrStatus": 135871,
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
        "UserName": "@03e767d5da8557e7a117c92826acc1f745d0adde031a5176e7140796fa5cf11e",
        "NickName": "蔡耀",
        "AttrStatus": 98343,
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
        "UserName": "@5560d039d1c1eedb4d054282a2586a45",
        "NickName": "胡超",
        "AttrStatus": 33665125,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "huc"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@6d213244ef0c7ee53cc2261fc1805ef3",
        "NickName": "翊扬。",
        "AttrStatus": 98343,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "aKu"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@4084c679fd30b476e3495ed6025cc1752c18ea8cb427141dfaeb28328f524d90",
        "NickName": "蔡淑珍 Kathy PMO",
        "AttrStatus": 100389,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-蔡淑珍Kathy",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@f3e4c7fd3ca090167dff7c95872975ef54c8b415583d1a2d0a7ae5ba56de840d",
        "NickName": "肖豫",
        "AttrStatus": 71743,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "Mars-Victor",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@a2eea262d23c30a8aba96e7094443aa3",
        "NickName": "僖帅",
        "AttrStatus": 110695,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-李国僖",
        "KeyWord": "guo"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@d4976c62073a62b8633fc47fc6dd8cb9a48818421fe216bf86d8e649ba1df072",
        "NickName": "Vincent ~ 钟伟强",
        "AttrStatus": 102437,
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
        "UserName": "@0d05278cfd0de997d9c3c3cca003d367bb66c4a37a46ad4396d264b81557a29e",
        "NickName": "吴承炽",
        "AttrStatus": 98405,
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
        "UserName": "@713f30dcbd2a6103cee27cc2ff382500",
        "NickName": "winter 李彬特",
        "AttrStatus": 16882495,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "for"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5d32b2af5f556d468ba8fe570ad5a0de1dd138dffeba2dee26e7b4a0cbc652b4",
        "NickName": "戴权祥",
        "AttrStatus": 98341,
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
        "UserName": "@0d8816cad1e53693265c24442f3da4d6",
        "NickName": "张惠峰",
        "AttrStatus": 229863,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-张惠锋-Lewis",
        "KeyWord": "zhf"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@21c9bb6b0d163f76a63ccdd6d169f2b9",
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
        "UserName": "@86864e97073c36f5871fc64bc4814c7fa424eaf8c4473ac107b972638cd10fa1",
        "NickName": "Carl-陈洋平",
        "AttrStatus": 233829,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州—陈洋平—Carl",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@d6b40a93e40c1c735ad97f413ba4dea18642331d4af467a68c237cb8cebaafc8",
        "NickName": "Sheldon Xie",
        "AttrStatus": 4427877,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-谢毅滦-Sheldon Xie",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@db9e2636e6e3c2e6585fbe1591152511",
        "NickName": "刘旭斌",
        "AttrStatus": 100391,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州_刘旭斌_Daniel",
        "KeyWord": "kod"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@38d8e8f246c0e5b9c839c29bc8d044290efb9d051bf7e01f69fee6b6a7c1f4c4",
        "NickName": "廖成龙 FD convergency iOS",
        "AttrStatus": 102501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-廖成龙-jacky",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@1fa421ec4ace394502f8a64ed20385fd",
        "NickName": "凌俊杰 iOS",
        "AttrStatus": 114791,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "lin"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@8db3697aafd671d72c62551cc09b6a8d150fb42e5ae9e79b34f42d678bd67ff0",
        "NickName": "唐小兵",
        "AttrStatus": 102501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州 唐小兵 Leo",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@6bb79624d2ec40cbf63dc82ef63d9dac4444323d618b9d9b15ba5b37f24f8dbd",
        "NickName": "Java 杨元生",
        "AttrStatus": 102501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "yan"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@6832dbf370fd217d3588b24621d0f94d63097f5ef0e94f05d0c441ba49b7bb2e",
        "NickName": "刘锐 FD convergency 安卓",
        "AttrStatus": 198693,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-刘锐-Jack",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@7f3d8c4d54c0750bd69cbde0f6513555",
        "NickName": "Leslie 江克非 SM",
        "AttrStatus": 33786303,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州- 江克非 Leslie",
        "KeyWord": "les"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5b29bf29f90bff2a693f26f8ea17dd31cfb59fbe62cd7dfbeaebcdfa537ad5fd",
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
        "UserName": "@52c66e40964082e19b2242e26ee085930cbab15506d1d7577b0462f08da54157",
        "NickName": "Minsanity",
        "AttrStatus": 33656865,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "明理Matthew",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@f901c3ec7a563a98b376c3c290ff9698",
        "NickName": "大墨Robin 🌀",
        "AttrStatus": 33785703,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-高龙彬Robin",
        "KeyWord": "mob"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@8c8b4280ff096ec1890dd05fae0fb16f5cb2e0fc8e0b7894976e5ed2d2e5b9b5",
        "NickName": "刘静雯Jene PMO",
        "AttrStatus": 33659837,
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
        "UserName": "@39572090bd48cef86099ac2c4c154ebf",
        "NickName": "幸运在向我招手",
        "AttrStatus": 37986405,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "zha"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@38d500ca702095dcc82ab0a7e1021409",
        "NickName": "Fay",
        "AttrStatus": 2198052327,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "nfs"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@fc96bc8e022bc271fdc5b65c9445f543ee0aa9b2f1d7855d2a89881749594440",
        "NickName": "lanmon 梁敏瑜",
        "AttrStatus": 98407,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-梁敏瑜-lanmon",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5aa7f11281731b461c9a582f407104c7",
        "NickName": "雷克龙 Jackie 安卓",
        "AttrStatus": 33652773,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-雷克龙-Jackie",
        "KeyWord": "lei"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@de3d3d7897e0206333e5806b27c3f1c3bdf2e627ad2936d493c372e7c7eb40bd",
        "NickName": "冬菇丶蒸鸡肉灬",
        "AttrStatus": 98407,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-杨德勇- Mark Yang",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@a3eaa19c58e7cbb5b4f4c7f7499eca2e",
        "NickName": "林聪 FD convergency iOS",
        "AttrStatus": 115135,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-林聪Lynn",
        "KeyWord": "lc4"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@2c4e9333a64efce05fe4116779521c00",
        "NickName": "戴国明",
        "AttrStatus": 16980071,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-Ming",
        "KeyWord": "min"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@3ddfd1b8f34abad545aaab2911f48781",
        "NickName": "Caesar文逸俊",
        "AttrStatus": 33657383,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-文逸俊-Caesar",
        "KeyWord": "pko"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@315957d849b4bf8e169fe3cb4b39d9197771a8a1408c21ecdb98ce8ef43d090c",
        "NickName": "老实人",
        "AttrStatus": 235879,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "陈穗辉",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@93f1aa1eaf8e98ccc47a83e23ba9e0d4",
        "NickName": "就是这么耿直!",
        "AttrStatus": 33652775,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "lxl"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@88ae66b961422fe74fffb0d0187e38e1df16f4a05e8b2acf478b471e01a3876c",
        "NickName": "郑永祥 Michael",
        "AttrStatus": 33788773,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-郑永祥-Michael",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@57a149dc87224d3fa40d49125419ff05f7af2fb116f1fe53a2e7ec0eba38cf58",
        "NickName": "Old@K",
        "AttrStatus": 137317,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-胡启文Kevin",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@4d9d9688a1617a2a657a468912a1c3327e23840ba890a4504996acf23c4f91e5",
        "NickName": "于顺燊 iOS",
        "AttrStatus": 102437,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-于顺燊-Justin",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@83dd32d78125fbb56b499d58b13ce647c814079330a11d7e1321c5e6a0e2a48d",
        "NickName": "Harvey-黄文斌",
        "AttrStatus": 17012669,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-黄文斌Harvey",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@d0044d9cbda91fb728f22fb99e0ebb7310530a9a48ec01ec891262b554a97343",
        "NickName": "张广洋 Ternence",
        "AttrStatus": 233575,
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
        "UserName": "@4862aed20bfc6cfec86bd457484ee931",
        "NickName": "叶颖欣 FD convergency iOS",
        "AttrStatus": 229813,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州 叶颖欣 june",
        "KeyWord": "lov"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@e7997dfdc16af3c6a98780372edfab20",
        "NickName": "……",
        "AttrStatus": 229439,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "n50"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@85cbf2126b8b907a07a4b611da70a197",
        "NickName": "一颗赛艇girl.",
        "AttrStatus": 103359,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-辛月-Jaina",
        "KeyWord": "new"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@38a25ab448ff7160522bcc9cf17c661b6ac72120b826d67460b5d71983c45847",
        "NickName": "我若为风",
        "AttrStatus": 102661,
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
        "UserName": "@ee63f349f953419c4b669e607b4772ee",
        "NickName": "Barry",
        "AttrStatus": 233511,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-慕云飞Barry",
        "KeyWord": "muy"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@06d12fe24a3acf72b098ae1eae39077e815da088715e3365c914d9825c066291",
        "NickName": "沙华",
        "AttrStatus": 233853,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-李银平Ying Ping Li _SP",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@8dfc85b9d423c11379c199a9e0ab7dd522ee20506e6f4ed629ef1d91d7ad763a",
        "NickName": "谢研",
        "AttrStatus": 229861,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-谢研Betty",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@e731122ef7cfa4ed153f76a265a510c8",
        "NickName": "石学慧🕗",
        "AttrStatus": 16881767,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-石学慧Bob",
        "KeyWord": "shi"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b1bc62225813f2b5e5f892095a764bf658a639f33b96781b7a911e3dea600893",
        "NickName": "蚌蚌～",
        "AttrStatus": 229479,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-沙洛沣-Bangbang",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@982bee742f6c891eb81e149366a581269d713dc96d1c4b975f008783e4e462ec",
        "NickName": "arong_breeze",
        "AttrStatus": 104509,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-郭争荣-arong",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@62d778d86a97189b041a232863682ae582926c0c6de062078c452884dd2b1a7c",
        "NickName": "小道",
        "AttrStatus": 229413,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-谷少刚-Allen",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b76534042e60eac2b2bdb61a6017a256f8c9d618680d188ba461cf2a51c38fb0",
        "NickName": "Sugar",
        "AttrStatus": 98429,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安—宋甜甜Suger",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@dfb04fdbe51e5fe78384ae86004db4d9e06eea5f1dfad1973916a9e74b06783a",
        "NickName": "陆聪Bobby",
        "AttrStatus": 104741,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-陆聪聪Bobby",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@e06eed73a937a12ae4c5a223bfb9bd096ffe0e7bacd52934a9e3b6ad5f635dcb",
        "NickName": "Wells",
        "AttrStatus": 2328869,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-wells 韦骏",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@e22386529a9a7a6c4146d3408f4d6c380415f0a2c53d651b91b13477efcc12d0",
        "NickName": "陈飞",
        "AttrStatus": 69733,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-陈飞Lay",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c0faf21db06a13c7840004ad04062ae83a3dc51913acc3dcaf3f8c703b13645d",
        "NickName": "莘灵悦",
        "AttrStatus": 37982245,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-张远鸿-Haley",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@665661e91b5d7a9f08aaf7120fee7176d4e303bb0b63d175f00d88382819beea",
        "NickName": "离殇青素",
        "AttrStatus": 102501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-刘亮亮_Allen",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b44caad87382891aadbb3b070efb09c595ed97a93f770c2006605fafb2a3aaf1",
        "NickName": "Crazy鬼头",
        "AttrStatus": 102437,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-朱正毅Victor",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@fdcf68017dff2cfe0610a763e21435c6e6e3abbc7ec32993dcc92d5704b05131",
        "NickName": "徐雪勇",
        "AttrStatus": 102433,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-徐雪勇-Tyler",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@8a126e9542bec8a2fe378fef8818e6e3",
        "NickName": "🍬",
        "AttrStatus": 68711,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-朱少沛Judi",
        "KeyWord": "Six"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@f6426d60ddbb3d00c708cc805bc7af38c4a336b90d2a92914b8862c7b2972b1c",
        "NickName": "Joey 孙健强 iOS",
        "AttrStatus": 2147582053,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州 孙健强 Joey",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@74872b5816c52ec539d63a696295687073f7c02aa53667c581a4280281c0d5f6",
        "NickName": "阿鲸别熬夜啦",
        "AttrStatus": 33697895,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-赵锡祯Jerry",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5e58c0bf359fd0f0f1c2d3175556a86239028d1114fdbf2824656d0596bb7391",
        "NickName": "王权斌",
        "AttrStatus": 233887,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-王权斌Sam",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@63cb11f62bd1048d63cbe459250c58fa",
        "NickName": "黄少强 iOS",
        "AttrStatus": 33753277,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "im9"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@ee88cf9bf8840f019e81f0ccfe393a5719372c56399e481bf30ac54ae95e783e",
        "NickName": "丁小双 iOS",
        "AttrStatus": 102845,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-丁小双- Rosh",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@98dda6e02c38c3af6e916f779fd58c56c9c0bdc516f6a2322f34c4e3f4a20239",
        "NickName": "张天龙 STMA",
        "AttrStatus": 200893,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-天龙-Talon",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@a44f0a797c376afe1631b3cb7ad2fda3e193a7da2f1a99f73143967f76fb54c9",
        "NickName": "刘建军 iOS",
        "AttrStatus": 102757,
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
        "UserName": "@29bd8d76e03205f7cff5eb1883e5b7bc",
        "NickName": "郭明健iOS",
        "AttrStatus": 4315239,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "guo"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@1af9eb13b473877b937707bfc7677908",
        "NickName": "曾慶龍 iOS",
        "AttrStatus": 4280615,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-曾慶龍-max",
        "KeyWord": "zen"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@14d35e2788ea38b6f5c654199686efc397a9de3bb52aaab7d5d518ad5259b6d2",
        "NickName": "陈奕Android",
        "AttrStatus": 4301925,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-陈奕Yee",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b5db46b3bcac533d1504286ff2c27224",
        "NickName": "KNOX 曹伟江",
        "AttrStatus": 50563007,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-曹伟江KNOX",
        "KeyWord": "cho"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@7d83811ded5b7785509b989e3107e0b7e18ba95a24e44055e9d7889a1ce00a74",
        "NickName": "子厘车",
        "AttrStatus": 72741,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-蔡日雄Symbol",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@1813574e55b2629e54aa32593250d836",
        "NickName": "黄江胜iOS",
        "AttrStatus": 232871,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-黄江胜-Jason",
        "KeyWord": "Jas"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@cd26718db8de8a28004e7e2a836e4010",
        "NickName": "唐友华",
        "AttrStatus": 102439,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "yvh"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@431cc2bf89381d96243b7b1ab9cecffa",
        "NickName": "ལིང་ལས།",
        "AttrStatus": 98343,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-梁蕾-Benny",
        "KeyWord": "lty"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@1d06136c47ee521f79fe86ce72d63c43739bd989ac44221020576ee6d27cd3ec",
        "NickName": "詹前力 LIVEN iOS",
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
        "UserName": "@8c12942c87aca396f9eefacdd9aac38b",
        "NickName": "mobius",
        "AttrStatus": 102783,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-秦宗健-ajian ",
        "KeyWord": "zig"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c05900d2c4aaf8009025927506ee0a9f",
        "NickName": "唐云龙 iOS",
        "AttrStatus": 229631,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-唐云龙",
        "KeyWord": "tyl"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@0df8947959d964098217e9eda1a8cabb",
        "NickName": "张群",
        "AttrStatus": 200871,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-张群Luke",
        "KeyWord": "Zha"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@d760fcaf6844446e25b2c7dd93bd0fc2",
        "NickName": "曾俊杰Android",
        "AttrStatus": 233575,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-曾俊杰Jim",
        "KeyWord": "gzw"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@6ba69de53054c8d3e971499a816c8c5dfbd7a7422d26a3155dd9d484b37349cc",
        "NickName": "罗成夫 STMA",
        "AttrStatus": 102589,
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
        "UserName": "@fc87951fcb01d6625501566766628db9",
        "NickName": "张帆 安卓",
        "AttrStatus": 245245,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-张帆Fan",
        "KeyWord": "fav"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@ad3390fd173978d853c4444f9908d71d413f46e8bb57a3c58303d6d67e14244d",
        "NickName": "孙科",
        "AttrStatus": 104831,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-孙科 Ken",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@98aea44debe7a2c722cffba87085dc2e29d50173e34ff31e4c5bda441f39382c",
        "NickName": "潘志壮",
        "AttrStatus": 104485,
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
        "UserName": "@47d57db5d976fd52a965052020e66cca8f7be5e628061a2cd72b211c55ec7806",
        "NickName": "Tcat许郁",
        "AttrStatus": 17011645,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-许郁Tcat",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b97ae29c66661d3fb8b99f13900a19cfecc355beafef5e0f6bb4d0ddaf878529",
        "NickName": "黄明",
        "AttrStatus": 17006629,
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
        "UserName": "@1bd712991b7de1999bf8651c84d528b5b5f4febb23f2ac7f10da480f525ffc94",
        "NickName": "何建生Jason",
        "AttrStatus": 102501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-何建生-Jason",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b4d978bf1cf861ba88f1ab5e61c147b3",
        "NickName": "郑智敏 android",
        "AttrStatus": 17006951,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "jea"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@ba1a1d5e5942b0e56050dfec6449c8c3",
        "NickName": "雷宁",
        "AttrStatus": 99327,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "lei"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@f2284d10d1a8f6002c643bec8efdc48d3778b9fa98591493c5ea2655d063458b",
        "NickName": "Sophia",
        "AttrStatus": 235877,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安Sophia",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@9abcf84f68deaa65d0514fb2e13faa119f5f1fe9876bc46c98d6f086a6ef89d3",
        "NickName": "杨太鹏 iOS",
        "AttrStatus": 235559,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-杨太鹏",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@110ee0645da0b27f8f6fd77969a92cf817abfa7b88c453313d9bcef3a163a6f6",
        "NickName": "梁思羽Kevin",
        "AttrStatus": 4285,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州–梁思羽",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c2a0b6bd40a2d86530a5db7950f5a8a4",
        "NickName": "樊华 GBA",
        "AttrStatus": 233573,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-Leon 樊华",
        "KeyWord": "LUC"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@a9c03d7981ac6407d0df2c6615f7e55a",
        "NickName": "jan",
        "AttrStatus": 99175,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-冼静Jane",
        "KeyWord": "XJD"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@6166e69afe036ffacd6a1dc6c0d866e9",
        "NickName": "。。。",
        "AttrStatus": 102527,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "ce7"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@4bf36a47c84fcf8cc45fdf3565d44a22784953a94184b768cb21100343e199b0",
        "NickName": "刘远明 iOS",
        "AttrStatus": 107775,
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
        "UserName": "@a6022f5cc37cc8faea586ba206a7cc43ce54dbb7b85842719f399aa96a6204af",
        "NickName": "CarinaMX",
        "AttrStatus": 233573,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安－候梦璇Carina",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@be4dd0943eb5aa47161eef0779f1ec02ceb1ebbc4157890667f50ec6a47638bc",
        "NickName": "🌙",
        "AttrStatus": 50563391,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-王千里Charlie",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@1b664030fd8ef02f4ad7218396e806d1",
        "NickName": "Tim Wei",
        "AttrStatus": 100479,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "wei"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@fad05e45778a9712060a3a15c26e8b64",
        "NickName": "涛",
        "AttrStatus": 102439,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-王涛Tommy",
        "KeyWord": "wan"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c6a12eb946145805356fd6fc193643a9edca24f7ae5c5f70943bb8d279e08d08",
        "NickName": "七夜",
        "AttrStatus": 103229,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-汪宇明Walter",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@fbb712b8dfeb9702f2b49e4232eb90f2d615e86a071e30d5346a7248f8aa97e7",
        "NickName": "yrh",
        "AttrStatus": 135357,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-杨荣翰-John",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b0cd93b8829fbad7724c49ba63a1dc293c6a2afac98faf402e308b7eb1bc0880",
        "NickName": "娟",
        "AttrStatus": 4428389,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-贺娟–Anna",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@a5fe46d510f50b57bd560e33b072306e6656e25fe0fddad235f3ece05392f180",
        "NickName": "Der Tod IST Frei.",
        "AttrStatus": 4197,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "Kidd 王文豪",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@0552c1811dbccc36fa2d405e0ffab641",
        "NickName": "Major",
        "AttrStatus": 230503,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-沈伟Major",
        "KeyWord": "sw9"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@8732a207a04dab52fabfa6fea1237baa39016afa6a08a3258ea6bc0a0f5530c7",
        "NickName": "Rong",
        "AttrStatus": 33656869,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-冯利荣-Frank",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@f0b56119a5a5106f8d1988bc3d642c5a71af40eef058a84f45658937b068b1ec",
        "NickName": "咕噜咕噜",
        "AttrStatus": 16912485,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "李旭昭 David",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c544bcc30cbdddb05f5ee1b30532562ed072f65de1eb409645685895ca317087",
        "NickName": "刘志文",
        "AttrStatus": 104677,
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
        "UserName": "@7c2805fe4e9bb84acd1a6c08e0afd66e865fa1e48e4f59816a10bb19177b0161",
        "NickName": "听话的尾巴",
        "AttrStatus": 233701,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-周金欢-Catherine",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5b03929870f7035b0ef13794698b914d0aff4432443f058c668b7834f2067a5a",
        "NickName": "Eve",
        "AttrStatus": 230245,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安- 李敏茹Daisy",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@79c4e42a528d1af2cdf3a0d0a934e9cf1ea0bf73618b9ea90ce13c1df9a5b704",
        "NickName": "Grant.W",
        "AttrStatus": 235645,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "che"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@735a7d1667d6d9dbda8a318ab8e2e5663d9f91fe65eb9eaba6d88a28fad6899c",
        "NickName": "壳",
        "AttrStatus": 236925,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-宋佳Polly",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b8866a64c982acd6b9aea6bf6eaf8753b9f6f712b00b96da28a5d9847b27e11e",
        "NickName": "Nick",
        "AttrStatus": 202047,
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
        "UserName": "@a3e540169887188453bd2b2ab557c4af9d5f85b9a083541f521fc9ac6fd56278",
        "NickName": "onload",
        "AttrStatus": 17011045,
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
        "UserName": "@a92f5f21c03e3b9f4eb910e66c282b57e4be1f710313b25191580933e2319b1a",
        "NickName": "傻瓜不是瓜",
        "AttrStatus": 16880061,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-张梦娈nobita",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@ab56782e6fdbd04fb9239ce8fe48318a58867cf917143914b6207755c5d49a41",
        "NickName": "加菲",
        "AttrStatus": 4197,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-孙豪-Abel",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@097aae7418c17bd6212e8e17e04150a946d57d5a54ddb5e4f8e35befea1f2e6a",
        "NickName": "HUI",
        "AttrStatus": 103527,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "zha"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@df9f5797f486cf4ca7aa9f49065c9724376c5f0efd3333b61f9a0ea203d6cf97",
        "NickName": "小林",
        "AttrStatus": 102501,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-PDI",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@88b117eb968bd9f009399f6d81f7898378abb4b826d6b5170b863d66854921be",
        "NickName": "朱光远",
        "AttrStatus": 102437,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-朱光远 Adder",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@fd9c0590622c2bdb7c81d720bb7ae35b709a0f994fcb3c43b893def45c8cb735",
        "NickName": "安静  ͣ ͩ ͣه٥",
        "AttrStatus": 16882045,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-赵佩云-Ada",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@a0f8135e275f76d8a4d3df8969d751a0b3de97d8f3dab219e67a6b217d22f733",
        "NickName": "🇨🇳",
        "AttrStatus": 102693,
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
        "UserName": "@50b976ac1283d8ec15a9f84e5b0aff94f59813edf6313ae48d4bab2e3ce9e979",
        "NickName": "Ferris",
        "AttrStatus": 233853,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安 - 范炳林 Ferris",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@ac8d0007659762f9bf6f95ce11a3bf29",
        "NickName": "SugarLei",
        "AttrStatus": 237669,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-雷宁-Phil",
        "KeyWord": "ytg"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@5a69b76304f1dd0c9e04b5db42d02c42",
        "NickName": "🇷yan",
        "AttrStatus": 4199,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-段晓涛-Ryan",
        "KeyWord": "dua"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@58c383f6dfa6021dd427269da1ee964f1d53243f5e08c114b11bd795544fbf63",
        "NickName": "Abby陈",
        "AttrStatus": 6245,
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
        "UserName": "@2bac5eb340e4577e03bb3a2cc6403fb0",
        "NickName": "Henry",
        "AttrStatus": 111229,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-常浩晨-Henry",
        "KeyWord": "o88"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c1888be337d676172ce222f248c19d19edb3eb0516347d74092eca92512be8c0",
        "NickName": "谢小黑🌱",
        "AttrStatus": 229565,
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
        "UserName": "@29fa924b2f5fcc53eafa1f4e3efb033e0a4fad90e0b6d60fab37958a7d5c6333",
        "NickName": "怎么老是你",
        "AttrStatus": 103781,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-王向前- Owen",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@b3a875de7831924b32f9d3ab50a73aa666156517980ad4ffaa463703c3e3822f",
        "NickName": "Demon Around",
        "AttrStatus": 67182695,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-Easton",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@1131c7f4c9e2925cc566da19af0238d379caa300634d838f047bdad425682a97",
        "NickName": "到账金额:  180 000.00",
        "AttrStatus": 200805,
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
        "UserName": "@49e83bdd6e4badfa10e68c166326c05967f706449e8bc4b4e7218a8a14cc5439",
        "NickName": "Robert",
        "AttrStatus": 104485,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-牛少帅Robert",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@c115667f5278d914ddd385d023a1b4a598bdb61e84a10e745b0fe74db9b59aa2",
        "NickName": "滑膛",
        "AttrStatus": 98749,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-杨冯-Jerry",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@effcf68034cf196ef8cb85f5319ed843",
        "NickName": "陈雨",
        "AttrStatus": 33655329,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安 陈雨Christian",
        "KeyWord": "che"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@99c9a6280aa35ef1dd0f51fd4fdecff9",
        "NickName": "Samuel",
        "AttrStatus": 104551,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-宇文巍-Samuel",
        "KeyWord": "yuw"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@111866e91946289b443bbf4cff38d75a90ac06c1fb0c1daf4e88308c9d209e2f",
        "NickName": "桔.🤎",
        "AttrStatus": 229735,
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
        "UserName": "@2c1b171d7c9bfff3e3f39f04dea185b8b87806e715001e1b3d08713d4c258f96",
        "NickName": "bye",
        "AttrStatus": 118845,
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
        "UserName": "@9e2da1fb7fb0913a6f1dc5d5df612bc5",
        "NickName": "Olivia Xu",
        "AttrStatus": 33787943,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "yue"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@30b9711db3832f7f2d48eefffb27295b",
        "NickName": "董先生",
        "AttrStatus": 231719,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-董斐-Bill",
        "KeyWord": "df8"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@691c01105d6249cd0affcb8a941f12288c920e299661bb4876a3e97a0e530e3a",
        "NickName": "blued.",
        "AttrStatus": 33682789,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-毛媛媛Blue",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@e2ebd41e0a1c91f2c4a900d038472b657944253759caf72374d4fe64080991dc",
        "NickName": "less is more",
        "AttrStatus": 71741,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-郑雪-Natalie",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@ff3985980ea1ec8ad709618bd34287cc2410882d01f684c4e83f2ed16c6a0eb3",
        "NickName": "Bean",
        "AttrStatus": 102437,
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
        "UserName": "@abde3cae810231fa42a7d1835039518d",
        "NickName": "🚁YOA",
        "AttrStatus": 117887,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "yuy"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@9aebbf7856bcaec338d9e92f37c733c67e868f159b98eb7c663e9f5f0728a7b7",
        "NickName": "Anna",
        "AttrStatus": 102973,
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
        "UserName": "@33599447e86cff335c27761190561a832e8d800697f12cfdb920793435e1f636",
        "NickName": "skychange",
        "AttrStatus": 135205,
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
        "UserName": "@35c0d0d65bad3d5a71ae18e2f5cf68409e47d82f27333bfeece7cb789968066e",
        "NickName": "華",
        "AttrStatus": 50565221,
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
        "UserName": "@a2e32d05156d68cb604fa8fa2be193c57f5551bda142fb40d111783ead8b69e9",
        "NickName": "零零发  Heley",
        "AttrStatus": 16781413,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安 +梁欢欢+Heley",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@03698a907a563f116ca44a4a52b550cb",
        "NickName": "乐",
        "AttrStatus": 112743,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-张嘉璐Jonny",
        "KeyWord": "le5"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@936afdd0567d9a7a69ab8029559e9e27f19c7aff8fec92fa8ae5b0761b2806d2",
        "NickName": "snow",
        "AttrStatus": 235877,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "Tiffany-张雅娟",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@2bc59a2bd5953e49be70eb246c2de38d5030f9c75b67598f82c693093427c66e",
        "NickName": "阳光拉菲〈lofy〉",
        "AttrStatus": 235621,
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
        "UserName": "@25fd4df684d4aaff9fb9d96e2c7e3d5c41d8abb5171d86d7a202a42340c3c36c",
        "NickName": "HAKUNA MATATA",
        "AttrStatus": 102437,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "西安-段豪 William",
        "KeyWord": ""
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@0d4c05f2f73283bfcfb8722a70e7eb035bc32f8d30dfc01ee89eddf462c7ef55",
        "NickName": "Camille",
        "AttrStatus": 102693,
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
        "UserName": "@f1bbe04745465d5d70326b26e8bd7882",
        "NickName": "邓毅 Android",
        "AttrStatus": 33656935,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-David",
        "KeyWord": "den"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@263127d40362665ba55c35ee3743b353",
        "NickName": "江^桀",
        "AttrStatus": 102439,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-江永杰Arno",
        "KeyWord": "jie"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@0a404b17eae3c98c007cacc37a324dc6",
        "NickName": "李经",
        "AttrStatus": 4135,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "广州-李经",
        "KeyWord": "luc"
    },
    {
        "MemberList": [],
        "Uin": 0,
        "UserName": "@a8e049fa8fc087d85f29bff8cae9b07e780f2a140a53edcfb8812d39cf63e3e4",
        "NickName": "张明华",
        "AttrStatus": 100391,
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "MemberStatus": 0,
        "DisplayName": "",
        "KeyWord": "zha"
    }
]

    toggle = WeChatFeatureToggle.instance()

    def test_analysis(self):
        analysis = self.toggle.analysis

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
        common = self.toggle.group.common
        self.assertEqual(common.expectedList, ["摸铃校友群", "骑洗衣机去地铁站", "【兄弟姐妹】", "Jade", "测试群",
                                               "Our Group", "网银业务交付部伙伴分群"])
        self.assertTrue("摸铃校友群" in common.expectedList)
        self.assertTrue("骑洗衣机去地铁站" in common.expectedList)
        self.assertTrue("【兄弟姐妹】" in common.expectedList)
        self.assertTrue("Jade" in common.expectedList)
        self.assertTrue("测试群" in common.expectedList)
        self.assertTrue("Our Group" in common.expectedList)
        self.assertFalse("琶洲中软群" in common.expectedList)
        self.assertFalse("网银交付部大群" in common.expectedList)
        self.assertTrue(common.queue)
        self.assertFalse(common.imageReturn)
        self.assertTrue(common.mapAnalysis)
        self.assertTrue(common.envelope)
        self.assertFalse(common.autoReply)
        self.assertTrue(common.atMeReply)

    def test_wechatTestGroupFeatureToggle(self):
        test = self.toggle.group.test
        self.assertEqual(test.expectedList, [])
        self.assertTrue(test.queue)
        self.assertTrue(test.imageReturn)
        self.assertTrue(test.mapAnalysis)
        self.assertTrue(test.envelope)
        self.assertFalse(test.autoReply)
        self.assertTrue(test.atMeReply)

    def test_wechatTestOurGroupFeatureToggle(self):
        ourGroup = self.toggle.group.ourGroup
        self.assertEqual(ourGroup.expectedList, ["曾超龙", "罗文轩", "伍楚婷", "徐鹏", "林俊杰", "曹伟江", "张广洋", "严其龙", "朱雄伟",
					"钟灵", "樊华", "叶志扬", "秦宗健", "梁斌文", "李锦宇", "李彬特", "戴国明", "黄文斌", "程珺",
					"梁思羽", "陈洋平", "何志伟", "叶庭强", "刘远明", "刘嘉奇", "冼静", "谢毅滦", "文逸俊", "刘洪威",
					"彭伟涛", "刘旭斌", "唐小兵", "余翼", "黄艳", "陈家乐", "梁敏瑜", "郑永祥", "唐友华", "覃淇韩", "凌俊杰",
					"方颖欢", "曾慶龍", "蔡日雄", "孙健强", "郑绵毅", "王伟达", "黄波", "江克非", "龚定显", "于顺燊",
					"徐治安", "胡嘉敏", "罗兴惠", "马仲豪", "曾昊", "卢平清", "王权斌", "谢祎龙", "詹前力", "刘建军", "杨元生",
					"高海梅", "郭明健", "杨成业", "李易承", "叶颖欣", "阮焯城", "丁小双", "曾俊杰", "黄少强", "陈奕",
					"黄江胜", "张冲", "周梓帆", "林聪", "蔡淑珍", "赖霄", "周楠"])
        self.assertTrue(len(ourGroup.expectedList) == 78)
        self.assertFalse(ourGroup.queue)
        self.assertFalse(ourGroup.imageReturn)
        self.assertFalse(ourGroup.mapAnalysis)
        self.assertFalse(ourGroup.envelope)
        self.assertFalse(ourGroup.autoReply)
        self.assertFalse(ourGroup.atMeReply)

    def test_weChatDHRFeatureToggle(self):
        dhrGroup = self.toggle.group.dhr

        self.assertEqual(dhrGroup.expectedList, ["李凯", "宋甜甜", "王志超", "蔡耀", "屈欢", "许月英", "王磊", "谢研", "裴明明",
                                                 "魏建华", "贾瑾", "刘晶", "候梦璇", "徐苗淼", "胡丹", "郭著", "穆斌斌",
                                                 "王雅如", "李涛", "胡超", "李敏茹", "宋佳", "校婷", "赵佩云", "王志军",
                                                 "周金欢", "杨冯", "夏睦平", "张小慧", "朱贝贝", "强曦", "李向东", "辛月",
                                                 "冯利荣", "康莎", "林俊杰", "郑智敏", "曹伟江", "张广洋", "张雅娟", "严其龙",
                                                 "樊华", "秦宗健", "梁斌文", "戴权祥", "李国僖", "张惠锋", "吴承炽", "李宏超",
                                                 "雷克龙", "明理", "李彬特", "陆聪聪", "戴国明", "张文康", "刘昌旭", "王涛",
                                                 "黄文斌", "李经", "沈伟", "卢旭龙", "杨德勇", "程珺", "梁思羽", "肖豫", "唐云龙",
                                                 "张晋", "胡启文", "张帆", "贺娟", "李银平", "杨太鹏", "陈飞", "雷宁", "陈洋平",
                                                 "张群", "慕云飞", "张明华", "陈少轩", "林健卜", "韦骏", "罗志林", "何志伟",
                                                 "杨荣翰", "刘远明", "南鑫林", "钟伟强", "冼静", "谢毅滦", "韩啸", "文逸俊",
                                                 "刘旭斌", "唐小兵", "古靓丽", "李超", "梁敏瑜", "王晨光", "雷宁", "郑永祥",
                                                 "谢晨", "郭争荣", "郑雪", "田兆伦", "常浩晨", "高龙彬", "毛媛媛", "董斐",
                                                 "宇文巍", "胡隆飞", "唐友华", "谢奎", "吴光耀", "王向前", "李航", "朱少沛",
                                                 "袁美军", "范炳林", "徐雪勇", "朱正毅", "段豪", "宋娜娜", "石学慧", "何鹏飞",
                                                 "张仪凡", "余云儒", "曾庆龙", "蔡日雄", "何建生", "刘亮亮", "孙健强", "孙科",
                                                 "刘静雯", "郑绵毅", "邓毅", "谷少刚", "潘志壮", "江克非", "于顺燊", "梁蕾",
                                                 "曾昊", "张远鸿", "黄明", "刘臻华", "段晓涛", "许郁", "陆琼", "王千里",
                                                 "梁欢欢", "何文杰", "张嘉璐", "沙洛沣", "王权斌", "汪宇明", "张逸飞", "詹前力",
                                                 "刘建军", "杨元生", "郭明健", "叶颖欣", "丁小双", "曾俊杰", "江永杰", "黄少强",
                                                 "刘兴红", "林聪", "黄江胜", "陈奕", "邱高颖", "陈丽君", "李旭昭", "孙豪",
                                                 "刘志文", "陈钰宏", "刘国辉", "朱光远", "罗成夫", "曾庆聪", "廖成龙", "张天龙",
                                                 "陈雨", "黎文杭", "张梦娈", "陈穗辉", "王文豪", "乔上飞", "牛少帅", "郑嘉豪",
                                                 "李浩生", "林延", "赵锡祯", "刘锐", "赵毅"])

        self.assertTrue(len(dhrGroup.expectedList) == 192)
        self.assertFalse(dhrGroup.queue)
        self.assertFalse(dhrGroup.imageReturn)
        self.assertFalse(dhrGroup.mapAnalysis)
        self.assertFalse(dhrGroup.envelope)
        self.assertFalse(dhrGroup.autoReply)
        self.assertFalse(dhrGroup.atMeReply)

    def test_weChatJadeFeatureToggle(self):
        jade = self.toggle.group.jade
        self.assertEqual(jade.expectedList, ["林俊杰", "张广洋", "谢毅滦", "陈洋平", "戴国明", "唐小兵", "刘旭斌", "何志伟",
                                             "杨元生", "文逸俊", "黄文斌", "李彬特", "郑永祥", "梁敏瑜", "曾昊",
                                             "于顺燊", "凌俊杰", "江克非", "郑绵毅", "蔡淑珍", "林聪", "叶颖欣", "廖成龙"]
                         , "expect list should be equal")
        self.assertTrue(len(jade.expectedList) == len(self.jade_chat_room_member) - 3)
        self.assertTrue(jade.queue)
        self.assertFalse(jade.imageReturn)
        self.assertTrue(jade.mapAnalysis)
        self.assertTrue(jade.envelope)
        self.assertFalse(jade.autoReply)
        self.assertFalse(jade.atMeReply)

    def test_weChatWasherFeatureToggle(self):
        washer = self.toggle.group.washer
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
        bns = self.toggle.group.brotherAndSister
        self.assertEqual(bns.expectedList, [], "expect list should be equal")
        self.assertFalse(bns.queue)
        self.assertFalse(bns.imageReturn)
        self.assertTrue(bns.mapAnalysis)
        self.assertTrue(bns.envelope)
        self.assertFalse(bns.autoReply)
        self.assertTrue(bns.atMeReply)

    def test_weChatCommonPersonalFeatureToggle(self):
        common = self.toggle.personal.common
        self.assertTrue(common.imageReturn)
        self.assertTrue(common.mapAnalysis)
        self.assertFalse(common.envelope)
        self.assertFalse(common.autoReply)

    def test_weChatJJFeatureToggle(self):
        jj = self.toggle.personal.jj
        self.assertFalse(jj.imageReturn)
        self.assertTrue(jj.mapAnalysis)
        self.assertTrue(jj.envelope)
        self.assertFalse(jj.autoReply)

    def test_dhrGroupReminder(self):
        dhr_members = self.toggle.group.dhrGroup.expectedList
        # print(dhr_members)
        msg = """
                    #接龙
        汇丰调查问卷完成统计

        1. 林俊杰 Jackie
        """
        result = WeChatAction.auto_reminder(self.dhr_group_chat_room_member, dhr_members, msg)
        print(result)
        
    def test_ourGroupReminder(self):
        group_members = self.toggle.group.ourGroup.expectedList
        msg = """
            #接龙
汇丰调查问卷完成统计

1. 林俊杰 Jackie
2. 周楠 Victoria
3. 赖霄-Sean
4. 黄波-Boris
5. 马仲豪 Mark
6. 黄少强-seanhuang
7. 刘建军-Thnaos
8. 杨成业－Curry
9. Ternence张广洋
10. 于顺燊-Justin
11. 罗兴惠 Kris
12. 覃淇韩
13. 郭明健 Joy
14. 刘洪威JackCode
15. 陈奕Yee
16. 谢祎龙jack
17. 郑永祥Michael
18. 高海梅 Hamy
19. 蔡日雄Symbol
20. 戴国明-Ming
21. Sheldon 谢毅滦
22. 何志伟Daniel
23. 阮焯城 Sans
24. 秦宗健 Ajian
25. 孙健强-Joey
26. 王伟达-Avater
27. 丁小双 Rosh
28. Kevin 梁思羽
29. 曹伟江-KNOX
30. 严其龙 Wave
31. 詹前力 LIVEN
32. 冼静 Jane
33. 彭伟涛-Stefan
34. 唐友华-tom
35. 樊华Leon
36. Kolor 陈家乐
37. 梁斌文Draven
38. Jason- 凌俊杰
39. 王权斌-Sam
40. 黄江胜 Jason
41. 杨元生_Yeson
42. 方颖欢 Huan
43. 刘旭斌Daniel
44. 曾慶龍max
45. 叶颖欣june
46. 周梓帆-Jerry
47. Kyle 程珺
48. 曾超龙_Sheldon
49. 罗文轩 Hins W X Luo
50. 曾俊杰 Jim
51. 唐小兵 Leo
52. 常志杰Sandy
53. 林聪 Lynn
54. 蔡淑珍 Kathy
55. 曾昊Anson
56. Alison_黄艳
57. 李锦宇
        """
        result = WeChatAction.auto_reminder(self.our_group_chat_room_member, group_members, msg, 60)

        reminder = """ 汇丰调查问卷完成统计 
@伍楚婷＋Phoenix 
@刘远明 Nicky 
@李彬特 winter 
@陈洋平—Carl 
@黄文斌-Harvey 
@文逸俊 Caesar 
@朱雄伟 Edwin 
@Frank 钟灵 
@Kyle 余翼 
@刘嘉奇Kid 
@叶庭强-jack 
@zion 徐治安 
@郑绵毅-Manny 
@江克非 Leslie 
@徐鹏_Westbrook 
@胡嘉敏-gami 
@龚定显captain 
@Driven-卢平清 
@Cloud李易承 
@张冲_Mack 
@Lanmon梁敏瑜 

未接龙人数还剩 21 人"""

        self.assertEqual(result, reminder)

        result = WeChatAction.auto_reminder(self.our_group_chat_room_member, group_members, msg, 20)
        self.assertEqual(result, None)

        result = WeChatAction.auto_reminder(self.our_group_chat_room_member,
                                            group_members,
                                            msg,
                                            remind_num=30,
                                            is_frequency_reduce=True,
                                            frequency=4)
        self.assertEqual(result, None)

        msg += "\n@伍楚婷＋Phoenix "
        reminder = """ 汇丰调查问卷完成统计 
@刘远明 Nicky 
@李彬特 winter 
@陈洋平—Carl 
@黄文斌-Harvey 
@文逸俊 Caesar 
@朱雄伟 Edwin 
@Frank 钟灵 
@Kyle 余翼 
@刘嘉奇Kid 
@叶庭强-jack 
@zion 徐治安 
@郑绵毅-Manny 
@江克非 Leslie 
@徐鹏_Westbrook 
@胡嘉敏-gami 
@龚定显captain 
@Driven-卢平清 
@Cloud李易承 
@张冲_Mack 
@Lanmon梁敏瑜 

未接龙人数还剩 20 人"""

        result = WeChatAction.auto_reminder(self.our_group_chat_room_member,
                                            group_members,
                                            msg,
                                            remind_num=30,
                                            is_frequency_reduce=True,
                                            frequency=4)
        self.assertEqual(result, reminder)

    def test_weChatJadeReminderLessThanTen(self):
        jade_members = self.toggle.group.jade.expectedList
        new_msg = """
                    #接龙
                    氛围调查
                    
                    1. 林俊杰 - Jackie
                    2. 郑绵毅-Manny
                    3. 唐小兵 Leo
                    4. 叶颖欣
                    5. 凌俊杰-Jason
                    6. 张广洋-Ternence
                    7. 林聪  Lynn
                    8. 曾昊 Anson
                    9. 戴国明-MING
                    10. 刘旭斌Daniel
                    11. 杨元生-Yeson
                    12. 廖成龙-Jacky
                    13. 李彬特 winter
                    14. 文逸俊 - Caesar
                    15. 黄文斌_Harvey
                    16. 于顺燊-Justin
                    17. Lanmon梁敏瑜
                    18. 何志伟Daniel
                    """
        reminder = """ 氛围调查 
@陈洋平-Carl 
@谢毅滦–Sheldon 
@郑永祥-Michael 
@江克非-Leslie 
@蔡淑珍 Kathy PMO 

未接龙人数还剩 5 人"""

        result = WeChatAction.auto_reminder(self.jade_chat_room_member, jade_members, new_msg)
        self.assertEqual(result, reminder)

    def test_weChatJadeReminderMoreThanTen(self):
        jade_members = self.toggle.group.jade.expectedList
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
        jade_members = self.toggle.group.jade.expectedList
        msg = """
            #接龙
            氛围调查
            
            1. 林俊杰 - Jackie
            2. 郑绵毅-Manny
            3. 唐小兵 Leo
            4. 叶颖欣
            5. 凌俊杰-Jason
            6. 张广洋-Ternence
            7. 林聪  Lynn
            8. 曾昊 Anson
            9. 戴国明-MING
            10. 刘旭斌Daniel
            11. 杨元生-Yeson
            12. 廖成龙-Jacky
            13. 李彬特 winter
            14. 文逸俊 - Caesar
            15. 黄文斌_Harvey
            16. 于顺燊-Justin
            17. Lanmon梁敏瑜
            18. 何志伟Daniel
            19. 蔡淑珍
            20. 郑永祥-Michael
            21. 陈洋平-Carl
            22. 谢毅滦–Sheldon
            23. 江克非-Leslie
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
        jade_members = self.toggle.group.jade.expectedList
        print("expectedList: ", jade_members)
        msg = """
#接龙
7月工时确认完成接龙

1. 林俊杰 - Jackie
2. 曾昊 Anson
3. 于顺燊-Justin
4. 刘旭斌Daniel
5. 戴国明-MING
6. 何志伟Daniel
7. 唐小兵 Leo
8. 黄文斌_Harvey
9. 杨元生-Yeson
10. 林聪  Lynn
11. 廖成龙-Jacky
12. 凌俊杰-Jason
13. 谢毅滦–Sheldon
14. 陈洋平-Carl
15. 张广洋-Ternence
16. 李彬特 winter
17. 郑永祥-Michael
18. 郑绵毅-Manny
                """

        result = WeChatAction.auto_reminder(self.jade_chat_room_member, jade_members, msg)
        print(result)

    def test_weChatActionAvailableTime(self):
        begin = "00:00"
        end = "23:59"
        result = WeChatAction.is_available_time(begin, end)
        self.assertTrue(result)

    def test_weChatActionUnavailableTime(self):
        begin = "00:00"
        end = "00:01"
        result = WeChatAction.is_available_time(begin, end)
        self.assertFalse(result)

    def test_our_group(self):
        begin = datetime.strptime(str(datetime.now().date()) + "10:45", "%Y-%m-%d%H:%M")
        end = datetime.strptime(str(datetime.now().date()) + "11:00", "%Y-%m-%d%H:%M")
        print(begin)
        print(end)

        now = datetime.now()
        print(now)

        print(now >= begin and now <= end)
