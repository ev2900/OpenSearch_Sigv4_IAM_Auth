from requests_aws4auth import AWS4Auth
import boto3
import requests

host = '<host_url>'.rstrip('/') # ex. search-opensearch-demo-basic-auth-tf2ubrkbsq63l3fjpycipkd364.us-east-1.es.amazonaws.com
path = '<api_path>'.strip('/') # movies/_doc
region = '<region>' # ex. us-east-1

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

url = host + '/' + path + '/'

# The JSON body to accompany the request (if necessary)
payload = {
    'title': 'Moneyball',
    'director': 'Bennett Miller',
    'year': '2011'
}

r = requests.post(url, auth=awsauth, json=payload) # requests.get, post, and delete have similar syntax

print(r.text)