import string
import random

#1 задание

def stroka(n):
    a = ''
    for i in range(n):
        a += random.choice(string.ascii_letters)
    return a


def kol(n):
    dlina = len(n)
    kol_A = 0
    kol_a = 0
    for i in range(dlina):
        if n[i] in string.ascii_lowercase:
            kol_a += 1
        else:
            kol_A += 1
    if kol_a == kol_A:
        return -1
    elif kol_A > kol_a:
        return 1
    else:
        return 0 
    
def mass(n,k):
    masss = []
    for i in range(k):
        b = stroka(n)
        masss.append(b)
    return masss

def prosent(mas):
    dlina_mass = len(mass)
    ko = 0
    for i in range(dlina_mass):
        if kol(mas) == 1:
            ko += 1
    return (ko/dlina_mass)


print ('Введите количество символов')
a = int(input())
b = stroka(a)
print(b)


print('Введите количество символов в строке')
n = int (input())
print('Введите количество строк')
k = int(input())


massiv_strok = mass(n,k)
print(massiv_strok)