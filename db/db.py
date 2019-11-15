from app import db

# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __init__(self, code, email, password):
        self.code = code
        self.email = email
        self.password = password

# Token Table
class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(120), unique=True)
    access_token = db.Column(db.String(120))
    refresh_token = db.Column(db.String(120))
    id_token = db.Column(db.String(120))
    expires_in = db.Column(db.String(120))
    state = db.Column(db.String(120))
    token_type = db.Column(db.String(120))

    def __init__(self, code, access_token, refresh_token, id_token, expires_in, state, token_type):
        self.code = code
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.id_token = id_token
        self.expires_in = expires_in
        self.state = state
        self.token_type = 'Bearer'
