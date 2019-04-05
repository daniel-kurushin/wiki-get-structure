from get_wiki_definition import get_wiki_definition
from hashlib import md5
from json import dump, load

try:
    hashes = load(open('database/hashes.dat'))
except FileNotFoundError:
    dump({},open('database/hashes.dat','w'),ensure_ascii=1,indent=2)
    hashes = {}
    
def __md5(_str):
    m = md5()
    m.update(_str.encode())
    return m.hexdigest()

def get_definition(definition = "Дерево"):
    try:
        rez = open("database/%s.dat" % definition).read()
    except FileNotFoundError:
        rez = get_wiki_definition(definition)
        _md5 = __md5(rez)
        if _md5 not in hashes.keys():
            open("database/%s.dat" % definition, 'w').write(rez)
            hashes.update({_md5:rez})
            dump(hashes,open('database/hashes.dat','w'),ensure_ascii=0,indent=2)
        else:
            pass
    return rez

if __name__ == '__main__':
    print(get_definition())

	# for word in ["Слово", "Дерево", "Растение"]:
	# 	print("\n", word, "\n\n", get_definition(word))

	# assert get_definition("Дерево") == DEREVO_DEFINITION
	# assert texts_are_alike(get_definition(), "Дерево - это жизненная форма\
	# 	деревянистых растений с единственной, отчётливо выраженной,\
	# 	многолетней, в разной степени одревесневшей, сохраняющейся\
	# 	в течение всей жизни, разветвлённой (кроме пальм) главной\
	# 	осью — стволом")