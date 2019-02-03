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
# 이미지를 저장할 폴더의 주소 (끝에 반드시 /(슬래시)를 붙일 것)
# directory path to save image (You have to attach /(slash) to end)

def download_image(url: str, dir_path: str):
    file_name = extract_file_name(url)
    url = quote(url.encode('utf8'), '/:')
    request.urlretrieve(url, dir_path + file_name)

    
# 네이버 카페 게시글이 아닌 URL을 전달했을 경우 발생시킬 Exception
# The exception to raise when user transfer URL which is not naver-cafe-article.
class InvalidURLException(Exception):
    # 생성할때 value 값을 입력 받는다.
    def __init__(self, value):
        self.value = value

    # 생성할때 받은 value 값을 확인 한다.
    def __str__(self):
        return f'Message: May be, You inserted URL that is not cafe article ( Received URL: { self.value } )'
