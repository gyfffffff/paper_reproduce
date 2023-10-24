import pandas as pd
import jieba

stopwords_path = r'data/News/raw/_temp_stopwords.txt'
original_data_path = r'data/News/raw/news.csv'
save_texts_raw_path = r'data/News/raw/_temp_corpus_raw.txt'
# save_wordlist_path = r'data/IndustryPolicy/raw/_temp_wordlist.txt'
save_cutted_corpus_path = r'glove/cutted_corpus.txt'

def save_raw_texts2txt(path, save_path):
    news_df = pd.read_csv(path)
    # ===========
    corpus_raw = news_df[['InfoTitle', 'Content']]
    # ===========
    with open(save_path, 'w', encoding='utf-8') as f:
        for _, line in corpus_raw.iterrows():
            try:
               f.write(''.join(line))
            except:
                pass

def load_stop_words():
    with open(stopwords_path, "r", encoding="utf-8") as f:
        return f.read().split("\n")

def cut_words():
    stop_words = load_stop_words()
    with open(save_texts_raw_path, encoding='utf8') as f:
        allData = f.readlines()
    result = []
    for words in allData:
        c_words = jieba.lcut(words.strip())
        if c_words == []:
            continue
        result.append([word for word in c_words if word not in stop_words])
    return result

def save_wordlist(path):
    wordList = []
    data = cut_words()
    with open(path, 'w', encoding='utf-8') as f:
        for words in data:
            for word in words:
                if word not in wordList:
                    wordList.append(word)
                    f.write(word+' ')
            f.write('\n')
    return wordList

def gen_cutted_corpus(path):
    data = cut_words()
    with open(path, 'w', encoding='utf-8') as f:
        for words in data:
            for word in words:
                f.write(word+' ')
            f.write('\n')
save_raw_texts2txt(original_data_path, save_texts_raw_path)
gen_cutted_corpus(save_cutted_corpus_path)