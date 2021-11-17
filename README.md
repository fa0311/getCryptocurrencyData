# getCryptocurrencyData

仮想通貨の詳細とレートを取得するライブラリ<br>

# import

```python
from getCryptoCurrencyData import CryptoCurrencyData
```

# use

```python
CryptoCurrencyData("bitcoin", proxies = {}, headers = {}).data
CryptoCurrencyData("ethereum").getRate("1D")
CryptoCurrencyData("ethereum").getRatePrediction()
```

# License

getCryptoCurrencyData is under MIT License
