class Conta:
    def __init__(self, titular, saldo, senha, deposito_inicial):
      self.titular = titular
      self.saldo = saldo 
      self.deposito = deposito_inicial
      self.senha = senha
#metodo Saque
  def Sacar(self,valor):
    if self.saldo >= valor:
        self.saldo-=valor
else:
    print('Saldo indisponivel')
