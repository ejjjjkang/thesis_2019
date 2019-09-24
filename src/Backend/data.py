import os
from io import open
import torch

"""
불용어 제거할 것 
1. 숫자
2. 한글자

"""

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
    def __init__(self, path):
        self.dictionary = Dictionary()
        self.train = self.tokenize(os.path.join(path, 'train_conservative.txt'))
        self.valid = self.tokenize(os.path.join(path, 'valid_conservative.txt'))
        self.test = self.tokenize(os.path.join(path, 'test_conservative.txt'))


        # self.okt = Okt()

    def tokenize(self, path):
        """Tokenizes a text file."""
        assert os.path.exists(path)
        with open(path, encoding="utf8") as fred:
            for line in fred:
                words = line.split() + ['<eos>']
                for word in words:
                    self.dictionary.add_word(word)

        with open(path, encoding="utf8") as fred:
            idss = []
            for line in fred:
                words = line.split() + ['<eos>']
                ids = []
                for word in words:
                    ids.append(self.dictionary.word2idx[word])
                idss.append(torch.tensor(ids).type(torch.int64))
            ids = torch.cat(idss)
            return ids