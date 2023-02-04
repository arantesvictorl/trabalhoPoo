from Usuario import Usuario

class Empresa(Usuario):
    def __init__(self, nome, senha, cnpj, contatos, infoPagamento, ramoAtuacao, esteticaVisual, publicoAlvo, produtoPrincipal) -> None:
        super().__init__(nome, senha, cnpj, contatos, infoPagamento)
        self.__ramoAtuacao = ramoAtuacao
        self.__esteticaVisual = esteticaVisual
        self.__publicoAlvo =  publicoAlvo
        self.__produtoPrincipal = produtoPrincipal

    @property
    def getramoAtuacao(self):
        return self.__ramoAtuacao

    @getramoAtuacao.setter
    def setramoAtuacao(self, ramoAtuacao):
        self.__ramoAtuacao = ramoAtuacao
        
    @property
    def getesteticaVisual(self):
        return self.__esteticaVisual

    @getesteticaVisual.setter
    def setesteticaVisual(self, esteticaVisual):
        self.__esteticaVisual = esteticaVisual
    
    @property
    def getpublicoAlvo(self):
        return self.__publicoAlvo
    
    @getpublicoAlvo.setter
    def setpublicoAlvo(self, publicoAlvo):
        self.__publicoAlvo = publicoAlvo

    @property
    def getprodutoPrincipal(self):
        return self.__produtoPrincipal

    @getprodutoPrincipal.setter
    def setprodutoPrincipal(self, produtoPrincipal):
        self.__produtoPrincipal = produtoPrincipal




        


        