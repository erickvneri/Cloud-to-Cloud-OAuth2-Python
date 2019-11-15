from app import app

BASE_URI = 'https://33db2dd8.ngrok.io'
print('\n * SMARTTHINGS APP CONFIG.')
print(' * CLIENT_ID:       sdfhufidsai845f645fdsa')
print(' * CLIENT_SECRET:   Magic is Real')
print(' * TARGET_URI:     ', BASE_URI)
print(' * OAUTH_URI:      ', BASE_URI + '/oauth/authorize')
print(' * TOKEN_URI:      ', BASE_URI + '/oauth/token\n')

if __name__ == '__main__':    
    # app.debug = True
    app.run(host='127.0.0.1', port=3000)
