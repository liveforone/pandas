import pandas as pd
import requests

url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
df = pd.read_html(url, encoding='cp949')
print(df[0])