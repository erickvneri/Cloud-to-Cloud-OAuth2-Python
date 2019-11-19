from lib.app_dao import validate_client_id, validate_redirect_uri, validate_client_secret
import redis
session = redis.Redis()

#1 /oauth/authorize Endpoint Handler
def auth_verification(request):
    '''Request Query Params'''

    client_id = request.args.get('client_id')
    response_type = request.args.get('response_type')

    # Session values
    redirect_uri = request.args.get('redirect_uri')
    state = request.args.get('state') 
    session.mset({ "client_state": state, "redirect_uri": redirect_uri })

    # Validation
    if validate_client_id(client_id):
        if validate_redirect_uri(redirect_uri):
            if response_type == 'code':
                return True

        return False

    return False

#2 /login Endpoint Handler
def login_as_callback(request):
    '''User's Data Params'''
    from lib.app_dao import hash_it, create_token

    # User credentials
    email = request.args.get('email')
    password = hash_it(request.args.get('password'))
    expires_in = request.args.get('expires_in')
    # Session values
    client_state = session.get('client_state').decode('utf-8')
    redirect_uri = session.get('redirect_uri').decode('utf-8')

    # Redirection values
    code = create_token(email, password, expires_in, client_state)
    location = redirect_uri + '?' + 'code=' + code + '&state=' + client_state
    return location

#3 /oauth/token Endpoint Handler
def validate_token_callback(request):
    '''Token Callback Req Form-data'''

    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')
    grant_type = request.form.get('redirect_uri')

    # Requeset Validation
    if validate_client_id(client_id):
        if validate_client_secret(client_secret):
            return True
            
    return False