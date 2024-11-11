def calcular_revestimento(area, rendimento_por_metro):
    """Calcula a quantidade de revestimento necessária."""
    return area / rendimento_por_metro

def obter_area():
    """Obtém a área a ser revestida do usuário."""
    while True:
        try:
            area = float(input("Digite a área a ser revestida em metros quadrados: "))
            if area <= 0:
                print("A área deve ser um número positivo.")
            else:
                return area
        except ValueError:
            print("Por favor, insira um número válido.")

def obter_rendimento():
    """Obtém o rendimento do revestimento do usuário."""
    while True:
        try:
            rendimento = float(input("Digite o rendimento do revestimento em metros quadrados por unidade: "))
            if rendimento <= 0:
                print("O rendimento deve ser um número positivo.")
            else:
                return rendimento
        except ValueError:
            print("Por favor, insira um número válido.")

def obter_preco_por_unidade():
    """Obtém o preço por unidade de revestimento do usuário."""
    while True:
        try:
            preco = float(input("Digite o preço por unidade de revestimento: "))
            if preco < 0:
                print("O preço deve ser um número não negativo.")
            else:
                return preco
        except ValueError:
            print("Por favor, insira um número válido.")

def calcular_custo(quantidade, preco):
    """Calcula o custo total do revestimento."""
    return quantidade * preco

def main():
    print("Cálculo de Custo do Revestimento")
    
    area = obter_area()
    rendimento = obter_rendimento()
    preco = obter_preco_por_unidade()

    quantidade = calcular_revestimento(area, rendimento)
    custo_total = calcular_custo(quantidade, preco)

    print(f"A quantidade de revestimento necessária é: {quantidade:.2f} unidades.")
    print(f"O custo total do revestimento é: R$ {custo_total:.2f}")

if _name_ == "_main_":
    main()