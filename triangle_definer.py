

a = float(input('tamanho do lado 1 = '))
b = float(input('tamanho do lado 2 = '))
c = float(input('tamanho do lado 3 = '))

if ((a) > abs(b -c) and a < (b + c)) or ((b) > abs(c-a) and b < (b + c)) or ((c) > abs(a + b) and c < (a + b)):
    if (a == b) or (b == c) or (c == a):
        if a == b == c:
            print('Este é um triangulo equilátero')
        else:
            print('Este é um trianguo isóceles')
    else:
        print('Este é um triangulo escaleno')

else:
    print('Não é possível formar um triangulo com estas medidas.')
