from core.models import Model
from api.api import API


def get_search_data():
    Model.do_something_start()
    result = API.get_search_data()
    Model.do_something_finish()
    return result
