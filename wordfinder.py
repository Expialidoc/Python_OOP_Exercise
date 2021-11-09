"""Word Finder: finds random words from a dictionary.
The word must be from the dictionary

>>> l = WordFinder('words.txt')
>>> l.random() in 'words.txt'
True

# >>> from words.txt import self.wList[ind]
# >>> l.random() in path
# True
"""
import random

class WordFinder:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.wList = list()
        for line in self.file:
            self.wList.append(line.strip())
        print(f"{len(self.wList)} words read")
        self.file.close()

    def random(self):
        ind = random.randint(0,len(self.wList)-1)
        return self.wList[ind]
