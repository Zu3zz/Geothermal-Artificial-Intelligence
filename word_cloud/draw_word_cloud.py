import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 读取CSV文件
    df = pd.read_csv('../../../github/Geothermal-Artificial-Intelligence/data/scholar_results_573.csv')

    # 提取abstract内容
    text = ' '.join(df['abstract'].dropna())

    # 定义要去掉的词
    custom_stopwords = set(STOPWORDS)
    # custom_stopwords.update(['artificial','intelligence', 'geothermal','indicators','AI','big','using','based','forward','intelligent','study','depends'])
    custom_stopwords.update(
        ['geothermal', 'AI', 'big', 'using', 'based', 'forward', 'intelligent', 'study', 'depends', 'machine',
         'learning', 'system', 'energy', 'artificial', 'intelligence','systems','model','field','method'])

    # 生成词云
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=250,
                          stopwords=custom_stopwords).generate(text)

    # 显示词云
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('articles_cloud_abstract_customize_250.png')
    plt.show()
