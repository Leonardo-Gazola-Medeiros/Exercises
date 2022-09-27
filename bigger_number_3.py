
a = float(input('Primeiro numero = '))
b = float(input('Segundo numero = '))
c = float(input('Terceiro numero = '))

if a == b == c:
    print('Todos os numeros são iguais')
else:
    if a < b > c:
        print(f'o maior valor dentre os tres numeros fornecidos é {b:.2f}')
    if b < c > a:
        print(f'o maior valor dentre os tres numeros fornecidos é {c:.2f}')
    if c < a > b:
        print(f'o maior valor dentre os tres numeros fornecidos é {a:.2f}')
