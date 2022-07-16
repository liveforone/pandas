import pandas as pd
df = pd.read_excel("C:\\Users\KYC\Ai Study\series\data.xlsx")
df = df.set_index('date')  #date를 인덱스(기준)으로 하는것인데 내가 엑셀을 잘못해서 에러뜸
print(df)