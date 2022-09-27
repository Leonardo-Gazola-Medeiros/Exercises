
dias = float(input('informe o tanto de dias '))
horas = float(input('informe o tanto de horas '))
minutos = float(input('informe o tanto de minutos'))
segundos = float(input('informe o tanto de segundos'))
total = (segundos + (minutos*60) + (horas*3600) + (dias*3600*24))
print(' o total de tempo em segundos será de: ', total)