# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv

filein=argv[1]
fileout=argv[2]

ignore = ['duplex', 'alias', 'Current configuration']

print('-'*50)
f="C:/WEB/2-grade/ready-exercises/07_files/{}"
with open(filein, 'r') as f, open(fileout, 'w') as dest:
    for line in f:
        i=0
        while i < len(ignore):
            if ignore[i] in line:
                break
            i+=1
        else:
           dest.write(line)

print("file was updated")