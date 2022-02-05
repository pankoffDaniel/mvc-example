from core.views import View
from services import get_search_data


class RunController:

    def __init__(self):
        self.view = View()
        self.main()

    def main(self):
        result = get_search_data()
        self.run_view(result)

    def run_view(self, result):
        self.view.show_result_message(result)


class ErrorController:

    def __init__(self, message: str):
        self.message = message
        self.view = View()
        self.main()

    def main(self):
        self.run_view()

    def run_view(self):
        self.view.show_error_message(self.message)


class AnotherController:
    pass
