'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-01 18:53:10
LastEditors: Data Designer
LastEditTime: 2020-12-01 18:57:53
'''
import numpy as np
import pandas as pd
import jieba.analyse
from pyecharts import options as opts
from pyecharts.globals import SymbolType
from pyecharts.charts import Pie, Bar, Map, WordCloud

# 商品excel文件保存路径
GOODS_EXCEL_PATH = r'vscode/test/test.xlsx'
# 读取标准数据
DF_STANDARD = pd.read_excel(GOODS_EXCEL_PATH)

def analysis_title():
    """
    词云分析商品标题
    :return:
    """
    # 引入全局数据
    global DF_STANDARD
    # 1、词数统计
    keywords_count_list = jieba.analyse.textrank(' '.join(DF_STANDARD.title), topK=10, withWeight=True)
    print(keywords_count_list)
    # 生成词云
    word_cloud = (
        WordCloud()
            .add("", keywords_count_list, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="手机性能词云TOP10"))
    )
    word_cloud.render('title-word-cloud.html')

if __name__ == '__main__':
    # 数据分析
    analysis_title()