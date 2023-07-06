menu = """
=============== MENU ===============
                
                [1] DEPOSITAR
                [2] SACAR
                [3] EXTRATO
                [4] SAIR

=====================================             

"""

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 0
extratos = []

def formatado(valor):
    v_format = format(valor, ".2f")    
    return v_format





while True:
    opcao = input(menu)

    if opcao == "1":

        valor_deposito = float(input("Digite valor de deposito R$ "))
        valor_formatado = formatado(valor_deposito)
        
        if valor_deposito > 0:

            saldo += valor_deposito
            extrato = {"tipo":"Deposito","valor": valor_deposito} 
            extratos.append(extrato)       
            print(f"SALDO DE R$ {formatado(saldo)}") 

        else:
            print("            ERRO        ")
            print("Valor deve ser número positivo !")   

    elif opcao == "2":
        
        print(f"Valor de Saldo R$ {formatado(saldo)}")
        valor_saque = float(input("Digite Valor desejado do saque R$ "))

        extrato = {"tipo":"Saque","valor": valor_saque} 
        extratos.append(extrato)
        
        
        if valor_saque <= limite and valor_saque < saldo and limite_saques <=3:
            
            saldo -= valor_saque
            limite_saques += 1
            print(f"LIMITE DE SAQUE DIÁRIO: {limite_saques}")
            print(formatado(saldo))
            if limite_saques >3:
                print("ERRO: Limite de saque diário ultrapassado")
                
        
        else:
            if valor_saque > limite or valor_saque > saldo:          
                print("ERRO: Saldo insuficiente")           

               
         

    elif opcao == "3":
        print('-----------------------')

        for operacao in extratos:
            valor_x = formatado(operacao["valor"])
            print(operacao["tipo"],valor_x)       
            
      
    elif opcao == "4":
        break

    else:
        print("Operação inválida, porfavor selecione um comando válido.")  




