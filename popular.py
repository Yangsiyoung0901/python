import requests
import bs4

html = requests.get('https://www.naver.com/')

soup = bs4.BeautifulSoup(html.text,'html.parser')

keywords = soup.select('span.ah_k')

real_keywords = keywords[0:20] #배열 0번째부터 n-1번째까지 가져와서 배열로 저장
real_real_keywords = [keyword.text for keyword in real_keywords]



print('아래의 보기 중에서 실검 1위를 맞춰보세요.')

problem = sorted(real_real_keywords) #1등이 무엇인지 모르게 가나다 순 정렬

print(problem)

your_answer = input('답을 입력하세요 : ')

if real_real_keywords[0]==your_answer :
    print('정답입니다.')
else :
    print('오답입니다.')