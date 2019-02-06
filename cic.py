# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urlparse
from urllib.parse import quote
import re
import os


# 게시글 내 이미지들의 원본 주소를 얻기 위한 정규 표현식
# Regular expression to get original path of images in article
reg = re.compile('fileurl="(?P<img>https://cafefiles.pstatic.net/[^ ]*[.][a-zA-Z]{3,4})"')


# scrap
# 게시글 내 이미지들의 원본 URL을 list로 묶어 반환합니다.
# This function return list of original url of image in article

# driver : webdriver
# 셀레니엄 드라이버입니다.
# This is Selenium driver

# url : str
# 게시글의 주소입니다.
# URL Address of cafe article
def scrap(driver: webdriver, url: str):
    images = list()

    driver.get(url)
    
    # 게시글 내의 이미지가 1개일 경우를 위한 코드
    # Code for case when number of images is only 1
    soup = BeautifulSoup(driver.page_source, 'lxml')
    img_tag = soup.select('#photoview')
    image = reg.search(str(img_tag))
    if bool(image):
        images.append(str(image.group('img')))
        return images
    
    try:
        driver.switch_to.frame("cafe_main")
    except NoSuchFrameException:
        raise InvalidURLException(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    lines = soup.select('#attachLayer > ul > script')

    for line in lines:
        m = reg.search(str(line))
        if bool(m):
            images.append(str(m.group('img')))

    return images


# scrap_by_id
# 게시글 내 이미지들의 원본 URL을 list로 묶어 반환합니다.
# This function return list of original url of image in article

# driver : webdriver
# 셀레니엄 드라이버입니다.
# This is Selenium driver

# cafe_id : int
# 카페의 아이디입니다.
# ID of cafe

# article_id : int
# 게시글의 아이디입니다.
# ID of article
def scrap_by_id(driver: webdriver, cafe_id: int, article_id: int):
    url = make_article_url_by_id(cafe_id, article_id)
    images = list()

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    img_tag = soup.select('#photoview')
    image = reg.search(str(img_tag))
    if bool(image):
        images.append(str(image.group('img')))
        return images

    try:
        driver.switch_to.frame("cafe_main")
    except NoSuchFrameException:
        raise InvalidURLException(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    lines = soup.select('#attachLayer > ul > script')

    for line in lines:
        m = reg.search(str(line))
        if bool(m):
            images.append(str(m.group('img')))

    return images


# extract_file_name
# URL로 부터 파일의 이름을 추출하기 위한 함수 입니다.
# The function to extract file name from url

# url : str
# 이미지가 위치하고 있는 URL 주소
# URL Address which image is located

def extract_file_name(url: str):
    parsed_url = urlparse(url)
    return os.path.basename(parsed_url.path)


# download_image
# URL을 이용하여 이미지를 저장하기 위한 함수 입니다.
# The function to save image using url

# url : str
# 이미지가 위치하고 있는 URL 주소
# URL Address which image is located

# dir_path : str
# 이미지를 저장할 폴더의 주소
# directory path to save image

def download_image(url: str, dir_path: str):
    file_name = extract_file_name(url)
    url = quote(url.encode('utf8'), '/:')
    try:
        request.urlretrieve(url, os.path.join(dir_path,file_name))
    except HTTPError:
        print('[e] Wrong Image URL. 이미지가 존재하지 않습니다.')

    
# 네이버 카페 게시글이 아닌 URL을 전달했을 경우 발생시킬 Exception
# The exception to raise when user transfer URL which is not naver-cafe-article.
class InvalidURLException(Exception):
    # 생성할때 value 값을 입력 받는다.
    def __init__(self, value):
        self.value = value

    # 생성할때 받은 value 값을 확인 한다.
    def __str__(self):
        return f'Message: May be, You inserted URL that is not cafe article ( Received URL: { self.value } )'
    
    
# 존재하지 않는 이미지 URL을 전달했을 경우 발생시킬 에러
# The error to raise when user transfer invalid image URL to function.
class NotFoundImage(Exception):
    def __init__(self, value):
        self.value = value

    # 생성할때 받은 value 값을 확인 한다.
    def __str__(self):
        return f'Message: Wrong Image URL. 이미지가 존재하지 않습니다. ( Received URL: { self.value } )'
