#Задача 1
##n = input ("Введите число:" )
#a = int (n[0])
#b = int (n[1])
#c = int (n[2])
#print (a+b+c)

#Задача 4
#S = int(input('Число Журавликов:'))
#P = int(S/6) 
#K = int((S/6)*4)
#S = int(S/6)
#print(P, K, S)

#Задача 6
#n = input('Введите номер билета: ')
#a = int(n[0]) + int(n[1]) + int(n[2])
#b = int(n[3]) + int(n[4]) + int(n[5])
#if a == b:
#    print('Да это счастливый билет')
#else:
 #   print('Это обычный билет')

 #Задача 8
n,m,k = int(input('В-те 1-ю сторону: ')),int(input('В-те 2-ю сторону: ')),int(input('В-те кол-во долек: '))
if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')

