import datetime
import math

from datetime import date, timedelta

dthoje = datetime.datetime.now()
print(dthoje.strftime("%d/%m/%Y"))

dtnasc=datetime.datetime(1969, 4, 16)
print(dtnasc.strftime("%d/%m/%Y"))

x15=timedelta(15)
x65=timedelta(65)
x1ano=timedelta(365)

print((dthoje-dtnasc).days," - dias desde o nascimento até hoje")

print(math.floor((dthoje-dtnasc).days/365.25), "anos calculados\n")

print( (dthoje+x15).strftime("%d/%m/%Y"), "data de hoje + 15 dias")
print( (dthoje+x65).strftime("%d/%m/%Y"), "data de hoje - 65 dias\n")

print((dthoje+x1ano).strftime("%d/%m/%Y"), "hoje + 365 dias")