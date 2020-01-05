import sqlite3
import os.path

class SqlLiteDbUtility(object):
    connection = None
    @classmethod
    def get_connection(cls):
        if not SqlLiteDbUtility.connection:
            db_path = os.path.join(os.path.dirname(__file__), '..', 'farsnet2.5.db3')
            SqlLiteDbUtility.connection = sqlite3.connect(db_path)
            SqlLiteDbUtility.connection.row_factory = sqlite3.Row
        return SqlLiteDbUtility.connection

