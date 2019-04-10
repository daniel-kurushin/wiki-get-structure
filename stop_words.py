#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:03:05 2019

@author: dan
"""

test_text = """Эксимер переворачивает лептон в полном соответствии с законом 
сохранения энергии. Плазменное образование зеркально сжимает изобарический 
объект одинаково по всем направлениям. Кристалл масштабирует межядерный 
резонатор.

Плазменное образование, даже при наличии сильных аттракторов, отражает взрыв. 
Многочисленные расчеты предсказывают, а эксперименты подтверждают, что силовое 
поле отрицательно заряжено. Колебание, при адиабатическом изменении параметров, 
излучает гамма-квант. Примесь искажает экситон. Осциллятор, в отличие от 
классического случая, отклоняет солитон. Линза излучает коллапсирующий взрыв.

Бозе-конденсат последовательно возбуждает экранированный резонатор только в 
отсутствие тепло- и массообмена с окружающей средой. Фронт, на первый взгляд, 
вертикально ускоряет экситон вне зависимости от предсказаний самосогласованной 
теоретической модели явления. Фонон трансформирует газ. В ряде недавних 
экспериментов плазменное образование усиливает торсионный лептон, 
тем самым открывая возможность цепочки квантовых превращений.
"""
# respect https://www.artlebedev.ru/yandex/site/saved/stopword.html
stop_words = """а   большой	бы
быть	в	весь
вот	все	всей
вы	говорить	год
да	для	до
еще	же	знать
и	из	к
как	который	мочь
мы	на	наш
не	него	нее
нет	них	но
о	один	она
они	оно	оный
от	ото	по
с	свой	себя
сказать	см  та	такой
только	тот	ты те тех
у	что	это  эта эти этим этих
этот	я"""

set_stop_words = set(stop_words.split())

def is_stop_word(word = 'где'):
    return word.lower() in set_stop_words

if __name__ == '__main__':
    for word in test_text.split():
        print(word, is_stop_word(word))
    