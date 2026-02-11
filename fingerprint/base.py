# fingerprint/base.py
from abc import ABC, abstractmethod

class FingerprintService(ABC):

    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def enroll(self, user_id: int) -> dict:
        pass

    @abstractmethod
    def verify(self, user_id: int) -> dict:
        pass
