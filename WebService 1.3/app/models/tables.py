from app import db


class Usuario(db.Model):
    __tablename__ = "usuarios"

    # id identifica de forma única da linha na tabela
    id = db.Column(db.Integer, primary_key=True)  # chave primária = campo de identificação
    usuario = db.Column(db.String, unique=True) # deve ter valor sem repetições
    senha = db.Column(db.String)
    cnpj = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    categoria = db.Column(db.String)
    # Faltam, infopagamento e privilegios
    # db.ForeignKey em um db.Column > referência algo em outra tabela "tabela.algo"
    # db.relationship('tabela relacionada', foreign_keys()

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, usuario, senha, cnpj, email, nome, categoria):
        self.usuario = usuario
        self.senha = senha
        self.cnpj = cnpj
        self.email = email
        self.nome = nome
        self.categoria = categoria

    def __repr__(self):
        return "<Usuario %r>" % self.categoria  # Representação na pesquisa no banco de dados
