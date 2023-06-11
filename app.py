import datetime
from time import ctime
remedios=[]
x=0
n='nao'
contador=0
remediopordia=0
while x!=n:
    remedios.append(str(input("Qual o remedio que voce toma? ")))
    remedios.append(int(input("Quantos remédios você toma por dia? ")))
    x=str(input("Voce toma algum outro remedio? sim/nao: "))
hoje = datetime.date.today()
dia = hoje.day
mes = hoje.month
print(mes)
print(hoje)
datafinal = hoje
print(type(dia))
print(remedios)
pilulas = int(input("Quantas pilulas voce comprou: "))
diaremedio = (dia+pilulas)
if diaremedio<=31:
    datafinal = hoje.replace(day=diaremedio)    
else:
    while diaremedio > 31:
        if (mes+1) == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            print("ta funcionando")
            while diaremedio>31:
                mes=mes+1
                diaremedio = diaremedio-31
        else:
            while diaremedio>30:
                print("ta funfando 2")
                mes=mes+1
    print(datafinal)
    datafinal = datafinal.replace(month=mes)
diafinal = datafinal.day
mesfinal = datafinal.month
anofinal = datafinal.year
print(diafinal,"/",mesfinal,"/",anofinal)
print()