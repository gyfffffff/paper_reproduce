import pandas as pd
import pickle
invalidstock = pickle.load(open('data/invalidstock.pkl', 'rb'))
df = pd.read_csv('tushare_stock_basic_20230705180446.csv', usecols=["ts_code", "name"])
# print(df)
for i, info in df.iterrows():
    if info['ts_code'] in invalidstock:
        df = df.drop(index=i)
df.to_csv('stock_list.csv', index=False)
print(len(invalidstock))
print(5227-df.shape[0])