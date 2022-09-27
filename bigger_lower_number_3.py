
a = float(input('Primeiro numero = '))
b = float(input('Segundo numero = '))
c = float(input('Terceiro numero = '))

if a == b == c:
    print('Todos os numeros são iguais')
else:
    if a < b > c:
        print(f'o maior valor dentre os tres numeros fornecidos é {b:.2f}')
        if a == c:
            print('Enquanto isso, os outros dois numeros tem o mesmo valor de ', a)
        else:
            if a > c:
                print(f'Enquanto isso, o menor valor dos tres numeros foi o valor de {c:.2f}')
            else:
                print(f'Enquanto isso, o menor valor dos tres numeros foi o valor de {a:.2f}')
    if b < c > a:
        print(f'o maior valor dentre os tres numeros fornecidos é {c:.2f}')
        if b == a:
            print('Enquanto isso, os outros dois numeros tem o mesmo valor de ', a)
        else:
            if b > a:
                print(f'Enquanto isso, o menor valor dos tres numeros foi o valor de {a:.2f}')
            else:
                print(f'Enquanto isso, o menor valor dos tres numeros foi o valor de {b:.2f}')
    if c < a > b:
        print(f'o maior valor dentre os tres numeros fornecidos é {a:.2f}')
        if b == c:
            print('Enquanto isso, os outros dois numeros tem o mesmo valor de ', b)
        else:
            if b > c:
                print(f'Enquanto isso, o menor valor dos tres numeros foi o valor de {c:.2f}')
            else:
                print(f'Enquanto isso, o menor valor dos tres numeros foi o valor de {b:.2f}')

