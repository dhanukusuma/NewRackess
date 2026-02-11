from extensions import db
from datetime import datetime

class Fingerprint(db.Model):
    __tablename__ = "fingerprints"

    id = db.Column(db.Integer, primary_key=True)

    # sementara pakai nama petugas
    staff_name = db.Column(db.String(100), unique=True, nullable=False)

    # template fingerprint hasil enroll
    template = db.Column(db.Text, nullable=False)

    device = db.Column(db.String(50), default="MOCK")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
