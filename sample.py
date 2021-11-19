from getCryptoCurrencyData import CryptoCurrencyData




print(CryptoCurrencyData("ethereum").getRate("1D"))


CryptoCurrencyData("bitcoin", proxies = {}, headers = {}).data
CryptoCurrencyData("ethereum", proxies = {
     "http":"http://example.com/proxy.pac",
     "https":"http://example.com/proxy.pac"

}).getRate("1D")
next(reversed(CryptoCurrencyData("ethereum").getRate("1D")["data"]["points"].values()), None)["c"][0]


# ["1D","7D","1M","3M","1Y","YTD","ALL"]