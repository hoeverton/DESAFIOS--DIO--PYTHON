from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
class Cliente:

    def __init__(self,endereco):

        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self,conta):

        pass    

    def adicionar_conta(self,conta):

        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self,cpf,nome,data_nascimento,endereco):
        super().__init__(endereco)

        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:

    def __init__(self,numero,cliente):

        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
         
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero   

    @property
    def agencia(self):
        return self._agencia    

    @property
    def cliente(self):
        return self._cliente  

    @property
    def historico(self):
        return self._historico      

    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)


    
    def sacar(self,valor):
        self.valor = valor
        if self._saldo <self.valor:
            print("\tERRO Saldo insuficiente!")

        else:

            self._saldo -= self.valor  
            print('\t Saque realizado com sucesso!')  
            
            self.historico.adicionar_transacao("saque", valor)

   
    def depositar(self,valor):

        if valor >0:
            self._saldo += valor
            print('\t Deposito realizado com sucesso!')  
            self.historico.adicionar_transacao("Deposito", valor)

        else:
            print("\t ERRO Valor inválido")    


class ContaCorrente(Conta):

    def __init__(self,numero,cliente, limite=500,limite_saques=3):
        super().__init__(numero,cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self.saques_realizador = 0

    def sacar(self,valor):   
       
        if self.saques_realizador >= self._limite_saques:
            print("Operação falhou! Numero de saques execedeu o limite")
            return
        if  valor >self._limite:
            print("Atenção Limite por saque R$500,00")
            return
        self.saques_realizador += 1
        return super().sacar(valor)   

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:t\t{self.numero}
            Titular:\t{self.cliente.nome}"""     

class Historico:

    def __init__(self):

        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes    

    def adicionar_transacao(self,tipo,valor):

        self._transacoes.append({

            "tipo": tipo,      
            "valor": valor,        
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")             
        })


class Transacao(ABC):

    @property
    @classmethod
    def valor(self):
        pass

    @classmethod
    def registrar(self,valor):
        pass

class Deposito(Transacao):

    def __init__(self,valor):

        self._valor = valor

    @property
    def valor(self):

        return  self._valor

    def registrar(self,conta):

        sucesso_transacao = conta.depositar(self.valor) 

        if sucesso_transacao:

            conta.historico.adicionar_transacao(self,'Deposito',self.valor)

class Saque(ABC):

    def __init__(self,valor):

        self._valor = valor

    @property
    def valor(self):
        return self._valor


    def registrar(self,conta):

        sucesso_transacao = conta.sacar(self.valor) 

        if sucesso_transacao:

            conta.historico.adicionar_transacao(self,'Saque',self.valor)


def menu():
    opcao_menu = input( """
=============== MENU ===============
                
                [1] Já sou cliente
                [2] Nova conta
                [3] SAIR
                

=====================================             

""")
    return opcao_menu


def main():
    
    clientes = []
    contas = []
    
    
    while True:
        opcao = menu()

        if opcao == "1":
            
            verificar_usuario = input("Digite seu Nome ")
            usuario_encontrado = False
            for cliente in clientes:
                if cliente["Nome"] == verificar_usuario:
                    usuario_encontrado = True
                    

                if usuario_encontrado:
                    print("\t  Menu carregando....")
                    def menu_cliente():

                        while True:
                            menu_cliente = input("""
                                        \t [1] Deposito
                                        \t [2] Saque
                                        \t [3] Extrato 
                                        \t [4] Voltar 
                                                    
                            """)

                            if  menu_cliente == "1":
                                print("-----------")
                                
                                valor_deposito = float(input("\t Digite valor deposito R$ "))
                                dep = Deposito(valor_deposito)
                                dep.registrar(contaCorrente)
                                

                            elif  menu_cliente == "2":  
                                valor_saque = float(input("\t Digite valor saque R$ "))
                                saq = Saque(valor_saque)
                                saq.registrar(contaCorrente)
                                

                            elif menu_cliente == "3":
                                
                                
                                print("          EXTRATO      ") 
                                for dicionario in contaCorrente.historico.transacoes:
                                    
                                    
                                    print('-----------------------')
                                    for chave, valor in dicionario.items():
                                        
                                        print(f"{chave}: {valor}")
                                        
                                    print()  # Para adicionar uma linha em branco entre os dicionários
                                    print(f"Saldo em conta R$ {contaCorrente.saldo}")                          
            


                            else:
                                print("Voltando para menu inicial......") 
                                return False   


                    menu_cliente()     

                

            else:
                print("Usuário não encontrado")
                
                
        elif opcao == "2":
            print("\t Seja bem Vindo! Vamos Precisar de alguns dados seus")
            cpf =  input('\t Digite seu CPF: ') 
            nome =  input("\tDigite seu Nome:")
            data_nascimento =  input("\t Digite sua Data nascimento:")
            endereco =  input("\t Digite seu Endereco:")
            
            c1 = PessoaFisica(cpf,nome,data_nascimento,endereco)
            
            clientes.append({"Nome" : c1.nome, "Cpf" : c1.cpf})
            print("Cliente adicionado com sucesso!")
            
            contaCorrente =ContaCorrente.nova_conta(c1,"00111")
            contas.append({"cliente" :contaCorrente.cliente.nome, "numero da conta" :contaCorrente.numero})  #Add nome do cliente e numero da conta na lista contas
         
        elif opcao == "3":

            break     
        
            


      
main()