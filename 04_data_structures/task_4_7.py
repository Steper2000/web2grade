# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'
Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
lis=mac.split(':')
print(lis)
ce=[int(lis[0], 16),int(lis[1], 16), int(lis[2], 16) ]
print(ce)
bs=str(bin(ce[0]).lstrip('0b'))+str(bin(ce[1]).lstrip('0b'))+str(bin(ce[2]).lstrip('0b'))
print(bs)