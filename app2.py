import datetime
from time import ctime
remedios=[]
mescom31=[1, 3, 5, 7, 8, 10, 12]
x=0
n='nao'
contador=0
remediopordia=0
while x!=n:
    remedios.append(str(input("Qual o remedio que voce toma? ")))
    remedios.append(int(input("Quantos remédios você toma por dia? ")))
    x=str(input("Voce toma algum outro remedio? sim/nao: "))
#Até aqui só estou fazendo o input no nome e quantidade dos remédios, no futuro
hoje = datetime.datetime.now()
dia = hoje.day
mes = hoje.month
print(mes)
print(hoje)
datafinal = hoje
print(type(dia))
print(remedios)
#Aqui é tudo teste de código, ver o valor de cada variável
#Aqui começa os calculos, o problema de verdade, kkkkkkkkk, risada de desespero
pilulas = int(input("Quantas pilulas voce comprou: "))
diaremedio = (dia+pilulas)
if diaremedio<=31:
    datafinal = hoje.replace(day=diaremedio)
#tem que colocar uma condicional para os meses com 30 dias, se for dia 12+19 pílulas vai dar erro, vai dar 31 dias, mas o mês vai só até 30
else:
    if (diaremedio>=30) or (diaremedio>=31):
        while diaremedio > 31:
            mes=(mes+1)
            if mes in mescom31:
                print("ta funcionando")
                diaremedio = diaremedio-31
            else:
                print("gg")
                diaremedio = diaremedio-30
        print(datafinal)
        datafinal = datafinal.replace(day=diaremedio)
        datafinal = datafinal.replace(month=mes)
diafinal = datafinal.day
mesfinal = datafinal.month
anofinal = datafinal.year
print((datafinal).strftime("%d/%m/%Y"," "))