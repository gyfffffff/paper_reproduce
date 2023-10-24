import pandas as pd
import os
topstocks = pd.read_csv('topstocks_orderby_avg_volume.csv')

# print(topstocks['stock'])
for i in range(len(topstocks['stock'])):
    stock = topstocks['stock'][i]
    path = r'D:\baiduyundownload\Data\Daily\2010-01-01,2023-07-05'
    filepath = os.path.join(path, filename)
