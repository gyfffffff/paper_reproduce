import pandas as pd
import os
weight = pd.read_csv(r'D:\baiduyundownload\Data\Basic\tushare_index_weight_hs300_20230706081700.csv')
# print(weight)

mean = weight.groupby('con_code')['weight'].mean().to_frame()
# print(mean.columns)
topstocks = pd.DataFrame.sort_values(mean,by=['weight'], ascending=False).iloc[:50,:]

# topstocks.to_csv('./stocklist.csv')

for stock in topstocks.index:
    filename = stock+'.csv'
    path = r'D:\baiduyundownload\Data\Daily\2010-01-01,2023-07-05'
    print(os.path.join(path, ))
