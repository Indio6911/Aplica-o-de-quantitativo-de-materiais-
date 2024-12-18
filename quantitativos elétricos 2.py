import objetos_eletricos

def main():
    print("=== Sistema de Avaliação de Quantitativos de Materiais Elétricos ===")
    
    materiais = {}
    continuar = True

    while continuar:
        print("\n--- Cadastro de Material Elétrico ---")
        nome_material = input("Digite o nome do material: ").strip()
        cor = input('digite o nome da cor ').strip()
        try:
            quantidade_por_ponto = int(input(f"Quantas unidades de {nome_material} são necessárias por ponto elétrico? "))
            quantidade_pontos = int(input(f"Quantos pontos elétricos serão instalados? "))
        except ValueError:
            print("Erro: Insira valores numéricos válidos!")
            continue
        
        material = objetos_eletricos.materiais_eletricos(nome_material ,cor, quantidade_pontos,quantidade_por_ponto )
        materiais[nome_material] = material

        print(f"Total de {nome_material}: {material.quantidade} unidades.")
        
        # Perguntar ao usuário se deseja continuar cadastrando materiais
        resposta = input("Deseja cadastrar outro material? (s/n): ").strip().lower()
        if resposta != "s":
            continuar = False

    # Exibir resumo dos materiais
    print("\n=== Resumo de Quantitativos ===")
    for material, quantidade in materiais.items():
        print(f"{material}: {quantidade} unidades")
    print("Obrigado por usar o sistema!")


if __name__ ==  '__main__':
    main()