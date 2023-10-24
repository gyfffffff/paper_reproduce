import pandas as pd
topstocks = pd.read_csv('topstocks_orderby_avg_volume.csv')

for stock in topstocks['stock']:
    print(stock)
