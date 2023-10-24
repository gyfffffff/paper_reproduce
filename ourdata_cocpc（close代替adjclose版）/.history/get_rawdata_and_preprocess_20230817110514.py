import pandas as pd
import os
from sklearn.preprocessing import normalize
from datetime import datetime



raw_data_path = r'./data/kdd17_like/price_long_50/'
preprocess_data_path = r'./data/kdd17_like/preprocess/'

def preprocess(file):
    with open(os.path.join(raw_data_path, file), 'r') as f:
        data = pd.read_csv(f)
        date_time = data['Date']

        open_price = normalize(data['Open'].to_numpy().reshape(1, -1))
        high_price = normalize(data['High'].to_numpy().reshape(1, -1))
        low_price = normalize(data['Low'].to_numpy().reshape(1, -1))
        close_price = normalize(data['Close'].to_numpy().reshape(1, -1))
    # print('shifted mv:', data['Adj Close'].shift(-1)[:3])

        # 修改2
        mv_percent = ((data['Close'] - data['Close'].shift(-1)
                        ) / data['Close'].shift(-1))[:-1].to_numpy()
        volume = data['Volume'].to_numpy().reshape(1, -1)

        # print('len date time:', len(date_time))
        # print(date_time[0])
        filename = file.split('.')[0] + '.txt'
        with open(os.path.join(preprocess_data_path, filename), 'a+') as wf:
            for i in range(len(date_time)-1):  #
                transform_data = []
                if '/' in date_time[i]:
                    revised_date = datetime.strptime(
                        date_time[i], '%m/%d/%Y').date().strftime('%Y-%m-%d')
                else:
                    revised_date = date_time[i]
                transform_data.append(revised_date)
                # print(mv_percent[i])

                # transform_data = transform_data.join('\t')
                transform_data.append(str(round(mv_percent[i], 6)))
                transform_data.append(str(round(open_price[0, i], 6)))
                transform_data.append(str(round(high_price[0, i], 6)))
                transform_data.append(str(round(low_price[0, i], 6)))
                transform_data.append(str(round(close_price[0, i], 6)))
                # 修改3
                transform_data.append(str(int(volume[0, i])))

                wf.write('\t'.join(transform_data))
                wf.write('\n')


topstocks = pd.read_csv('topstocks_orderby_avg_volume.csv')
count = 0
for i in range(200):
    filename = topstocks['stock'][i].split('.')
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
    validdata.to_csv('.\\data\\kdd17_like\\price_long_50\\'+filename, index=False)
    try:
        preprocess(filename)
        count+=1
        if(count == 50):
            break
    except:
        os.remove('.\\data\\kdd17_like\\price_long_50\\'+filename)
        pass
