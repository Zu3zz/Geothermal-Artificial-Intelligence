# -*- coding: utf-8 -*-

"""
@author: tronzheng
@file: count_country.py
@time: 2024/9/11 11:19
@desc: 
"""

import spacy
import pandas as pd
from collections import Counter

if __name__ == '__main__':

    # 加载spacy的预训练模型
    nlp = spacy.load('en_core_web_sm')

    # 读取CSV文件
    df = pd.read_csv('../../../github/Geothermal-Artificial-Intelligence/data/scholar_results_700.csv')

    # 提取title列
    titles = df['abstract'].dropna()

    # 初始化计数器
    country_count = Counter()

    # 遍历每个标题，使用spacy识别国家名称
    for title in titles:
        doc = nlp(title)
        for ent in doc.ents:
            if ent.label_ == 'GPE':  # GPE (Geopolitical Entity) 包括国家
                country_count[ent.text] += 1

    # 打印结果
    print(country_count)
