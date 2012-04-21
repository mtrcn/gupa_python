import httplib
import time
import oauth
import json
import webbrowser
import sys

class GUPA(oauth.OAuthClient):

    #GUPA server URL and its version
    SERVER = 'gupa.geomatikuygulamalar.com'
    VERSION = 'v1'
    
    #GUPA OAUTH service urls
    REQUEST_TOKEN_URL = 'http://'+SERVER+'/'+VERSION+'/oauth/request_token'
    ACCESS_TOKEN_URL = 'http://'+SERVER+'/'+VERSION+'/oauth/access_token'
    AUTHORIZATION_URL = 'http://'+SERVER+'/'+VERSION+'/oauth/authorize'

    def __init__(self, consumer_key, consumer_secret):
        self.connection = httplib.HTTPConnection(GUPA.SERVER)
        self.consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)

    def fetch_request_token(self):
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(self.consumer, callback=None, http_url=GUPA.REQUEST_TOKEN_URL)
        oauth_request.sign_request(oauth.OAuthSignatureMethod_PLAINTEXT(), self.consumer, None)
        #print 'REQUEST (via headers)'
        #print 'parameters: %s' % str(oauth_request.parameters)
        self.connection.request('POST', GUPA.REQUEST_TOKEN_URL, headers=oauth_request.to_header()) 
        response = self.connection.getresponse()
        return json.loads(response.read())

    def fetch_access_token(self, token):
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(self.consumer, token=token, http_url=GUPA.ACCESS_TOKEN_URL)
        oauth_request.sign_request(oauth.OAuthSignatureMethod_PLAINTEXT(), self.consumer, token)
        #print 'REQUEST (via headers)'
        #print 'parameters: %s' % str(oauth_request.parameters)
        self.connection.request('POST', GUPA.ACCESS_TOKEN_URL, headers=oauth_request.to_header()) 
        response = self.connection.getresponse()
        return json.loads(response.read())

    def authorize_token(self, oauth_token):
        oauth_request = oauth.OAuthRequest.from_token_and_callback(token=oauth_token, http_url=GUPA.AUTHORIZATION_URL)
        #print 'REQUEST (via url query string)'
        #print 'parameters: %s' % str(oauth_request.parameters)
        webbrowser.open(oauth_request.to_url(),new=2)
        print "Enter PIN:"
        return sys.stdin.readline().strip("\r\n")

    def access_resource(self, parameters, service_path):
        headers = {'Content-Type' :'application/x-www-form-urlencoded'}
        service_url = 'http://'+GUPA.SERVER+'/'+GUPA.VERSION+service_path
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(self.consumer, http_method='POST', http_url=service_url, parameters=parameters)
        oauth_request.sign_request(oauth.OAuthSignatureMethod_PLAINTEXT(), self.consumer, None)
        #print 'REQUEST (via post body)'
        #print 'parameters: %s' % str(oauth_request.parameters)
        self.connection.request('POST', service_url, body=oauth_request.to_postdata(), headers=headers)
        response = self.connection.getresponse()
        return response.read()
