import sqlite3

from core.db import Database


class ConfigModel:
    """Model of user config."""

    db = Database()

    @classmethod
    def create_config_table(cls, db: Database):
        """Create empty config table."""
        sql = """
        CREATE TABLE config (
            token    VARCHAR(255) NOT NULL,
            language VARCHAR(255) DEFAULT 'en' NOT NUll
        );"""
        db.execute(sql)

    @classmethod
    def is_config_exists(cls) -> bool:
        """Return True if config exists, or else - False."""
        with cls.db as db:
            try:
                db.execute('SELECT EXISTS(SELECT * FROM config);')
            except sqlite3.OperationalError:  # case when table doest not exist
                cls.create_config_table(db)
                return False
            return True if db.cursor.fetchone()[0] else False

    @classmethod
    def remove_config(cls):
        """Remove config data."""
        sql = 'DELETE FROM config WHERE TRUE;'
        with cls.db as db:
            db.execute(sql)

    @classmethod
    def configure(cls, token: str, language: str):
        """Configure user data in the Database."""
        if cls.is_config_exists():
            cls.remove_config()
        sql = """
        INSERT INTO config(token, language) VALUES('{token}', '{language}');
        """.format(token=token, language=language)
        with cls.db as db:
            db.execute(sql)
