# -*- coding: utf-8 -*-
#python2
from  collections  import Counter
import codecs
# 打开文件，读取内容，并把词存于一个list里
loadFile = codecs.open("happiness_seg.txt","r",encoding='utf-8')
wordList = loadFile.read().split(" ")
# 生成一个计数的字典
c = Counter()
# 把满足条件的二元词组放入计数字典中，并计数
for i in range(0,(len(wordList) - 1)) :
    if len(wordList[i]) >= 2 and len(wordList[i + 1]) >= 2:
        double_words = wordList[i] + wordList[i + 1]
        c[double_words] = c[double_words] + 1

most_words = c.most_common(10)
for i in range(len(most_words)):
    print most_words[i][0],most_words[i][1]
