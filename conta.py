class Conta:
    def __init__(self, titular, saldo, senha, deposito_inicial):
      self.titular = titular
      self.saldo = saldo 
      self.senha = senha
        
  def nome_titular(self, nome):
      self.titular = nome
      
  def definir_senha(self, senha):
      self.senha = senha
      
  def retire_saldo(self, saque):
      if self.saldo >= saque:
          self.saldo-=saque
          print('saque de R$ (saque) realizado')
      else:
          print("sem saldo")
    conta = conta ("jeiza", 400, 1423)
    conta.retirar_saldo(10)
print(f"saldo da (conta.titular): R$(conta.saldo)")
      

