# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def parse_cdp_neighbors(command_output):
    dic={}
    dev=command_output[:command_output.find('>')]
    table=command_output[command_output.find("Port ID")+8:].rstrip().split('\n')
    for row in table:
        lir=row.split()
        #dic=lir[-2]+lir[-1]
        dic[tuple([dev, lir[1]+lir[2]])]=tuple([lir[0], lir[-2]+lir[-1]])
    return dic



with open("C:/WEB/2-grade/ready-exercises/11_modules/sh_cdp_n_sw1.txt", 'r') as f:
    comm=f.read()

print(parse_cdp_neighbors(comm))