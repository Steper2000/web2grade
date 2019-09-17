# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
table=[]

with open("C:/WEB/2-grade/ready-exercises/07_files/CAM_table.txt", 'r') as f:
    for line in f:
        strl=line.split()
        if len(strl) == 4 and strl[0] != "----" and strl[0] != "Vlan":
            table.append(strl)


for i in range(len(table)-1):
    for j in range(len(table)-i-1):
        if int(table[j][0]) > int(table[j+1][0]):
            table[j], table[j+1] = table[j+1], table[j]

for elem in table:
    print(f'{elem[0]:<7}{elem[1]}{elem[3]:>8}')
