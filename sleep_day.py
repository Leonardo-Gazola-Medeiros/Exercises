

def dormir(dia_semana, feriado):

    if feriado == True:
        return True
    elif dia_semana == False:
        return True
    elif (dia_semana == True) and (feriado == False):
        return False
    else:
        return False

print(dormir(True, True))