from requests import get, exceptions


class Genderize:
    ENDPOINT = 'https://api.genderize.io'

    def __init__(self, name):
        self.name = name
        self.data = self.get_data()
        self.gender = self.data.get('gender', '')
        self.probability = self.data.get('probability')

    def get_data(self):
        try:
            response = get(Genderize.ENDPOINT, params={'name': self.name})
            return response.json()
        except exceptions.RequestException:
            return {}
