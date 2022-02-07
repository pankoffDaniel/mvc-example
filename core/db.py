import sqlite3

from src.views import View


class Database:
    """The Database class for working with SQLite3."""

    def __enter__(self):
        """Initialize the database connection with the cursor."""
        self.connection = sqlite3.connect('db.sqlite')
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the cursor, and database connection.
        Commit if Exception is not raised,
        Rollback if Exception is raised.
        """
        self.cursor.close()
        if isinstance(exc_val, sqlite3.Error):
            View.print_text(f'Error: {exc_val}')
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def execute(self, sql: str):
        """Execute an SQL statement."""
        self.cursor.execute(sql)
