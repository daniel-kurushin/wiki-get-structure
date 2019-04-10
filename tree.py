from nltk.tokenize import WordPunctTokenizer
wpt = WordPunctTokenizer()

PUNKT = list(".,:;-")


class Tree(dict):
    def update(self, adict):
        for akey in adict.keys():
            a = self.__wrap(akey[0])
            b = self.__wrap(akey[1])
            super().update({(a,b):adict[akey]})
    
    def __wrap(self, _str = "очень длинная строка,с пробелами, и знаками препинания"):
        _len = 0
        rez = ""
        for token in wpt.tokenize(_str):
            _len += len(token)
            try:
                if token not in PUNKT: 
                    rez += " "
            except IndexError:
                pass
            rez += token
            if _len > 20:
                rez += "\n"
                _len = 0
        return rez.strip()


if __name__ == '__main__':
    atree = Tree()
    atree.update({('прикладная, лингвистика','научный стиль'): 1})
    print(atree)
    atree.update({('прикладная лингвистика','научный стиль'): 2})
    print(atree)
    