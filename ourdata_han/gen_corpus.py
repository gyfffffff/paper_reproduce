import pandas as pd
df = pd.read_csv('News_Abs_19-22.csv')
with open('corpus.txt', 'w', encoding='UTF-8') as f:
    for i, line in df.iterrows():
        if '每日交易公开信息' in line[1] or line[2] == ' ':
            continue
        # print(line)
        f.writelines(line[2])
        f.write('\n')
    # f.write('\n')
