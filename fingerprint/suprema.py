# fingerprint/suprema.py
from .base import FingerprintService

class SupremaFingerprintService(FingerprintService):

    def connect(self):
        # nanti isi SDK asli
        return True

    def enroll(self, user_id):
        raise NotImplementedError("Suprema enroll not implemented yet")

    def verify(self, user_id):
        raise NotImplementedError("Suprema verify not implemented yet")
