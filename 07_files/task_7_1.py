# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
pr='''Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}'''

with open("C:/WEB/2-grade/ready-exercises/07_files/ospf.txt", 'r') as f:
    for ospf_route in f:
        l=ospf_route.split()
        print('\n', pr.format(l[0], l[1], l[2].strip('[]'), l[4].rstrip(','), l[5].rstrip(','), l[6]))