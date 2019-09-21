# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#import ipaddress
import subprocess
def ping_ip_addresses(ip_list):
    com1=[]
    com2=[]
    for ip in ip_list:
        reply=subprocess.run(['ping', ip])
        if reply.returncode==0:
            com1.append(ip)
        else:
            com2.append(ip)
    l=[com1, com2]
    com=tuple(l)
    return com


iplist=['10.10.10.3', '8.8.8.8', '87.250.250.242', '6.8.3.6']
print(ping_ip_addresses(iplist))
