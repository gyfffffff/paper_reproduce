# coding = utf-8
def clearBlankLine():
    file1 = open('data/corpus_raw.txt', 'r', encoding='utf-8')  # 要去掉空行的文件
    file2 = open('data/corpus.txt', 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()

