#네이버 증시 페이지에 대신 접속을 해서,
#현재 코스피 지수를 가져오는 프로그램
import requests
import bs4

html = requests.get('https://finance.naver.com/sise/sise_index.nhn?code=KOSPI')
#주소의 html 파일이 저장된다.

soup = bs4.BeautifulSoup(html.text,'html.parser')
#html text를 내가 보기 좋게 접근할 수 있도록 변경

kospi = soup.select_one('#now_value')
#css selecor로 내가 원하는 태그를 가져옴

print(kospi.text)