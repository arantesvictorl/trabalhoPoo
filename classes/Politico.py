from Usuario import Usuario


class Politico(Usuario):
    def __init__(self, nome, senha, cnpj, contatos, infoPagamento, informacoesPartido, bandeiras, curriculo) -> None:
        super().__init__(nome, senha, cnpj, contatos, infoPagamento)
        self.__informacoesPartido = informacoesPartido
        self.__bandeiras = bandeiras
        self.__curriculo = curriculo

    @property
    def getinformacoesPartido(self):
        return self.__informacoesPartido

    @getinformacoesPartido.setter
    def setinformacoesPartido(self, informacoesPartido):
        self.__informacoesPartido = informacoesPartido

    @property
    def getbandeiras(self):
        return self.__bandeiras

    @getbandeiras.setter
    def setbandeiras(self, bandeiras):
        self.__bandeiras = bandeiras

    @property
    def getcurriculo(self):
        return self.__curriculo

    @getcurriculo.setter
    def setcurriculo(self, curriculo):
        self.__curriculo = curriculo


