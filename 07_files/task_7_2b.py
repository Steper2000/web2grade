# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

print('-'*50)

with open('C:/WEB/2-grade/ready-exercises/07_files/config_sw1.txt', 'r') as f, open('C:/WEB/2-grade/ready-exercises/07_files/config_sw1_cleared.txt', 'w') as dest:
    for line in f:
        i=0
        while i < len(ignore):
            if ignore[i] in line:
                break
            i+=1
        else:
           dest.write(line)