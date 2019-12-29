import sqlite3
import os
from . import Sense
from . import Synset

__all__ = ["sense", "synset"]

_db_path = os.path.join(os.path.dirname(__file__), 'farsnet2.5.db3')
_con = sqlite3.connect(_db_path)

sense = Sense.SenseService(_con)
synset = Synset.SynsetService(_con)