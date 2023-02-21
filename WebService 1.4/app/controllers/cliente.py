from app import app, db
from flask_login import login_user
from flask import render_template, send_from_directory, redirect, flash, url_for

from app.models.tables import Usuario
from app.models.forms import LoginForm, CadastroForm


@app.route('/static/images/<path:path>')
def send_image(path):
    return send_from_directory('static/images', path)


# Página de login/inicial
# Se o usuario ou senha não forem inseridos corretamente, a página só sera recarregada
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


# Página de cadastro -> redireciona para o login quando cadastrar corretamente
# Se o email não for inserido na norma padrão, todos os campos não forem preenchidos,
# ou ainda o campo "confirmar senha" não for igual ao "senha", a pagina só será recarregada
@app.route("/signin", methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usr = Usuario(form.usuario.data, form.senha.data, form.cnpj.data, form.email.data,
                      form.nome.data, form.categoria.data)
        db.session.add(usr)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('formCli.html', form=form)

