# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
print('-'*50)

with open('C:/WEB/2-grade/ready-exercises/07_files/config_sw1.txt', 'r') as f:
    for line in f:
        i=0
        while i < len(ignore):
            if ignore[i] in line:
                break
            i+=1
        else:
            if line[0] != "!": 
                print(line.rstrip())
                
        
           