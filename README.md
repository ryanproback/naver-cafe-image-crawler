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

## Dependencies
- python 3.6
- selenium
- bs4
- urllib
