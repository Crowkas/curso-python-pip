import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()

    for i in categories:
        print(i['id'])
        print(i['name'])
        print(i['image'])
        print(i['creationAt'])
        print(i['updatedAt'])

