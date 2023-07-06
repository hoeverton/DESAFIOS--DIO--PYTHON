def menu():
    opcao_menu = input( """
=============== MENU ===============
                
                [1] DEPOSITAR
                [2] SACAR
                [3] EXTRATO
                [4] SAIR

=====================================             

""")
    return opcao_menu



def formatado(valor):
    v_format = format(valor, ".2f")    
    return v_format

def depositar(valor_deposito, extratos, saldo_atual):
    if valor_deposito > 0:
        saldo_atual += valor_deposito
        extrato = {"tipo": "Deposito", "valor": valor_deposito} 
        extratos.append(extrato)
        print(f"SALDO DE R$ {formatado(saldo_atual)}")
        
    else:
        print("            ERRO        ")
        print("Valor deve ser número positivo !")   

    return saldo_atual, extratos

def sacar(saldo,valor_saque,limite_saques,limite):
     print(f"VALOR SALDO DA FUNCAO {saldo}")
     if valor_saque <= limite and valor_saque < saldo and limite_saques < 3:
            saldo -= valor_saque
            limite_saques += 1
            print(f"LIMITE DE SAQUE DIÁRIO: {limite_saques}")
            print(formatado(saldo))
            
            if limite_saques > 3:
                print("ERRO: Limite de saque diário ultrapassado")
     else:
            if valor_saque > limite or valor_saque > saldo:          
                print("ERRO: Saldo insuficiente")      
     return saldo, limite_saques

def fun_extrato(extratos,saldo):   
           
        for operacao in extratos:
            valor_x = formatado(operacao["valor"])
            print(operacao["tipo"],valor_x)      
        print(f" Saldo em conta R$ {formatado(saldo)}")    
  
def func_usuario(usuarios):
    nome_usuario = input("Usuario: ")
    if nome_usuario not in  usuarios:
        print('Verificamos que você não tem uma conta aberta, vamos realizar seu cadastro!')
        nome = input("Nome: ")
        cpf =  input("CPF: ")
        endereco = input("Endereço: ")
        conta = func_conta(usuarios)  
        
        usuario = {"Nome:":nome, "cpf:": cpf, "Endereço:": endereco, "Agencia":conta["Agencia"],"C/C ":conta["Numero da conta:"]}
        print('---------------------------')
        print(f" Segue os dados da sua conta Agencia:{usuario['Agencia'] } C/C: {usuario['C/C ']}")
    
    return usuarios.append(usuario)


def func_conta(conta_correntes:0):

        if conta_correntes not in conta_correntes:
            numero_conta = "000"
            ag = "001"
            conta_ag = None
            numero_conta = str(int( numero_conta) + 1).zfill(3)
            conta_ag = {"Numero da conta:": numero_conta, "Agencia": ag}
            conta_correntes.append(conta_ag)

            
                     

        return conta_ag    
         

def main():
    saldo = 0
    limite = 500
    numero_saques = 0
    limite_saques = 0
    extratos = []
    usuarios = []
    conta_correntes = []
    func_usuario(usuarios)
    
    while True:
        opcao = menu()

        if opcao == "1":
            valor_deposito = float(input("Digite valor de deposito R$ "))
            saldo, extratos = depositar(valor_deposito, extratos, saldo)
            
        elif opcao == "2":
            print(f"Valor de Saldo R$ {formatado(saldo)}")
            valor_saque = float(input("Digite Valor desejado do saque R$ "))

            extrato = {"tipo": "Saque", "valor": valor_saque} 
            extratos.append(extrato)
            saldo, limite_saques = sacar(saldo,valor_saque,limite_saques,limite)       

        elif opcao == "3":
            print('-----------------------')
            print("          EXTRATO      ")        
        
            fun_extrato(extratos,saldo)
        elif opcao == "4":
            break  

main()         