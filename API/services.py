import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()

def find_book(params={}):
    response = generate_request('https://www.etnassoft.com/api/v1/get/', params)
    if response:
       return response
    return ''