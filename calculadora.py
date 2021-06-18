titulo = str("calculadora")
print("\033[1;32m{:=^61}\033[m".format(titulo))

n1 = float(input("digite um número: "))
operacao = input('''\033[1;36m[+]soma
[-]subtração 
[*]multiplicação 
[/]divisão
escolha a operação: \033[m''')
n2 = float(input("digite outro número: "))
print('\033[1;33m=\033[m' * 60)

if operacao == "+" :
    print(f"\033[1;35m{n1} + {n2} = {n1 + n2}\033[m")
    print('\033[1;33m=\033[m' * 60)

if operacao == "-" :
    print(f"\033[1;35m{n1} - {n2} = {n1 - n2}\033[m")
    print('\033[1;33m=\033[m' * 60)

if operacao == "*" :
    print(f"\033[1;35m{n1} * {n2} = {n1 * n2}\033[m")
    print('\033[1;33m=\033[m' * 60)

if operacao == "/" :
    print(f"\033[1;35m{n1} / {n2} = {n1 / n2}\033[m")
    print('\033[1;33m=\033[m' * 60)
