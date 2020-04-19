from pyecharts.charts import Bar, Pie, Map, WordCloud
from pyecharts.options import InitOpts, TitleOpts, ToolboxOpts, VisualMapOpts
from pyecharts.render import make_snapshot

# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
from PIL import Image
import wordcloud
import numpy as np
import jieba
import re

import os
import shutil

class Analytics:

    @classmethod
    def wechat_friends_analysis(cls, friends):
        # print(itchat.get_friends()[1])

        provinces, province_count, cities, city_count = [], [], [], []

        tuple_city_list = cls.wechat_information_refine("City", friends, 3, True)
        tuple_province_list = cls.wechat_information_refine("Province", friends, 4, True)

        sex_title = ["未知", "男", "女"]
        remark_sex_count = [0, 0, 0]
        no_remark_sex_count = [0, 0, 0]

        for friend in friends:
            sex = friend["Sex"]
            if len(friend["RemarkName"]):
                remark_sex_count[sex] += 1
            else:
                no_remark_sex_count[sex] += 1

        for i, j in tuple_province_list:
            if not len(i):
                i = "未知"
            provinces.append(i)
            province_count.append(j)

        for i, j in tuple_city_list:
            if not len(i):
                i = "未知"
            cities.append(i)
            city_count.append(j)

        # print(cities, city_count)
        # print(provinces, province_count)

        page_title = "好友性别数据统计"
        bar_sex = Bar(init_opts=InitOpts(page_title=page_title))
        bar_sex.add_xaxis(sex_title)
        bar_sex.add_yaxis("有备注", remark_sex_count)
        bar_sex.add_yaxis("无备注", no_remark_sex_count)
        bar_sex.set_global_opts(title_opts=TitleOpts(title="微信好友性别数据统计", pos_left=60))
        bar_sex.render("sex.html")

        bar_city = Bar()
        bar_city.add_xaxis(cities)
        bar_city.add_yaxis("微信好友地区数据统计", city_count)
        bar_city.set_global_opts(toolbox_opts=ToolboxOpts(is_show=True))
        bar_city.render("city.html")

        bar_province = (
            Bar()
                .add_xaxis(provinces)
                .add_yaxis("微信好友省份统计", province_count)
                .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True))
        )
        make_snapshot(snapshot, bar_province.render("bar_province.html"), "bar_province.png")

        city_data_list = [(i, j) for i, j in zip(cities, city_count)]
        pie_city = (
            Pie(init_opts=InitOpts(
                page_title="微信好友城市分析",
                width="1400px",
                height="800px",
            ))
                .add(
                data_pair=city_data_list,
                series_name="微信好友分布",
                # radius=["25%", "75%"],
                # rosetype="radius"
            )
                .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True, pos_top="50px"),
                                 title_opts=TitleOpts(title="微信好友城市分析", pos_top="80px", pos_left="10px"))
            # .render("pie_city.html")
        )
        make_snapshot(snapshot, pie_city.render("pie_city.html"), "pie_city.png")

        province_data_list = [(i, j) for i, j in zip(provinces, province_count)]
        pie_province = (
            Pie(init_opts=InitOpts(
                page_title="微信好友省份分析",
                width="1200px",
                height="800px",
            ))
                .add(
                data_pair=province_data_list,
                series_name="微信好友分布",
                radius=["25%", "75%"],
                rosetype="Mapping"
            )
                .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True, pos_top="60px"),
                                 title_opts=TitleOpts(title="微信好友省份分析", pos_top="60px", pos_left="50px"))
            # .render("pie_province.html")
        )
        make_snapshot(snapshot, pie_province.render("pie_province.html"), "pie_province.png")

        province_geo = (
            Map(init_opts=InitOpts(page_title="微信好友分布"))
                .add("微信好友分布geo图", tuple_province_list, "china")
                .set_global_opts(
                title_opts=TitleOpts(title="微信好友分布分布", pos_left="30px"),
                visualmap_opts=VisualMapOpts(max_=200, is_piecewise=True))
            # .render("geo_province.html")
        )
        make_snapshot(snapshot, province_geo.render("geo_province.html"), "geo_province.png")

    @classmethod
    def wechat_information_refine(cls, key, friends, filter_count, reverse) -> []:
        information, count = [], []

        for friend in friends:
            info = friend[key]

            if info not in information:
                information.append(info)
                count.append(0)

        info_length = len(count)

        for friend in friends:
            for i in range(info_length):
                if friend[key] == information[i]:
                    count[i] += 1

        temp_list = [(i, j) for i, j in zip(information, count) if j >= filter_count]
        temp_list.sort(key=lambda x: x[1], reverse=reverse)

        # print(temp_list)
        return temp_list


    @classmethod
    def wechat_signature_words(cls, friends):
        all_word_list = []
        final_words = {}
        for friend in friends:
            words = jieba.cut(friend["Signature"])
            for w in list(words):
                res = re.match(r"([\u4e00-\u9fa5]+)", w)
                if res:
                    all_word_list.append(w)

        # print(all_word_list)

        for w in all_word_list:
            if w not in final_words.keys():
                final_words[w] = 0

            final_words[w] += 1

        sort_words = sorted(final_words.items(), key=lambda x: x[1], reverse=True)
        print(words)

        chart_wc = (
            WordCloud(init_opts=InitOpts(page_title="微信签名词云"))
                .add("签名词云", sort_words, word_size_range=[20, 100], shape="triangle")
                .set_global_opts(title_opts=TitleOpts(title="微信签名词云", pos_left="140px"),
                                 toolbox_opts=ToolboxOpts(is_show=True))
            # .render("signature.html")
        )
        make_snapshot(snapshot, chart_wc.render("signature.html"), "signature.png")

        img = Image.open("IMG_7946.JPG")
        mask = np.array(img)
        wc = wordcloud.WordCloud(font_path="simsun.ttc",
                                 background_color="white",
                                 # stopwords=wordcloud.STOPWORDS.add("的"),
                                 stopwords={"自己", "一个", "的"},
                                 # max_words=100,
                                 mask=mask)
        wc.generate(" ".join(all_word_list))
        wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
        wc.to_file("word_cloud.png")
        print("============================= Wchat signature words success =============================")


    @classmethod
    def file_classify(cls, file_type, des_path):

        file_list = []
        for file in os.listdir():
            suffix = file.split(".")[-1]
            if suffix == file_type:
                file_list.append(file)

        if not os.path.exists(des_path):
            os.mkdir(des_path)
            print("create dir success")
        else:
            cur_path = os.path.join(os.getcwd(), des_path)
            # print(cur_path)
            os.chdir(cur_path)
            for f in file_list:
                if os.path.exists(f):
                    os.remove(f)

        # print("file list: %s" % file_list)
        os.chdir(os.path.pardir)
        for f in file_list:
            shutil.move(f, des_path)