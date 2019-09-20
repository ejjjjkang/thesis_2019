import os
from io import open
import torch
from konlpy.tag import Okt  #한국어말뭉치

PATH = ''

class Dictionary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = []

    def add_word(self, word):
        if word not in self.word2idx:
            self.idx2word.append(word)
            self.word2idx[word] = len(self.idx2word) - 1
        return self.word2idx[word]

    def __len__(self):
        return len(self.idx2word)

class Corpus(object):
    def __init__(self):
        self.dictionary = Dictionary()

    def Tokenize(self):
        """tokenize text file"""
        n = 0
        result = []
        assert os.path.exists(PATH)
        with open(PATH, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                n = n+1
                if not line:break
                temp = []
                for word in tokenlist:
                    if word[1] in ["Noun"]:  # 명사일 때만
                        temp.append((word[0]))  # 해당 단어를 저장함

                if temp:  # 만약 이번에 읽은 데이터에 명사가 존재할 경우에만
                    result.append(temp)  # 결과에 저장
            f.close()

