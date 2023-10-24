import pandas as pd
topstocks = pd.read_csv('topstocks_orderby_avg_volume.csv')

# print(topstocks['stock'])
for i in range(len(topstocks['stock'])):
    stock = topstocks['stock'][i])
