import bs4
import requests

html = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')
#주소의 html 파일이 저장된다.

soup = bs4.BeautifulSoup(html.text,'html.parser')
#html text를 내가 보기 좋게 접근할 수 있도록 변경

dollar = soup.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')
#css selecor로 내가 원하는 태그를 가져옴

print(dollar.text)