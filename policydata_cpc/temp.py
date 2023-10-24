import pandas as pd

# df = pd.read_csv('data/News/raw/LC_News.csv', parse_dates=['InfoPublDate'])
# print(df.head())
# df2 = df[(df['InfoPublDate']>='2018-12-03 00:00:00')&(df['InfoPublDate']<'2023-07-01 00:00:00')]
# df2.to_csv('data/News/raw/news.csv')
pd.read_csv('data/News/raw/news.csv', usecols=['InfoPublDate', "InfoTitle", "Content"]).to_csv('data/News/raw/news.csv')
