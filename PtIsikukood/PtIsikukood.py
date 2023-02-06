from math import * 
from random import * 
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
            y=ik_list[1]+ik_list[2] #aasta
            m=ik_list[3]+ik_list[4] #kuu
            d=ik_list[5]+ik_list[6] #päev
            if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
                print("Sünnipäev ei saa luua")
                arvud.append(ik)
            else:
                if s1==1 or s1==2:
                    yy="18"
                elif s1==3 or s1==4:
                    yy="19"
                else:
                    yy="20"
                spaev=str(d)+"."+str(m)+"."+yy+str(y) #ei ole 18...,19...,20...
                print(f"Sünnipäev on {spaev}")
                print(f"Viimane number: ,{ik_list}")
                kontrollnr=0

                hhh=int(ik_list[8]+ik_list[9]+ik_list[10])
                if 1<=hhh<=10:
                    haigla="kuresaare Haigla"
                elif 11<=hhh<=19:
                    haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
                elif 21<=hhh<=220:
                    haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                elif 221<=hhh<=270:
                    haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
                elif 271<=hhh<=370:
                    haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
                elif 371<=hhh<=420:
                    haigla="Narva Haigla"
                elif 421<=hhh<=470:
                    haigla="Pärnu Haigla"
                elif 471<=hhh<=490:
                    haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
                elif 491<=hhh<=520:
                    haigla("Järvamaa Haigla (Paide)")
                elif 521<=hhh<=570:
                    haigla("Rakvere, Tapa haigla")
                elif 571<=hhh<=600:
                    haigla("Valga Haigla")
                elif 601<=hhh<=650:
                    haigla("601...650")
                elif 651<=hhh<=700:
                    haigla("Lõuna-Eesti Haigla (Võru), Põlva Haigla")
                else:
                    haigla=" "

                if int(ik_list[0])%2==0:
                    sugu="naine"
                else:
                    sugu="mees"
                print(f"See in {sugu}, sünnipäev{spaev}. Ta on sündinud {haigla}")
                isikukoodid.append(ik)

print(isikukoodid)
arvud=list(map(int,arvud))
arvud.sort()
print(arvud)