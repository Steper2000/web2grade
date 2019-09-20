# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
                    
                    if "duplex auto" in fstr[i+2]:
                        vlan=1
                    else:
                        vlan=fstr[i+2][fstr[i+2].find('vlan ')+5:]

                    intrf=fstr[i][fstr[i].find(' ')+1:]
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
            

print(get_int_vlan_map("C:/WEB/2-grade/ready-exercises/09_functions/config_sw2.txt"))