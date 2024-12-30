
class materiais_eletricos :
    def __init__(self, m, c,quantidade_pontos,quantidade_por_ponto):
        self.modelo = m
        self.quantidade = self.calcular_quantitativo_materiais(quantidade_pontos,quantidade_por_ponto)
        self.caracteristica = c
    def calcular_quantitativo_materiais(self,quantidade_por_ponto,quantidade_pontos):
        
        total_material = quantidade_por_ponto * quantidade_pontos
        return total_material

class Cabo(materiais_eletricos): 
    def __init__(self, m, c, quantidade_pontos, quantidade_por_ponto, secao): 
        super().__init__(m, c, quantidade_pontos, quantidade_por_ponto) 
        self.secao = secao


class Tomada(materiais_eletricos): 
            def __init__(self, m, c, quantidade_pontos, quantidade_por_ponto, tipo): 
                super().__init__(m, c, quantidade_pontos, quantidade_por_ponto)
                self.tipo = tipo

class Interruptor(materiais_eletricos):
     def __init__(self, m, c, quantidade_pontos, quantidade_por_ponto, tipo): 
        super().__init__(m, c, quantidade_pontos, quantidade_por_ponto) 
        self.tipo = tipo

class Disjuntor(materiais_eletricos): 
    def __init__(self, m, c, quantidade_pontos, quantidade_por_ponto, corrente_nominal):
         super().__init__(m, c, quantidade_pontos, quantidade_por_ponto) 
         self.corrente_nominal = corrente_nominal