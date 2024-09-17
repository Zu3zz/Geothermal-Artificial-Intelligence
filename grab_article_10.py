from scholarly import scholarly
import pandas as pd


def get_article(n):
    search_query = scholarly.search_pubs('geothermal artificial intelligence')

    # 存储结果
    results = []

    # 获取前700条结果
    for i in range(n):
        try:
            article = next(search_query)
            # 提取所需信息
            title = article.get('bib', {}).get('title', 'N/A')
            year = article.get('bib', {}).get('pub_year', 'N/A')
            abstract = article.get('bib', {}).get('abstract', 'N/A')
            journal = article.get('bib', {}).get('venue', 'N/A')
            authors = article.get('bib', {}).get('author', 'N/A')

            # 添加到结果列表
            results.append({
                'title': title,
                'year': year,
                'abstract': abstract,
                'journal': journal,
                'authors': authors
            })
        except StopIteration:
            break
    return results


if __name__ == '__main__':
    # 存储结果
    article_size = 700
    results = get_article(article_size)

    # 将结果转换为DataFrame
    df = pd.DataFrame(results)

    # 保存为CSV文件
    df.to_csv('scholar_results_{}.csv'.format(article_size), index=False)

    print("Results saved to scholar_results.csv")
