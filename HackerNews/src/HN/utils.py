import requests

def getting_data(url_id):
    r = requests.get('http://hn.algolia.com/api/v1/items/' + str(url_id))
    data = r.json()
    return data

def getting_sentiments(title):
    headers = {'X-AYLIEN-TextAPI-Application-Key':'144f2613e81e476e4af26b5ac92a0218','X-AYLIEN-TextAPI-Application-ID':'a99d2bc6'}
    r = requests.get('https://api.aylien.com/api/v1/sentiment?text=' + str(title), headers=headers)
    data = r.json()
    return data
