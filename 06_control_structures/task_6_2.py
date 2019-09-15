# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ipstr=input('\nВведите ip: ')
ip=ipstr.split('.')
if int(ip[0])>=1 and int(ip[0])<=223:
    print('unicast')
elif int(ip[0])>=224 and int(ip[0])<=239:
    print('multicast')
elif ipstr=="255.255.255.255":
    print("local broadcast")  
elif ipstr=='0.0.0.0':
    print('unassigned')  
else:
    print('unused')
