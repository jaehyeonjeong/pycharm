from currency_converter import CurrencyConverter

cc = CurrencyConverter("http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip") #최신 환율 정보로 업데이트 합니다.
print(cc.convert(1, 'USD', 'KRW')) #1달러를 대한민국 원화로 변경할 때 금액을 출력합니다.