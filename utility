import re

article_id_reg = re.compile('articleid=(?P<articleid>[0-9]+)')
total_count_reg = re.compile('search.totalCount=(?P<totalcount>[0-9]+)')


def get_extension(string: str):
    ext = re.compile('(?P<ext>[.][a-z]{3,4})$')
    e = ext.search(string)
    return e.group('ext')


def get_article_id(url: str):
    m = article_id_reg.search(url)
    return m.group('articleid')


def get_total_count(url: str):
    m = total_count_reg.search(url)
    return m.group('totalcount')


def make_board_url_by_id(cafe_id: int, board_id: int):
    cafe_query_string = f'search.clubid={str(cafe_id)}'
    board_query_string = f'search.menuid={str(board_id)}'
    board_type_query_string = 'search.boardtype=L'  # 리스트 타입 게시판
    url = 'https://cafe.naver.com/ArticleList.nhn?' \
          + cafe_query_string + '&' \
          + board_query_string + '&' \
          + board_type_query_string

    return url


def make_article_url_by_id(cafe_id: int, article_id: int):
    cafe_query_string = f'search.clubid={str(cafe_id)}'
    board_query_string = f'search.articleid={str(article_id)}'
    url = 'https://cafe.naver.com/ArticleList.nhn?' \
          + cafe_query_string + '&' \
          + board_query_string

    return url
