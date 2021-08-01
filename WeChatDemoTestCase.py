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

    def test_weChatJadeFeatureToggle(self):
        toggle = WeChatFeatureToggle.instance()

        jade = toggle.group.jade
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

    def test_weChatCommonPersonalFeatureToggle(self):
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
        toggle = WeChatFeatureToggle.instance()
        jade_members = toggle.group.jade.expectedList
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
        toggle = WeChatFeatureToggle.instance()
        jade_members = toggle.group.jade.expectedList
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
        begin = datetime.strptime(str(datetime.now().date()) + '10:45', '%Y-%m-%d%H:%M')
        end = datetime.strptime(str(datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')
        print(begin)
        print(end)

        now = datetime.now()
        print(now)

        print(now >= begin and now <= end)
