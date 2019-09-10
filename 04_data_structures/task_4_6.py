# -*- coding: utf-8 -*-
'''
Задание 4.6
aaaaaaaaaaaaaaaaaaaaa
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
pr='''Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}'''
l=ospf_route.split()
print(l)
print(pr.format(l[0], l[1], l[2].strip('[]'), l[4].rstrip(','), l[5].rstrip(','), l[6]))
