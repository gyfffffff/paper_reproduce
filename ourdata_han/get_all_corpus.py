import pandas as pd
df = pd.read_csv('LC_NewsAbstract.csv', usecols=[
                 'InfoPublDate', 'InfoTitle', 'Abstract'])
df['InfoPublDate'] = pd.to_datetime(df['InfoPublDate'])
df = df.sort_values(by='InfoPublDate').reset_index(drop=True)
df1 = df[(df['InfoPublDate'] >='2019-01-01') & (df['InfoPublDate']<='2022-12-31')]
df1.to_csv('News_Abs_19-22.csv', index=False)
# print(df[(df['InfoPublDate'] == '2020-04-09') &
#          (df['InfoPublDate'] != '每日交易公开信息(2020-04-09)')])


