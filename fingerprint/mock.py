from .base import FingerprintService
from models import Fingerprint
from extensions import db
from datetime import datetime
import uuid

class MockFingerprintService(FingerprintService):

    def connect(self):
        return True

    def enroll(self, staff_name):
        # simpan ke DB (mock tapi real behavior)
        record = Fingerprint(
            staff_name=staff_name,
            template=f"MOCK-{uuid.uuid4()}",
            device="MOCK",
            created_at=datetime.utcnow(),
        )
        db.session.add(record)
        db.session.commit()

        return {
            "success": True,
            "fingerprint_id": record.id,
            "device": record.device,
        }

    def verify(self, staff_name):
        record = Fingerprint.query.filter_by(staff_name=staff_name).first()

        if not record:
            return {
                "matched": False,
                "reason": "Fingerprint not enrolled",
            }

        return {
            "matched": True,
            "fingerprint_id": record.id,
            "device": record.device,
        }
