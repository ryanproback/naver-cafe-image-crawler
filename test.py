from selenium import webdriver
from cic import scrap, download_image

# --------------------- Test Case ------------------------

# 이미지의 원본 주소를 스크랩하는 테스트
# The Test Scraping original urls of images
def case_scrap():
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://cafe.naver.com/joonggonara/556661313'
    my_list = scrap(driver, url)
    print(my_list)


# 이미지의 원본 주소를 스크랩하여 특정 폴더에 다운로드하는 테스트
# Scraping original urls of images and Using these to download image to specific directory
def case_scrap_and_download():
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://cafe.naver.com/joonggonara/556661313'
    my_list = scrap(driver, url)
    print(my_list)
    for my_url in my_list:
        download_image(my_url, 'testdir/')
        
        
if __name__ == "__main__":
    case_scrap_and_download()        
