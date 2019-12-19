import requests
import bs4

i=input('게임 명을 정확히 입력하세요. : ')
ins_game_name = i.split()
game_name=ins_game_name[0]
for i in range(1,len(ins_game_name)):
    game_name=game_name+'+'+ins_game_name[i]

html = requests.get('https://isthereanydeal.com/search/?q={}'.format(game_name))
#주소의 html 파일이 저장된다.

soup = bs4.BeautifulSoup(html.text,'html.parser')
#html text를 내가 보기 좋게 접근할 수 있도록 변경

game_cost = soup.select_one('#pageContainer > div:nth-child(2) > div > div.card__content > div:nth-child(3) > div > div > div.numtag__primary')
#css selecor로 내가 원하는 태그를 가져옴

discount_rate = soup.select_one('#pageContainer > div:nth-child(2) > div > div.card__content > div:nth-child(3) > div > div > div.numtag__second')
exac_game_name = soup.select_one('#pageContainer > div:nth-child(2) > div > div.card__content > div.card__head.card__row > a.card__title')

if discount_rate == None:
    discount_rate='0%'
    print(exac_game_name.text, game_cost.text , discount_rate)
else :
    print(exac_game_name.text, game_cost.text, discount_rate.text)