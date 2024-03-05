# 웹 크롤링 (Crawling) : 브라우저 드라이버를 이용하여 실제로 각 페이지를 이동하며 '동적'으로 데이터를 수집하는 방법

# 웹 스크래핑 (Scraping) : 웹 페이지의 응답을 받아 데이터를 분석하여 필요한 데이터를 수집하는 방법

# 파이썬 스크래핑 패키지 : beautifulSoup4
# pip install beautifulSoup4
# 파이썬 크롤링 패키지 : selenium
# pip install selenium

# requests : 파이썬에서 가장 많이 사용되는 HTTP 라이브러리
# pip install requests
import requests
from bs4 import BeautifulSoup

URL = 'https://naver.com'

response = requests.get(URL)
print(response)
# https://developer.mozilla.org/ko/docs/Web/HTTP/Status -> HTTP 상태 코드 정보
# 100번대 추가 요청 기다림
# 200번대 성공
# 300번대 리소스 위치
# 400번대 요청자 클라이언트 오류
# 500번대 응답자 서버 오류

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else :
    print(response.status_code)