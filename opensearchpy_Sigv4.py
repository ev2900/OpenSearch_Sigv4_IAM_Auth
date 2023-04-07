from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth # pip install opensearch-py
import boto3

host = '<host_url>' # ex. search-opensearch-demo-basic-auth-tf2ubrkbsq63l3fjpycipkd364.us-east-1.es.amazonaws.com
region = '<region>' # ex. us-east-1

credentials = boto3.Session(profile_name='os-profile').get_credentials()

auth = AWSV4SignerAuth(credentials, region)

index_name = 'movies'

client = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

# Add a document to the index.
document = {
  'title': 'Moneyball',
  'director': 'Bennett Miller',
  'year': '2011'
}
id = '1'

response = client.index(
    index = index_name,
    body = document,
    id = id,
    refresh = True
)

print(response)