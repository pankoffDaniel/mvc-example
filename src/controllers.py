from .views import View


class Controller:
    """The Controller class to get and show some data."""

    @classmethod
    def __init__(cls):
        cls.main()

    @classmethod
    def main(cls):
        """The main logic of the Controller."""
        result = 'Some result data'
        cls.run_view(result)

    @classmethod
    def run_view(cls, result):
        View.print_text(result)
