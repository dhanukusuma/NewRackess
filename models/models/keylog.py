from datetime import datetime
from extensions import db


class KeyLog(db.Model):
    __tablename__ = "key_logs"

    id = db.Column(db.Integer, primary_key=True)
    ticket_mbs = db.Column(db.String(50), nullable=False)
    visitor_name = db.Column(db.String(100), nullable=False)
    visitor_company = db.Column(db.String(100))
    rack_location = db.Column(db.String(100), nullable=False)

    time_in = db.Column(db.DateTime)
    time_out = db.Column(db.DateTime)

    status = db.Column(db.String(20), default="borrowed")

    # === Fingerprint reference (NEW) ===
    borrower_fp_id = db.Column(db.Integer, nullable=True)
    staff_in_fp_id = db.Column(db.Integer, nullable=True)
    staff_out_fp_id = db.Column(db.Integer, nullable=True)

    # TTD saat PINJAM
    signature_in_visitor = db.Column(db.Text)
    signature_in_staff = db.Column(db.Text)
    staff_in_name = db.Column(db.String(100))

    # TTD saat KEMBALI
    signature_out_visitor = db.Column(db.Text)
    signature_out_staff = db.Column(db.Text)
    staff_out_name = db.Column(db.String(100))

    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
