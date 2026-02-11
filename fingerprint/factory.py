# fingerprint/factory.py
from config import FINGERPRINT_MODE
from .mock import MockFingerprintService
from .suprema import SupremaFingerprintService

def get_fingerprint_service():
    if FINGERPRINT_MODE == "SUPREMA":
        return SupremaFingerprintService()
    return MockFingerprintService()
