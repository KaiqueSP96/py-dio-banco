class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.saques_realizados = 0
        self.limite_saques = 3
        self.valor_maximo_saque = 500

    def sacar(self, valor):
        if valor < 0:
            print("O valor do saque não pode ser negativo.")
            return
        
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques atingido. Você não pode sacar mais hoje.")
            return
        
        if valor > self.valor_maximo_saque:
            print(f"O valor máximo para saque é R${self.valor_maximo_saque}.")
            return
        
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        
        self.saldo -= valor
        self.saques_realizados += 1
        print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return
        
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# Exemplo de uso do sistema bancário
def main():
    conta = ContaBancaria(1500)  # Saldo inicial de R$1500

    while True:
        print("\nMenu:")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Consultar Saldo")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor_saque = input("Digite o valor do saque: ")
            # Verifica se o usuário tentou usar o sinal de negativo
            if '-' in valor_saque:
                print("O valor do saque não pode ser negativo.")
                continue
            
            try:
                valor_saque = float(valor_saque)
                conta.sacar(valor_saque)
            except ValueError:
                print("Por favor, insira um número válido para o saque.")
        
        elif opcao == '2':
            valor_deposito = input("Digite o valor do depósito: ")

            if '-' in valor_deposito:
                print("O valor do deposito não pode ser negativo.")
                continue

            try:
                valor_deposito = float(valor_deposito)
                conta.depositar(valor_deposito)
            except ValueError:
                print("Por favor, insira um número válido para o depósito.")
        
        elif opcao == '3':
            conta.consultar_saldo()
        
        elif opcao == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()