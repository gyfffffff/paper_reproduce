import pandas as pd
weight = pd.read_csv(r'D:\baiduyundownload\Data\Basic\tushare_index_weight_hs300_20230706081700.csv')
# print(weight)

mean = weight.groupby('con_code')['weight'].mean().to_frame()
# print(mean.columns)
topstock = pd.DataFrame.sort_values(mean,by=['weight'], ascending=False).iloc[:50,:]

topstock.


