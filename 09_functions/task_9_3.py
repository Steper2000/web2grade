# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
    with open(config_filename, 'r') as f:
        com1={}
        com2={}
        fstr=f.read().rstrip().split('\n')
        for i in range(len(fstr)):
            if "interface " in fstr[i]:
                if 'mode access' in fstr[i+1]:
                    intrf=fstr[i][fstr[i].find(' ')+1:]
                    vlan=fstr[i+2][fstr[i+2].find('vlan ')+5:]
                    #print(intrf, vlan)
                    com1[intrf]=int(vlan)
                elif "trunk encapsulation dot1q" in fstr[i+1]:
                    intrf=fstr[i][fstr[i].find(' ')+1:]
                    vlan=fstr[i+2][fstr[i+2].find('vlan ')+5:].split(',')
                    #print(intrf, vlan)
                    vlans=[]
                    for v in vlan:
                        vlans.append(int(v))
                    com2[intrf]=vlans
    l=[com1, com2]
    com=tuple(l)
    return com
            

print(get_int_vlan_map("C:/WEB/2-grade/ready-exercises/09_functions/config_sw1.txt"))