# conversor de bases numericas
# autor: Alisson Guilherme

print('Conversor de bases numericas')
print('-'*30)

print('''Qual base numerica deseja utilizar ?
Decimal     [ 1 ] 
Binário     [ 2 ]
Octal       [ 3 ]
Hexadecimal [ 4 ]
''')
opcao = int(input("opção: "))

if opcao == 1:
    numDecimal = int((input('Digite um número decimal: ')))
    print('convertido para binário: {}'.format(bin(numDecimal)))
    print('convertido para hexadecimal: {}'.format(hex(numDecimal)))
    print('convertido para octal: {}'.format(oct(numDecimal)))

elif opcao == 2:
    pass
elif opcao == 3:
    pass
elif opcao == 4:
    pass
else:
    print('opção não recohecida')
