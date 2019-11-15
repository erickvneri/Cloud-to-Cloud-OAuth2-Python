# Validate OAuth Methods
def validate_client_id(client_id):
    CLIENT_ID = 'sdfhufidsai845f645fdsa'
    if client_id == CLIENT_ID:
        return True
    
    return False

def validate_redirect_uri(redirect_uri):
    PERMITED_REDIRECT_URI = 'https://c2c-us.smartthings.com/oauth/callback,https://c2c-eu.smartthings.com/oauth/callback,https://c2c-ap.smartthings.com/oauth/callback'
    if redirect_uri in PERMITED_REDIRECT_URI.split(','):
        return True
    
    return False

def validate_client_secret(client_secret):
    CLIENT_SECRET = 'Magic is Real'
    if client_secret == CLIENT_SECRET:
        return True

    return False

# Hashing Passwords Method
def hash_it(password):
    import random, string, secrets

    password_hashed = password + secrets.token_hex(5)
    chars = string.ascii_lowercase
    return (password_hashed.join(random.choice(chars) for i in range(3)))

