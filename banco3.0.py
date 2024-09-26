import datetime
import time
import schedule

saques_dia = 10
limite_saque = 1500
saldo = 1500
depositos = []
retiradas = []
emprestimos = []
usuario = str(input('Digite seu nome: '))

def reset_dia():
     global saques_dia, limite_saque
     print('Novo dia!, realizando reset.')
     saques_dia = 10
     limite_saque = 1500


schedule.every().day.at("00:00").do(reset_dia)

def crediario():
    global saldo
    while True:

        try:
            credito = float(input("Valor desejado: R$"))
            juros = (credito / 100) * 1.7
            for parcelas in range(1, 13):
                print(f'{parcelas} x R${(credito / parcelas) + juros:.2f} = R${credito + (parcelas * juros):.2f}')
            total = int(input("Digite a quantidade de parcelas desejada: "))
            if total >=1 and total <=12:
                print(f"R${credito:.2f} liberado.")
                print(f'Dívida parcelada em {total}x de R${(credito / total) + juros:.2f}')
                saldo += credito
                emprestimos.append((credito,datetime.datetime.now()))
                break
            else:
                print("Número de parcelas inválido.")
                time.sleep(1)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número de parcelas valido.")
            time.sleep(2)
            
def retirada():
    global limite_saque, saldo, saques_dia
    try:
        if saques_dia >= 1:
            print(f'Saldo R${saldo}')
            saque = float(input('Valor do saque: R$'))
            if saque <= saldo and saque <= limite_saque:
                saldo -= saque
                limite_saque -= saque
                saques_dia -= 1
                retiradas.append((saque, datetime.datetime.now()))
                print(f'Saque de R${saque:.2f} Realizado com sucesso! Saldo atual disponivel R${saldo:.2f}')
            else:
                if saldo < saque:
                    print(f'Saldo insuficiente!. Saldo atual R${saldo}')
                if limite_saque < saque:
                    print('limite de saque atingido')
            
        else: 
            print('Limite de saques diarios atigindos!. ')  
         
    except ValueError:
        print('Digite uma entrada valida.')

def entrada():
    global saldo
    try:
        deposito = float(input('Digite o valor do deposito: R$'))
        if deposito > 0:
            saldo += deposito
            depositos.append((deposito, datetime.datetime.now()))
            print(f'Deposito realizado com sucesso! Saldo atual é de R${saldo:.2f}')
        else:
            print('valor invalido. O deposito deve ser maior que Zero.')
    except ValueError:
        (print('Entrada invalida, Verifique o numero digitado.'))

def extrato():
    global credito
    print(f'R${saldo}')
    for saque, data_hora in retiradas:
        print(f'Saque de R${saque:.2f} em {data_hora.strftime("%d/%m/%Y %H:%M:%S")}')
    for deposito, data_hora in depositos:
        print(f'Deposito de R${deposito:.2f} em {data_hora.strftime("%d/%m/%y %H:%M:%S")}')
    for credito, data_hora in emprestimos:
        print(f'Emprestimos contratados {credito:.2f} em {data_hora.strftime("%d/%m/%y %H:%M:%S")}')

while True:
    
    schedule.run_pending()


    Opçao = int(input(f'------------------------BEM VINDO AO BANCO LISOS------------------------\nBem vindo(a) {usuario.title()} \n\n\nPara Saque digite 1\nPara Deposito digite 2\nPara Extrato digite 3\nPara Crediário digite 4\nPara Finalizar digite 5\n'))
    if Opçao == 1:
        retirada()
        time.sleep(3)
    elif Opçao == 2:
        entrada()
        time.sleep(3)

    elif Opçao == 3:
        extrato()
        time.sleep(3)
    elif Opçao== 4: 
         crediario()
         time.sleep(3)

    elif Opçao == 5:
        print('Obrigado por usar o Banco Lisos')
        time.sleep(2)
        break

    

    