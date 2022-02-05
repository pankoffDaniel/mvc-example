import sys

from core.controllers import \
    RunController, \
    ErrorController, \
    AnotherController


class CLI:

    @classmethod
    def __init__(cls):
        cls.main()

    @classmethod
    def main(cls):
        user_action = cls.asc_user_action()
        cls.run_controller(user_action)

    @classmethod
    def run_controller(cls, user_action: str):
        action_controllers = {
            'run': RunController,
            'another_function': AnotherController(),
        }
        try:
            action_controllers[user_action]()
        except KeyError:
            ErrorController('Incorrect Value')

    @classmethod
    def asc_user_action(cls):
        user_action = input('Your action (run/exit): ')
        if user_action == 'exit':
            sys.exit(0)
        return user_action
