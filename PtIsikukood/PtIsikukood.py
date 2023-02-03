from math import * 
from random import * 

while True:
    ik=input("Sisestage isikukood: ") #str - просто строка
    if len(ik)!=11:
        print("Liiga palju või liiga võhe sümboleid. Sisesta veel krd:")
    else:
        print("Isikukoodi kontroll")
        ik_list=list(ik)
        s1=int(ik_list[0]) #"1"->1
        if s1 not in [1,2,3,4,5,6]:
            print("Esimene sümbol ei ole õige!")
        else:
            print("Esimene sümbol on õige")
            y=ik_list[1]+ik_list[2] #aasta
            m=ik_list[3]+ik_list[4] #kuu
            d=ik_list[5]+ik_list[6] #päev
            if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
                print("Sünnipäev ei saa luua")
            else:
                if s1==1 or s1==2:
                    yy="18"
                elif s1==3 or s1==4:
                    yy=="19"
                else:
                    yy="20"
                spaev=str(d)+"."+str(m)+"."+yy+str(y) #ei ole 18...,19...,20...
                print(f"Sünnipäev on {spaev}")
                print(f"Viimane number: {ik_list[-1]}")