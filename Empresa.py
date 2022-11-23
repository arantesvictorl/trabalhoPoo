from Usuario import Usuario

class Empresa(Usuario):
    def __init__(self, nome, senha, cnpj, contatos, infoPagamento, servicos, mercado, tempoMercado, filosofia, tamanho) -> None:
        super().__init__(nome, senha, cnpj, contatos, infoPagamento)
        self.__servicos = servicos
        self.__mercado = mercado
        self.__tempoMercado = tempoMercado
        self.__filosofia =  filosofia
        self.__tamanho = tamanho

        