# naver-cafe-image-crawler
This is image crawler for Naver Cafe (네이버 카페 게시글 이미지 크롤러 입니다. )

## 사용법
### scrap
1. 네이버 카페 게시글 주소를 인수로 넘깁니다.
2. list로 묶인 게시글 내의 이미지 주소들이 반환됩니다.

### download_image
1. 원본 이미지 주소와 이미지가 저장될 폴더를 인수 넘깁니다.
#### scrap을 통해 반환받은 이미지들을 다운받을 경우
1. 반복문을 통해 한 주소 씩 함수를 호출 하도록 합니다.


## 사용 예
```python
from cic import scrap, download_image
from selenium import webdriver
import os


# 이미지의 원본 주소를 스크랩하여 특정 폴더에 다운로드하는 테스트
# Scraping original urls of images and Using these to download image to specific directory
def case_scrap_and_download():
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://cafe.naver.com/joonggonara/556661313'
    my_list = scrap(driver, url)
    print(my_list)
    if not os.path.exists('testdir'):
        os.mkdir('testdir')
    for my_url in my_list:
        download_image(my_url, 'testdir/')
    driver.close()


if __name__ == "__main__":
    case_scrap_and_download()
```

## Dependencies
- Windows
- python 3.6
- selenium
- bs4
- urllib
