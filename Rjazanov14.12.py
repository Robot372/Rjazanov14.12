from random import *
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
     mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos,n)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg,n)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    sort(s)
    print(s)

def vahetus(a:int,b:int):
    """
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    for i in range(n):
     loend.append(randint(a,b))
    

def jagamine(loend,p,n,nol):
    for el in loend:
        if el>0:
            p(append(el))
        elif el<0:
            n(append(el))
        else:
            nol(append(el))

def keskmine(loend,n):
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
            kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    loend(append(el))
    loend(sort())

arvud_loendis()

