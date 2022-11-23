from Usuario import Usuario

class Politico(Usuario):
    def __init__(self, nome, senha, cnpj, contatos, infoPagamento, informacoesPartido, bandeiras, curriculo ) -> None:
        super().__init__(nome, senha, cnpj, contatos, infoPagamento)
        self.__informacoesPatido = informacoesPartido
        self.__bandeiras = bandeiras
        self.__curriculo = curriculo