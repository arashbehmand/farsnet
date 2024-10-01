"""
The `SqlLiteDbUtility` class provides a utility for managing SQLite database connections in Python.
"""

import sqlite3
import os.path


class SqlLiteDbUtility:
    """
    A utility class for managing the SQLite database connection.
    """

    connection = None

    @classmethod
    def get_connection(cls):
        """
        Retrieves the SQLite database connection.
        Creates a new connection if one doesn't already exist.

        Returns:
            sqlite3.Connection: The SQLite database connection.
        """
        if cls.connection is None:
            db_path = os.path.join(
                os.path.dirname(__file__), "../farsnet2.5.db3"
            )
            cls.connection = sqlite3.connect(db_path)
            cls.connection.row_factory = sqlite3.Row
        return cls.connection
