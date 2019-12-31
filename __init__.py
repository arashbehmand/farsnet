import sqlite3
import os
from .service.SenseService import SenseService
from .service.SynsetService import SynsetService

__all__ = ["sense_service", "synset_service"]

_db_path = os.path.join(os.path.dirname(__file__), 'farsnet2.5.db3')
_con = sqlite3.connect(_db_path)
_con.row_factory = sqlite3.Row

sense_service = SenseService(_con)
synset_service = SynsetService(_con)