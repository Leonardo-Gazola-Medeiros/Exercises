
preço = float(input('informe o preço: '))
desconto = float(input('informe o desconto(%): '))
total = (preço - (preço*(desconto/100)))
print( 'o preço final do produto será de: ', total)