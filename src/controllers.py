from .views import View
from .services import get_data


class Controller:
    """The Controller class to get and show some data."""

    @classmethod
    def __init__(cls):
        cls.main()

    @classmethod
    def main(cls):
        """The main logic of the Controller."""
        result = get_data()
        cls.run_view(result)

    @classmethod
    def run_view(cls, result):
        View.print_text(result)
