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

   
    def depositar(self,valor):

        if valor >0:
            self._saldo =+ valor

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

    def adicionar_transacao(self,transacao):

        self._transacoes.append({

            "tipo":transacao.__class__.__name__,
            "valor":transacao.valor, #?
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        })

            
cliente1 = PessoaFisica("000.000.000-00","Eto","18/1/1999","XY 55")
conta_corrente1 = ContaCorrente(12345, cliente1)
conta_corrente1.depositar(1000)

conta_corrente1.sacar(100)
conta_corrente1.sacar(100)
conta_corrente1.sacar(100)
conta_corrente1.sacar(100)
print(conta_corrente1.saldo)
print(conta_corrente1.saques_realizador)
print(conta_corrente1.historico.transacoes)
