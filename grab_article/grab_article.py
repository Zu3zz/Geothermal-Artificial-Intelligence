from scholarly import scholarly


def get_article(n):
    search_query = scholarly.search_pubs('geothermal artificial intelligence')

    # 存储结果
    results = []

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
    results = get_article(700)

    # 打印结果
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Year: {result['year']}")
        print(f"Abstract: {result['abstract']}")
        print(f"Journal: {result['journal']}")
        print(f"Authors: {result['authors']}")
        print("\n" + "-" * 80 + "\n")
