menu = """
[d] Deposito
[e] Extrato
[s] Sacar
[q] Sair

=> """

saldo = 0
limite = 500
SAQUE_MAX = 3
numero_saque = 0
extrato = ""
sacando = 0
while True:

    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("qual valor você quer depositar?"))
        if valor <= 0:
            print("digite um valor valido")
        else:
            saldo = saldo + valor

    elif opcao == "e":
        print('____ extrato______\n')
        print("seu saldo atual é: {:.2f}".format(saldo))
        print("você sacou: {} vezes".format(numero_saque))
        print("seu ultimo saque foi: {} reais".format(sacando))

    elif opcao == "s":
        if saldo == 0 :
            print("saldo indisponivel")
            continue
        elif numero_saque == SAQUE_MAX:
            print('você atingiu o limite de saque diario')
            continue
        sacando = float(input("qual valor do saque: "))
        if  sacando > limite:
            print("o maximo por saque é 500 reais")
        elif sacando > saldo:
            print("valor maior que o saldo")
        else :
            print('saque de{:.2f} reais feito'.format(sacando))
            saldo = saldo - sacando
            numero_saque = numero_saque + 1
        
    elif opcao == "q":
        break

    else:
        print("operação invalida")
        