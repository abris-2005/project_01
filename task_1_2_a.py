# -*- coding: utf-8 -*-
"""Nask_1_2_A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TwzM3f0jkWdCQqVCY6AcToqhaIKYns4m
"""

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
t1 = 0
for i in range(3):
 x = random.randint(0, len(my_favorite_songs)-1)
 t1 = t1 + my_favorite_songs[x] [1]
print('Три песни звучат', t1, 'минут')
