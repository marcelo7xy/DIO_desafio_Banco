"""                SISTEMA_BANCÁRIO
Implementar apenas 3 operações: depósito, saque e extrato.

* 1 único usuário
* Depositar valores positivos.
* Variável extrato exibindo todos os valores de depósito e saque.

* perguntar valor a ser depositado, inteiro e positivo.
* apenas 3 saques diários com limite máximo de R$ 500,00 por saque.
* exibir erro por falta de saldo.
* exibir valores "R$ xxx.xx"

"""

from time import sleep
conta = 0
quantidade_de_depositos = 0
quantidade_de_saques = 0
LIMITE_SAQUE_DIARIO = 500
extrato = ""

while True:
    opcoes = print("""
    ############ Banco Parma ############

            [1] Deposito
            [2] Saque
            [3] Extrato
            [0] Sair

    #####################################
    """)
    menu = int(input("Escolha uma opção: "))
    if menu == 1:
        while True:
            deposito =float(input("Quanto gostaria de depositar:R$ "))
            if deposito > 0:
                conta += deposito
                quantidade_de_depositos =+ 1
                extrato += f"{quantidade_de_depositos}º Deposito: R${deposito}\n"
                print("Depositando...\n")
                sleep(1.5)
                print(f"R${deposito:.2f} depositado com sucesso")
                break
            else:
                print("entrada inválida. tente novamente...\n")
                sleep(2)

    elif menu == 2:
        if quantidade_de_saques < 3:
            quantidade_de_saques += 1
            while True:
                saque = float(input("Quanto gostaria de sacar:R$ "))
                if saque > 0:
                    if saque > LIMITE_SAQUE_DIARIO:
                        print("Limite máximo por saque de R$ 500.00, tente novamente\n")
                        sleep(1.5)
                        continue
                    if saque > conta:
                        print("Saldo insuficiente. tente novamente\n")
                        sleep(1.5)

                    elif saque <= conta:
                        conta -= saque
                        extrato += f"{quantidade_de_saques}º Saque: R${saque}\n"
                        print(f"sacando R${saque:.2f}...")
                        sleep(1)
                        print("aguarde a contagem das cédulas... ", end= "")
                        sleep(3)
                        print("retire seu dinhero...\n")
                        sleep(1.3)
                        print(f"saldo atual >> R${conta:.2f}")
                        break
                else:
                    print("entrada inválida. tente novamente...")
        else:
            print("Número de máximo de saques diário atingido. Favor entrar em contato com o seu gerente")

    elif menu == 3:
        print("imprimindo...")
        sleep(1.5)
        print("Não foram realizadas movimentações." if not extrato else extrato)

        '''
        print(f"""
        Seu saldo atual é de {conta}
        Último deposito foi de {deposito}
        Último saque foi de {saque}
        """)
        '''
        sleep(4)
    elif menu == 0:
        print("Encerrando operação...")
        sleep(1.8)
        print("Obrigado e volte sempre")
        break
    else:
        print("entrada inválida, tente novamente...")
        sleep(2.2)
        continue
    sleep(3)
