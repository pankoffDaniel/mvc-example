class View:
    """The View class to print data."""

    @staticmethod
    def print_text(text: str):
        print(text)

    @staticmethod
    def print_interface(interface: dict):
        for number, action in interface.items():
            print(f'{number}. {action}')
