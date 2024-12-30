import objetos_eletricos
import PySimpleGUI as sg

def main():

    sg.theme("Black")
    layout = [
        [sg.Text("Nome do Material:")],
        [sg.Input(key="nome_material")],
        [sg.Text("Cor:")],
        [sg.Input(key="cor")],
        [sg.Text("Quantas unidades são necessárias por ponto elétrico:")],
        [sg.Input(key="quantidade_por_ponto")],
        [sg.Text("Quantos pontos elétricos serão instalados?:")],
        [sg.Input(key="quantidade_pontos")],
        [sg.Button("Cadastrar"), sg.Button("Visualizar")]
    ]

    interface = sg.Window("Quantitativo Elétrico", layout=layout, finalize=True)
    materiais = {}

    while True:
        janela, evento, valores = sg.read_all_windows()

        if evento == sg.WIN_CLOSED:
            break
        elif evento == "Cadastrar":
            if janela["nome_material"].get() == "" or janela["caracteristicca"].get() == "" or janela["quantidade_pontos"].get() == "" or janela["quantidade_por_ponto"].get() == "":
                sg.popup("Preencha todos os campos!")
                continue

            nome_material = janela["nome_material"].get() 
            caracteristica = janela["caracteristica"].get()
            try:
                quantidade_pontos = int(janela["quantidade_pontos"].get()) 
                quantidades_por_ponto = int(janela["quantidade_por_ponto"].get())
            except Exception:
                sg.popup("Os campos quantidades por ponto elétrico e quantidade de pontos devem ser números!")
                continue

            material = objetos_eletricos.materiais_eletricos(nome_material, caracteristica , quantidade_pontos, quantidades_por_ponto)
            materiais[nome_material] = material  

            sg.popup("Item Cadastrado com Sucesso!")

        elif evento == "Visualizar":
            msg = "=== Resumo de Quantitativos ==="
            for material, quantidade in materiais.items():
                msg = msg + f"\n{material}: {quantidade.quantidade} unidades"
            
            msg = msg + "\nObrigado por usar o sistema!"

            sg.popup(msg)

    janela.close()


if __name__ ==  '__main__':
    main()