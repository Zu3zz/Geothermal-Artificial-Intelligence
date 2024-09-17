import pandas as pd
import matplotlib.pyplot as plt
if __name__ == '__main__':

    # 读取CSV文件
    df = pd.read_csv('../../../github/Geothermal-Artificial-Intelligence/data/scholar_results_573.csv')

    # 选取前573条数据
    df = df.head(573)

    # 去除年份小于2000的文章
    df = df[df['year'] >= 2000]

    # 统计每年的文章数量，去除2025年的数据
    year_counts = df[df['year'] != 2025]['year'].value_counts().sort_index()

    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(year_counts.index, year_counts.values, color='skyblue')

    # 添加柱顶标注
    for bar in bars:
        yval = bar.get_height()
        year = int(bar.get_x())
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{int(yval)}', va='bottom', ha='center')

    # 设置图表标题和标签
    plt.title('Number of Articles per Year',fontsize=16)
    plt.xlabel('Year',fontsize=14)
    plt.ylabel('Number of Articles',fontsize=14)

    # 设置每年的横坐标
    plt.xticks(year_counts.index, rotation=45)

    # 保存图片
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('articles_per_year.png')

    # 显示图表
    plt.show()