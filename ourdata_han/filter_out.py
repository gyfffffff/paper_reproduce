import pandas as pd
import jieba
stocks = pd.read_csv('stock_list.csv')
sc = stocks['ts_code'].loc[:]
sn = stocks['name'].loc[:]
stock_dict = {code:name for code, name in zip(sn,sc)}
df = pd.read_csv('News_Abs_19-22.csv')

# 加载停用词词表
stop_words = open('data/stopwords.txt', "r", encoding="utf-8").read().split("\n")

# 加载文本,切词
def cut_words(line2):
    c_words = jieba.lcut(line2)
    return [word for word in c_words if word not in stop_words]

'''
判断一条语句是否包含词库中的词
'''
def word_parameter(word_list):
    '''包含关系方法所需的词典'''
    word_set = set(word_list)
    num_list = [len(word) for word in word_set if len(word) > 0]  # 词库字数
    num_list = list(set(num_list))  # 词库字数去重[2,3,4]
    return word_set, num_list


def slice_len(s, n):
    '''截取字符串中固定长度的所有词'''
    result_list = []
    length = len(s)
    for i in range(0, length):
        if i < length-n+1:
            result_list.append(s[i:i+n])
    return result_list


def mycon(s, word_list):
    '''词库可能字数的词全部切分且与词库比较'''
    word_set, num_list = word_parameter(word_list)
    temp_list = []  # 所有切分词
    for num in num_list:
        temp_list.extend(slice_len(s, num))
    temp_list1 = list(set(temp_list) & word_set)  # 求交集
    return sorted(temp_list1, key=len, reverse=True)



import os
os.chdir('./data/tweet/preprocessed')

from tqdm import tqdm
for i, line in tqdm(df.iterrows()):
    date = line[0]
    if '每日交易公开信息' in line[1] or line[2] == ' ':
        continue
    tit_abst = line[1]+' '+line[2]
    contentstock = mycon(tit_abst, stock_dict.keys())
    if contentstock: # 如果含有股票名称
        for stock in contentstock:
            sc = stock_dict[stock]
            if not os.path.exists(sc):
                os.mkdir(sc)
            single_news_dict = {"text":cut_words(line[2]), "created_at":date}
            with open(os.path.join(sc, date), 'a+', encoding='UTF-8') as f1:
                f1.writelines(str(single_news_dict))
                f1.write('\n')
        os.chdir('../../')
        with open('corpus_raw.txt', 'a+', encoding='UTF-8') as f:
            f.writelines(line[2])
            f.write('\n')
        os.chdir('./tweet/preprocessed')





