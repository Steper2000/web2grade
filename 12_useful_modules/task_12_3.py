# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''
from tabulate import tabulate

def print_ip_table(reachable, unreachable):
    print('\nReachable       Unreachable\n-------------  -------------')
    for i, j in zip(reachable, unreachable):
        print(f'{i:<16}{j:<16}')
        if j==unreachable[len(unreachable)-1] and len(reachable)>len(unreachable):
            k=len(unreachable)
            while k<len(reachable):
                print(f'{reachable[k]:<16}')
                k+=1
        elif i==reachable[len(reachable)-1] and len(reachable)<len(unreachable):
            k=len(reachable)
            while k<len(unreachable):
                print(f'{unreachable[k]:>29}')
                k+=1
        
    


l=['10.101.100.2', '10.101.100.4', '10.101.100.6', '10.101.100.8', '10.101.100.9']
p=['10.101.100.1', '10.101.100.3', '10.101.100.5', '10.101.100.7', '10.101.100.10','10.101.100.12']
print_ip_table(l, p)