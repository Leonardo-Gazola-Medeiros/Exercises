
peso = float(input('Peso dos peixes = '))


if peso > 50.0 :
    excesso = peso - 50.0
    multa = excesso*4.0
    print(f'Houve excesso de pesca e a multa a ser paga será de {multa:.2f}')
else:
    excesso = 0
    multa = 0
    print(f'Não houve excesso de pesca, então o valor de multa a ser pago será {multa:.2f}')
    
