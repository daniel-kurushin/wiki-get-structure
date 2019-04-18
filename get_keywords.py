#!/usr/bin/python3

test = """
Подынтегральное выражение, в первом приближении, изменяет 
кинетический момент. Начальное условие движения, исключая 
очевидный случай, недоказуемо. Регулярная прецессия, согласно 
уравнениям Лагранжа, изящно транслирует апериодический 
систематический уход, что обусловлено малыми углами карданового 
подвеса.

Учитывая, что (sin x)’ = cos x, вращение представляет собой 
нормальный гирогоризонт. Однако исследование задачи в более 
строгой постановке показывает, что интеграл Гамильтона 
стационарно специфицирует угол крена. Частота методически 
заставляет иначе взглянуть на то, что такое вектор.

Математическая статистика интегрирует дифференциальный маховик. 
Функция B(x,y) позволяет исключить из рассмотрения интеграл от 
функции, имеющий конечный разрыв, в итоге приходим к логическому 
противоречию. Линейное программирование, несмотря на внешние 
воздействия, усиливает многомерный подвижный объект, откуда 
следует доказываемое равенство. Неконсервативная сила перманентно 
связывает полином. Дисперсия различна. 1/r²
"""

from rutermextract import TermExtractor
from pymorphy2 import MorphAnalyzer
from movingavg import Moving

mo = MorphAnalyzer()
te = TermExtractor()

AVGLEN = 8

FILTR = set([
    'Abbr', 'Fixd', 'Geox', 'Name', 'Surn', 'NUMB',
    'англ', 'википедия', 'гео', 'фам',
    'такая статья', 'такая страница',
    'такие название', 'быстрое старт', 'статья', 'руководство',
])

def get_keywords(text = ""):
    terms = te(text)
    try:
        max_count = terms[0].count
        for term in terms:
            if term.count >= max_count / 10:
                yield term.normalized 

    except IndexError as e:
        pass
    
def filter_keywords(keywords = ["россия", "бердяев", "информатика"], filter = FILTR):
    global AVGLEN
    
    for keyword in keywords:
        params = []
        
        ma = Moving()
        for a in mo.parse(keyword):
            kwl = len(keyword)
            if a.tag.grammemes != {'LATN'} and kwl > AVGLEN / 3:
                params += list(a.tag.grammemes)
            ma.update(kwl)
        
        print(keyword, AVGLEN)
        AVGLEN = float(ma)
        
        if not filter & set(params + [keyword]) and not len(keyword) < 3:
            yield keyword.replace('/', '_')
        else:
#            import sys
#            print(keyword, params, file = sys.stderr)
            pass

if __name__ == '__main__':
	print(list(filter_keywords(get_keywords(test))))
#	print(filter_keywords())
