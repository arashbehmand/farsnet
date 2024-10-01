from .service.SenseService import SenseService
from .service.SynsetService import SynsetService

__all__ = ["sense_service", "synset_service"]

sense_service = SenseService()
synset_service = SynsetService()
