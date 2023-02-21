from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin


app = Flask(__name__, template_folder='templates')
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

lm = LoginManager()
lm.init_app(app)


@lm.user_loader
def load_user(user_id):
    from app.models.tables import Usuario
    return Usuario.query.get(int(user_id))


from app.models import tables, forms
from app.controllers import cliente

