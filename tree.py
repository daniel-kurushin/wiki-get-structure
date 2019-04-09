from nltk.tokenize import WordPunctTokenizer
wpt = WordPunctTokenizer()

PUNKT = list(".,:;-")


class Tree(dict):
    def update(self, adict):
        for akey in adict.keys():
            a = self.__wrap(akey[0])
            b = self.__wrap(akey[1])
            super().update({(a,b):adict[akey]})
    
    def __join(self, tokens = ['очень', 'длинная', 'строка', ',', 'с', 'пробелами', ',', 'и', 'знаками', 'препинания']):
        rez = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token in PUNKT:
                rez[-1] += token
            else:
                rez += [token]
            return rez

    def __wrap(self, _str = "очень длинная строка,с пробелами, и знаками препинания"):
        _len = 0
        rez = ""
        for token in self.__join(wpt.tokenize(_str)):
            _len += len(token)
            rez += " " + token
            if _len > 20:
                rez += "\n"
                _len = 0
        return rez.strip()


if __name__ == '__main__':
    atree = Tree()
    atree.update({('a','g'):'b'})
    print(atree)
    atree.update({('a','g'):'очень длинная строка,с пробелами, и знаками препинания'})
    print(atree)
    