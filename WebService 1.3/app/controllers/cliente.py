from app import app, db
from flask_login import login_user
from flask import request, render_template, send_from_directory, redirect, flash, url_for

from app.models.tables import Usuario
from app.models.forms import LoginForm


@app.route('/static/images/<path:path>')
def send_image(path):
    return send_from_directory('static/images', path)


@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')


# login - formulario de autenticacao
@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usr = Usuario.query.filter_by(usuario=form.usuario.data).first()
        if usr and usr.senha == form.senha.data:
            login_user(usr)
            print(usr)
            if usr.categoria == "Empresa/MEI":
                return render_template('aplicacaoMEI.html', usuario=usr, senha=usr.senha)
            else:
                return render_template('aplicacaoPOLITICO.html', usuario=usr, senha=usr.senha)
        else:
            flash("Usuário ou senha invalidos")

    return render_template('login.html', form=form)

# rota para cadastrar manualmente - É APENAS TESTE
@app.route("/teste")
def teste():
    i = Usuario("admin", "admin", "04354/001", "vasco@gmail.com", "Gu", "Empresa/MEI")
    db.session.add(i)
    db.session.commit()
    return "OK"


# autenticacao - verifica se o usuario e senha existem
@app.route("/signin", methods=['GET'])
def cadastro():
    return render_template('formCli.html')


# página do cliente
@app.route("/autentica", methods=['POST'])
def autentica():
    usr = request.form['usuario']
    pswrd = request.form['senha']
    if usr == 'admin' and pswrd == 'admin':
        return render_template('aplicacaoMEI.html', usuario=usr, senha=pswrd)
    return render_template('login.html', msg='Usuario Inexistente!')


# página do cliente
@app.route("/cadastrarCli", methods=['POST'])
def cliente():
    nome = request.form['nome']
    cnpj = request.form['cnpj']
    email = request.form['email']
    usuario = request.form['usuario']
    senha = request.form['senha']
    return render_template('login.html', nome=nome, cnpj=cnpj, email=email, usuario=usuario,
                           senha=senha)

