import GUPA

def run_complex_test():
    print '** GUPA Python Client Test **'
    # consumer key and secret granted by the GUPA
    consumer_key = 'XXXX'
    consumer_secret = 'XXXX'
    client = GUPA(consumer_key, consumer_secret)
    pause()

    # get request token
    print '* Obtain a request token ...'
    token = client.fetch_request_token()
    token = oauth.OAuthToken(token['oauth_token'],token['oauth_token_secret'])
    print 'GOT'
    print 'key: %s' % str(token.key)
    print 'secret: %s' % str(token.secret)
    pause()

    # authorize the token
    print '* Authorize the request token ...'
    request_token_key = client.authorize_token(token)
    token.key = request_token_key
    pause()

    # get access token
    print '* Obtain an access token ...'
    token = client.fetch_access_token(token)
    token = oauth.OAuthToken(str(token['oauth_token']),str(token['oauth_token_secret']))
    print 'GOT'
    print 'key: %s' % str(token.key)
    print 'secret: %s' % str(token.secret)
    pause()

    # access some protected resources
    print '* Access protected resources ...'
    # resource specific params
    parameters = {'point': 'POINT(1000.0 1000.0)', 'distance': '121.26', 'azimuth': '168.3460'}    
    params = client.access_resource(parameters, '/basic_calc/coord/')
    print 'response: %s' % params
    pause()

def run_simple_test():
    print '** GUPA Python Client Test **'
    # consumer key and secret granted by the GUPA
    consumer_key = 'XXXX'
    consumer_secret = 'XXXX'
    client = GUPAClient(consumer_key, consumer_secret)
    pause()
    # access some protected resources
    print '* Access protected resources ...'
    # resource specific params
    parameters = {'point': 'POINT(1000.0 1000.0)', 'distance': '121.26', 'azimuth': '168.3460'}    
    params = client.access_resource(parameters, '/basic_calc/coord/')
    print 'response: %s' % params
    pause()

def pause():
    print ''
    time.sleep(1)

if __name__ == '__main__':
    #run_complex_test()
    run_simple_test()
    print 'Done.'