# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
print('-'*50)
with open('C:/WEB/2-grade/ready-exercises/07_files/config_sw1.txt', 'r') as f:
    for line in f:
        if line[0] != "!":
            print(line.rstrip('\n'))