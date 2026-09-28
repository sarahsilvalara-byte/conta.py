class Conta:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.saldo = saldo
        self.senha = senha

    def nome_titular(self, nome):
        self.titular = nome

    def definir_senha(self, senha):
        self.senha = senha

    def retire_saldo(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
            print(f"Saque de R$ {saque:.2f} realizado.")
        else:
            print("Sem saldo suficiente.")
conta = Conta("Jeiza", 400, 1423)
conta.retire_saldo(10)
print(f"Saldo da {conta.titular}: R$ {conta.saldo:.2f}")
