# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
ipm=argv[1]
ip=ipm[0:ipm.find('/')]
m=ipm[ipm.find('/')+1:]
print(m)
mi=int(m)

oc=ip.split('.')
ipbs='0'*(8-len(bin(int(oc[0])).lstrip('0b'))) + bin(int(oc[0])).lstrip('0b')+'0'*(8-len(bin(int(oc[1])).lstrip('0b'))) + bin(int(oc[1])).lstrip('0b')+'0'*(8-len(bin(int(oc[2])).lstrip('0b'))) + bin(int(oc[2])).lstrip('0b')+'0'*(8-len(bin(int(oc[3])).lstrip('0b'))) + bin(int(oc[3])).lstrip('0b')

#print(ipbs)
pmb=ipbs[:mi]+'0'*(32-mi)
#print(pmb)

print(f'''
----------------------------
Network
     {int(pmb[0:8], 2):<8} {int(pmb[8:16],2):<8} {int(pmb[16:24], 2):<8} {int(pmb[24:32],2):<8}
     {int(pmb[0:8]):08} {int(pmb[8:16]):08} {int(pmb[16:24]):08} {int(pmb[24:32]):08}''')



mb='1'*mi +'0'*(32-mi)
#print(mb[:8])

print(f'''
Mask
     {int(mb[0:8], 2):<8} {int(mb[8:16], 2):<8} {int(mb[16:24], 2):<8} {int(mb[24:32], 2):<8}
     {int(mb[0:8]):08} {int(mb[8:16]):08} {int(mb[16:24]):08} {int(mb[24:32]):08}''')
