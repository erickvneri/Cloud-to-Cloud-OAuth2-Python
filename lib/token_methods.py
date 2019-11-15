import secrets

# Token Methods
def create_token(email, password, expires_in, client_state):
    '''Create SmartThings C2C Interactions' Token'''
    from db.db import db, User, Token

    code = 'C-' + secrets.token_hex(15)
    access_token = 'AT-' + secrets.token_hex(15)
    refresh_token = 'RT-' + secrets.token_hex(15)
    id_token = 'IDT-' + secrets.token_hex(15)
    state = client_state
    token_type = 'Bearer'
   
    # Database New Values
    token = Token(code, access_token, refresh_token, id_token, expires_in, state, 'Bearer')
    new_user = User(code, email, password)
    # Inserts queries
    db.session.add(new_user)
    db.session.add(token)
    db.session.commit()
    return code


def get_token(code, grant_type):
    '''Retrieve Token to ST'''
    from db.db import Token
    from db.schema import token_schema

    # Token Queries
    if grant_type == 'authorization_code':
        token = Token.query.filter_by(code=code).first()
        return token_schema.jsonify(token)

    elif grant_type == 'refresh_token':
        refreshed_token = refresh_token(code)
        return refreshed_token


def refresh_token(code):
    '''Refresh Token to ST'''
    from db.db import Token, db
    from db.schema import token_schema

    # DB Operations
    refreshed_token = Token.query.filter_by(code=code).first()
    refreshed_token.access_token = 'AT-' + secrets.token_hex(15)
    refreshed_token.refresh_token = 'RT-' + secrets.token_hex(15)
    refreshed_token.id_token = 'IDT-' + secrets.token_hex(15)
    db.session.commit()

    return token_schema.jsonify(refreshed_token)

