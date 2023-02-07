from math import * 
from random import * 
from module2 import * 

#03/02/23
arvud=[]
isikukoodid=[]

while True:
    ik=input("Sisestage isikukood: ") #str - просто строка
    if ik=="1": break
    if len(ik)!=11:
        print("Liiga palju või liiga võhe sümboleid. Sisesta veel kord:")
        arvud.append(ik)
    else:
        print("Isikukoodi kontroll")
        ik_list=list(ik)
        s1=int(ik_list[0]) #"1"->1
        if s1 not in [1,2,3,4,5,6]:
            print("Esimene sümbol ei ole õige!")
            arvud.append(ik)
        else:
            print("Esimene sümbol on õige")
            spaev=Sünnipaev(ik_list)
            if spaev=="Viga":
                arvud.append(ik)
            else:
                #
                print(f"Sünnipäev on {spaev}")
                print(f"Viimane number: ,{ik_list}")
                kontrollnr=0
                a1=int(ik[0])*1
                b1=int(ik[1])*2
                b2=int(ik[2])*3
                b3=int(ik[3])*4
                b4=int(ik[4])*5
                b5=int(ik[5])*6
                b6=int(ik[6])*7
                b7=int(ik[7])*8
                b8=int(ik[8])*9
                b9=int(ik[9])*1

                s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
                print(s11)
                s=s11//11
                print(s)
                p=s*11
                p1=s11-p
                if p1==int(ik[10]):
                    print(p1)
                else:
                    a1=int(ik[0])*3
                    b1=int(ik[1])*4
                    b2=int(ik[2])*5
                    b3=int(ik[3])*6
                    b4=int(ik[4])*7
                    b5=int(ik[5])*8
                    b6=int(ik[6])*9
                    b7=int(ik[7])*1
                    b8=int(ik[8])*2
                    b9=int(ik[9])*3
                    s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
                    print(s11)
                    s=s11//11
                    print(s)
                    p=s*11
                    p1=s11-p
                    print(p1)


                hhh=int(ik_list[8]+ik_list[9]+ik_list[10])
                #
                haigla=Sunnikoht(hhh)

                #
                sugu=Sugu(ik_list)
                print(f"See on {sugu}, sünnipäev {spaev}. Ta on sündinud {haigla}")
                isikukoodid.append(ik)

while True:
    print(isikukoodid)
    isikukoodid=naised_mehed(isikukoodid)
    print(isikukoodid)
    arvud=list(map(int, arvud))
    arvud.sort()
    print(arvud)

print(isikukoodid)
arvud=list(map(int,arvud))
arvud.sort()
print(arvud)
#Создание пользовательских функций