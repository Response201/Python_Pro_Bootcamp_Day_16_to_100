import requests

def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def post_data(url, headers=None, params=None):

    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    print(response)


def put_data(url, headers=None, params=None):
    response = requests.put(url, headers=headers, json=params)
    response.raise_for_status()
    print(response)

def delete_data(url, headers=None):
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    print(response)