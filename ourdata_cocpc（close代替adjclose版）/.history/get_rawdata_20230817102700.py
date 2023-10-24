import pandas as pd
import os
topstocks = pd.read_csv('topstocks_orderby_avg_volume.csv')

# print(topstocks['stock'])
for i in range(200):
    filename = topstocks['stock'][i]
    path = r'D:\baiduyundownload\Data\Daily\2010-01-01,2023-07-05'
    filepath = os.path.join(path, filename)
    data = pd.read_csv(filepath)
    data["DATES"] = pd.to_datetime(data["DATES"])
    s_date = pd.to_datetime('2014-01-01')
    e_date = pd.to_datetime('2023-01-01')
    validdata = data[['DATES',
                      'SeqOpenPrice',
                      'SeqHighPrice',
                      'SeqLowPrice',
                      'SeqClosePrice',
                      'SeqTurnoverVolume']][(data["DATES"]>=s_date) & (data['DATES']<e_date)]
    validdata.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    validdata.index = range(1,len(validdata)+1)
    try:
        
    validdata.to_csv('.\\data\\kdd17_like\\price_long_50\\'+filename, index=False)
