from app import app
from flask import request, render_template

#raiz - home page
@app.route("/", methods=['GET']) 
def home():
    return render_template('index.html')
@app.route("/index", methods=['GET']) 
def index():
    return render_template('index.html')

#login - formulario de autenticacao
@app.route("/login", methods=['GET']) 
def login():
    return render_template('login.html')

#autenticacao - verifica se o usuario e senha existem
@app.route("/signin", methods=['GET']) 
def cadastro():
    return render_template('formCli.html')

#página do cliente
@app.route("/autentica", methods=['POST']) 
def autentica():
    usr = request.form['usuario']
    pswrd = request.form['senha']
    if usr == 'vintao' and pswrd == '12345':
        return render_template('usuario.html', usuario=usr, senha=pswrd)
    return render_template('login.html', msg='Usuario Inexistente!')

#página do cliente
@app.route("/cadastrarCli", methods=['POST']) 
def cliente():
    nome = request.form['nome']
    cnpj = request.form['cnpj']
    email = request.form['email']
    usuario = request.form['usuario']
    senha = request.form['senha']
    return render_template('usuario.html',nome=nome, cnpj=cnpj, email=email, usuario=usuario, senha=senha)
