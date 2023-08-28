import requests
from bs4 import BeautifulSoup

target1 = str(True)
target2 = str(True)

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}"
                            .format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span')
    print(containers.text) #접근정보만 나오지 환율정보는 나오지 않음
    #크롤링은 좀더 공부하고 다시 보는것으로 가자


get_exchange_rate('usd', 'krw')
