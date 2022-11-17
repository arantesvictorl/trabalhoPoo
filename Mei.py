from Usuario import Usuario

class Mei(Usuario):
    def __init__(self, nome, senha, cnpj, contatos, tipoUsuario, infoPagamento, servicos, mercado, experiencia) -> None:
        super().__init__(nome, senha, cnpj, contatos, tipoUsuario, infoPagamento)
        self.__servicos = servicos
        self.__mercado = mercado
        self.__experiencia = experiencia
        