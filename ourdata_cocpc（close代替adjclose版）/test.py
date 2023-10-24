import pickle

path  = r'CoCPC/data/stock_datasets/test_stock_50_batchs.pkl'

df = pickle.load(open(path, 'rb'))

# print(len(df[0]))  50个batch，每个32样本

# print(df[0])    4 features, labels, raw_adj_close_price_feat, data_dict['ts']

# print(len(df[0][3]))   20*32

print(len(df[0][0][0][0]))  

# print(df[0][0][0])   32 第一天的feature？




