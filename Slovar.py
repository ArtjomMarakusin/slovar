from random import *

est_list=[]
eng_list=[]

def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def tolkimine(mas1, mas2 ): 
    sona=input("Введи слово, кoторое надо перевести ")
    signal = 0
    if sona in mas1:
        tolk=mas2[mas1.index(sona)]
    elif sona in mas2:
        tolk=mas1[mas2.index(sona)]
    else:
        signal = 1
        tolk=""
        print("Такого слова в словаре нет - у вас есть возможность его добавить:")
    return tolk, signal

def uus_sona(mas1,mas2,f1,f2):
    sona_eng=input("Введите слово на английском ")
    sona_est=input("Введите слово на эстонском ")
    mas1.append(sona_eng)
    mas2.append(sona_est)
    fail=open(f2,'a',encoding="utf-8-sig")
    fail.write(sona_est+"\n")
    fail.close()
    fail=open(f1,'a',encoding="utf-8-sig")
    fail.write(sona_eng+"\n")
    fail.close()
    return mas1, mas2

def error_in_dict(mas_est,mas_eng,f1,f2):
    nr = int(input("Введите номер слова, в котором ошибка: " + 'от 1 до '+str(len(mas_est))+' '))
    print("Ошибка в паре слов: "+ mas_est[nr-1] + " - " + mas_eng[nr-1])
    mas_est.pop(nr-1)
    mas_eng.pop(nr-1)
    fail=open(f1,'w',encoding="utf-8-sig")
    for el in mas_eng:
        fail.write(el+"\n")
    fail.close()
    fail=open(f2,'w',encoding="utf-8-sig")
    for el in mas_est:
        fail.write(el+"\n")
    fail.close()
    uus_sona(mas_eng,mas_est,f1,f2)
    print(mas_est)
    print(mas_eng)
    
def check(mas_est,mas_eng):
    result = 0
    mitu = int(input("Сколько слов у тебя спросить: " + 'от 1 до '+str(len(mas_est))+' ')) 
    for i in range(mitu):
        nr = randint(0,len(mas_est)-1)
        vastus = input("Переведи слово " + mas_est[nr] + " ")
        if vastus == mas_eng[nr]:
            print("OK")
            result += 1
    print("Процент правильных ответов",str( round(result/mitu*100)) +"%")

eng_list=loe_failist("eng.txt")
est_list=loe_failist("est.txt")

while 1:
    valik = input("Хочешь переводить, введи t. Хочешь проверить свои знания, введи с ")
    if valik == "t":
        print(eng_list)
        print(est_list)
        er = input("Все ли слова в слова написаны верно? y/n ")
        if er == 'y':
            t,s = tolkimine(eng_list, est_list)
            if s == 0:
                print(t)
            else:
                rus_list, eng_list=uus_sona(eng_list,est_list,"eng.txt","est.txt")
        else:
            print("Сейчас будем исправлять ошибку!")
            error_in_dict(est_list,eng_list,"eng.txt","est.txt")
    elif valik == "c":
        check(est_list,eng_list)
    else:
        print("Такого выбора не предусмотрено")
