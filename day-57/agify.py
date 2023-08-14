from requests import get, exceptions


class Agify:
    ENDPOINT = 'https://api.agify.io'

    def __init__(self, name):
        self.name = name
        self.data = self.get_data()
        self.age = self.data.get('age')

    def get_data(self):
        try:
            response = get(Agify.ENDPOINT, params={'name': self.name})
            return response.json()
        except exceptions.RequestException:
            return {}
