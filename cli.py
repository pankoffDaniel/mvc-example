import sqlite3
import sys

from src.controllers import Controller
from src.views import View
from core.db import Database


class CLI:
    """The CLI class for user to manage program."""

    interfaces = {
        'config_exists': {
            '1': 'Start',
            '2': 'Configure',
            '3': 'Exit',
        },
        'config_not_exists': {
            '1': 'Configure',
            '2': 'Exit',
        },
    }
    db = Database()

    @classmethod
    def __init__(cls):
        cls.main()

    @classmethod
    def get_interface(cls) -> dict:
        """Return the interface in depending on the config."""
        if cls.is_config_exists():
            return cls.interfaces['config_exists']
        return cls.interfaces['config_not_exists']

    @classmethod
    def configure(cls):
        """Configure user data in the Database."""
        pass

    @classmethod
    def start_user_action(cls, user_action: str):
        action_methods = {
            'Start': Controller,
            'Configure': cls.configure,
            'Exit': cls.exit,
        }
        action_methods[user_action]()

    @classmethod
    def main(cls):
        """The main logic of the CLI."""
        interface = cls.get_interface()
        View.print_interface(interface)
        user_action = cls.ask_user_action(interface)
        if user_action:
            cls.start_user_action(user_action)

    @classmethod
    def is_config_exists(cls) -> bool:
        """Return True if config exists, or else - False."""
        with cls.db as db:
            try:
                db.execute('SELECT EXISTS(SELECT * FROM config LIMIT 1)')
            except sqlite3.OperationalError:  # case when table doest not exist
                return False
            return db.cursor.fetchone()[0]

    @classmethod
    def exit(cls):
        View.print_text('Goodbye!')
        sys.exit(0)

    @classmethod
    def ask_user_action(cls, interface: dict):
        user_action = input('Your action: ')
        try:
            return interface[user_action]
        except KeyError:
            View.print_text('Incorrect command!')
