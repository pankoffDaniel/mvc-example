from os import getenv


class API:
    URL = getenv('URL')
    TOKEN = getenv('TOKEN')

    @classmethod
    def get_search_data(cls):
        return 'Some data'
