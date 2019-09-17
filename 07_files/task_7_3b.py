# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan=input("Введите vlan: ")

with open("C:/WEB/2-grade/ready-exercises/07_files/CAM_table.txt", 'r') as f:
    for line in f:
        strl=line.split()
        if len(strl) == 4 and strl[0] != "----" and strl[0] != "Vlan" and strl[0]==vlan:
            print(f'{strl[0]:<7}{strl[1]}{strl[3]:>8}')

            