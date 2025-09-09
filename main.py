from datetime import datetime

# Bloco de funções
def cria_cabecalho_extrato():
  return f"{'='*54}\nData\t\t\tOperacão\t\tValor\n{'='*54}\n"

def cria_rodape_extrato(saldo):
  return f"\n{'-'*54}\nSaldo: {f'R$ {saldo:.2f}':>47}"

def atualiza_extrato(extrato, operacao, valor):
  extrato = "\n".join(extrato.splitlines()[:-3])
  extrato += f"\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}{operacao:>13}{f'R$ {valor:.2f}':>22}\n"
  extrato += cria_rodape_extrato(saldo)
  return extrato

def mostrar_extrato():
    print(extrato)

def obter_saldo():
    pass

def atualiza_saldo_extrato(saldo):
  return f"\n{'-'*54}\nSaldo: \t\t\t\t\t{saldo:.2f}"

def atualiza_extrato(extrato, operacao, valor):
    extrato = "\n".join(extrato.splitlines()[:-3])
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    extrato += f"\n{data_hora:>17}{operacao:>13}{f'R$ {valor:.2f}':>22}\n"
    extrato += cria_rodape_extrato(saldo)
    return extrato

# Constantes
LIMITE_VALOR_SAQUE = 500
LIMITE_QTDE_SAQUES = 3

# Variáveis
saldo = 0
numero_saques = 0
extrato = cria_cabecalho_extrato() + "" + cria_rodape_extrato(saldo)

menu = """

[d] Depositar
[s] Sacar
[e] Mostrar extrato
[q] Sair

=> """

while True:    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato = atualiza_extrato(extrato, 'Depósito', valor)
        else:
            print("O valor de depósito deve ser maior que zero.")
    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))
        if valor <= 0:
            print("O valor de saque deve ser maior que zero.")
        else:
            if saldo == 0 or valor > saldo:
                print(f"Saldo insuficiente para saque de R$ {valor:.2f}.")
            elif numero_saques >= LIMITE_QTDE_SAQUES:
                print(f"O limite da quantidade de saques diários ({LIMITE_QTDE_SAQUES}) foi atingido.")
            elif valor > LIMITE_VALOR_SAQUE:
                print(f"O valor limite para saque é de R$ {LIMITE_VALOR_SAQUE:.2f}.")
            else: 
                numero_saques += 1
                saldo -= valor
                extrato = atualiza_extrato(extrato, 'Saque', valor)
                print(f"Realizado o saque de R$ {valor}.\nHá ({LIMITE_QTDE_SAQUES - numero_saques}) saques diários disponíveis.")

    elif opcao == "e":
        print(extrato)
    elif opcao == "q":
        print("Saindo do sistema...")
        break
    else:
        print("Por gentileza, selecione a opção correta!")  

