# -*- coding: cp1251 -*-
# иморт модуля pdb для отладки
import pdb

# создание пустого словаря для хранения вопросов
questions = {}

# задаем переменную mail с адресом
mail = 'ADRESS'

# задаем переменную text с текстом вопроса
text = 'QUEST'

# добавление в словарь questions пару ключ-значение (mail: text)
questions[mail] = text

# установка точки останова для отладки
pdb.set_trace()
