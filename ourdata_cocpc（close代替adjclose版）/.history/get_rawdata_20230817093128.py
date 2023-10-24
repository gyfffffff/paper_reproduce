import pandas as pd
import os
# stocklist = os.listdir('D:\\baiduyundownload\\Data\Daily\\2010-01-01,2023-07-05\\')
# volumeconunt = {}
# for stock in stocklist:
#     data = pd.read_csv(r'D:\baiduyundownload\Data\Daily\2010-01-01,2023-07-05\\'+stock)
#     volumeconunt[stock] = data['SeqTurnoverVolume'].mean()
volumeconunt_df = pd.DataFrame({'000001.SZ.csv': 83031607.73231708, '000002.SZ.csv': 85833776.00121951,
                                '000004.SZ.csv': 2470245.7021341464}, index=acolumns=['stock', 'avg_volume'])
print(volumeconunt_df)
















# import pandas as pd
# import os
# import datetime
# weight = pd.read_csv(r'D:\baiduyundownload\Data\Basic\tushare_index_weight_hs300_20230706081700.csv')
# # print(weight)

# mean = weight.groupby('con_code')['weight'].mean().to_frame()
# # print(mean.columns)
# topstocks = pd.DataFrame.sort_values(mean,by=['weight'], ascending=False).iloc[:50,:]

# # topstocks.to_csv('./stocklist.csv')

# for stock in topstocks.index:
#     filename = stock+'.csv'
#     path = r'D:\baiduyundownload\Data\Daily\2010-01-01,2023-07-05'
#     filepath = os.path.join(path, filename)
#     data = pd.read_csv(filepath)
#     data["DATES"] = pd.to_datetime(data["DATES"])
#     s_date = pd.to_datetime('2014-01-01')
#     e_date = pd.to_datetime('2023-01-01')
#     validdata = data[['DATES',
#                       'SeqOpenPrice',
#                       'SeqHighPrice',
#                       'SeqLowPrice',
#                       'SeqClosePrice',
#                       'SeqTurnoverVolume']][(data["DATES"]>=s_date) & (data['DATES']<e_date)]
#     validdata.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
#     validdata.index = range(1,len(validdata)+1)
#     validdata.to_csv('.\\data\\kdd17_like\\price_long_50\\'+filename, index=False)


