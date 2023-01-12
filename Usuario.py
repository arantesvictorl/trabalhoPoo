class Usuario():
    def __init__(self, nome, senha, cnpj, contatos, infoPagamento) -> None:
        self.__nome = nome
        self.__senha = senha
        self.__cnpj = cnpj
        self.__contatos = contatos
        self.__infoPagamento = infoPagamento

    @property
    def getNome(self):
        return self.__nome

    @getNome.setter
    def setNome(self, nome):
        self.__nome = nome

    @property
    def getSenha(self):
        return self.__senha

    @getSenha.setter
    def setSenha(self, senha):
        self.__senha = senha
    
    @property
    def getCnpj(self):
        return self.__cnpj
    
    @getCnpj.setter
    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def getContatos(self):
        return self.__contatos

    @getContatos.setter
    def setContatos(self, contatos):
        self.__contatos = contatos

    @property
    def getInfoPagamento(self):
        return self.__infoPagamento
    
    @getInfoPagamento.setter
    def setInfoPagamento(self, infoPagamento):
        self.__infoPagamento = infoPagamento
    


