import json
import re
import requests


class CryptoCurrencyData:
    def __init__(self, currency: str = "bitcoin", proxies: dict = {}, headers: dict = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}):
        self.headers = headers
        self.proxies = proxies
        pattern = '<script id="__NEXT_DATA__" type="application/json">(.+?)</script>'
        BASE_URL = "https://coinmarketcap.com/ja/currencies/{0}/".format(currency)
        html = requests.get(url=BASE_URL, headers=self.headers, proxies=self.proxies).text
        self.data = json.loads(re.findall(pattern, html)[0])

    def getRate(self, scale: str = "1D"):
        cryptoId = self.data["props"]["initialProps"]["pageProps"]["info"]["id"]
        convertId = 2797
        BASE_URL = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart?range={0}&id={1}&convertId={2}".format(scale,cryptoId,convertId)
        return requests.get(url=BASE_URL, headers=self.headers, proxies=self.proxies).json()

    def getRatePrediction(self, scale: str = "half-year"):
        cryptoId = self.data["props"]["initialProps"]["pageProps"]["info"]["id"]
        BASE_URL = "https://api.coinmarketcap.com/data-api/v3/price-prediction/query/{0}?cryptoId={1}".format(scale,cryptoId)
        return requests.get(url=BASE_URL, headers=self.headers, proxies=self.proxies).json()