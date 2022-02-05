import sys

from core.controllers import RunController


class CLI:

    @classmethod
    def main(cls):
        user_action = cls.asc_user_action()
        cls.run_controller(user_action)

    @staticmethod
    def run_controller(user_action: str):
        action_controllers = {
            'run': RunController,
        }
        try:
            action_controllers[user_action]().main()
        except KeyError:
            print('Incorrect value!')

    @classmethod
    def asc_user_action(cls):
        user_action = input('Your action (run/exit): ')
        if user_action == 'exit':
            print('Goodbye!')
            cls.exit()
        return user_action

    @staticmethod
    def exit():
        sys.exit(0)
