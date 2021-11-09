from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        self.file = open(path, 'r')
        self.wList = list()
        for line in self.file:
            if len(line.strip()) != 0 and not line.startswith('#'):
                self.wList.append(line.strip())   
        print(f"{len(self.wList)} words read")