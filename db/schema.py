from app import ma

# Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('code', 'email', 'password')

class TokenSchema(ma.Schema):
    class Meta:
        fields = ('code', 'access_token', 'refresh_token', 'id_token', 'expires_in', 'state', 'token_type')

# Init Schemas

user_schema = UserSchema()
token_schema = TokenSchema()