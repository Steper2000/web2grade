# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ipstr=input('\nВведите ip: ')
ip=ipstr.split('.')

if len(ip)!=4:
   print('Неправильный IP-адрес: не та длина')
else:
   try:
      ipi=[]
      for adress in ip:
         ipi.append(int(adress))
  
   
   except ValueError:
      print('Неправильный IP-адрес: есть буквы')
   
   else:
      if ipi[0]>=1 and ipi[0]<=223:
         print('unicast')
      elif ipi[0]>=224 and ipi[0]<=239:
         print('multicast')
      elif ipstr=="255.255.255.255":
         print("local broadcast")  
      elif ipstr=='0.0.0.0':
         print('unassigned')  
      else:
         print('unused')
   
