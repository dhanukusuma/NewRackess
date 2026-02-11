from datetime import datetime
from extensions import db


class ActivityLog(db.Model):
    __tablename__ = "activity_logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    action = db.Column(db.String(100), nullable=False)  # e.g. "borrow_key", "return_laptop"
    entity_type = db.Column(db.String(50))              # "key", "laptop"
    entity_id = db.Column(db.Integer)                   # id dari keylog/laptoplog
    details = db.Column(db.Text)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
