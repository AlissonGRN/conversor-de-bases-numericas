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
    print('convertido para binário: {}'.format(bin(numDecimal)[2:]))
    print('convertido para hexadecimal: {}'.format(hex(numDecimal)[2:]))
    print('convertido para octal: {}'.format(oct(numDecimal)[2:]))

elif opcao == 2:
    numBinario = input('Digite um número em binario: ')
    print('convertido para decimal: {}'.format(int(numBinario, 2)))
    print('convertido para hexadecimal: {}'.format(hex(int(numBinario, 2))[2:]))
    print('convertido para octal: {}'.format(oct(int(numBinario, 2))[2:]))


elif opcao == 3:
    pass
elif opcao == 4:
    pass
else:
    print('opção não recohecida')
