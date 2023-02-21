from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    usuario = StringField("usuario", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired()])


class CadastroForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('e-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('confirmar senha', validators=[DataRequired(),
                                                                   EqualTo('senha')])
    cnpj = StringField('cnpj', validators=[DataRequired()])
    usuario = StringField("usuario", validators=[DataRequired()])
    categoria = SelectField('Categoria', choices=[('Empresa/MEI', 'Empresa/MEI'),
                                                  ('Político', 'Político')])
