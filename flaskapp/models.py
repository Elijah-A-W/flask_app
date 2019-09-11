from flaskapp  import db, app
from flask_login import LoginManager

login_manager = LoginManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return'{}'.format(self.name)