from flask import Blueprint, request, jsonify
from flask_login import login_required
from fingerprint.factory import get_fingerprint_service
from models import Fingerprint
from extensions import db

fingerprint_bp = Blueprint("fingerprint", __name__, url_prefix="/fingerprint")


@fingerprint_bp.route("/enroll", methods=["POST"])
@login_required
def enroll_fingerprint():
    staff_name = (request.form.get("staff_name") or "").strip()
    if not staff_name:
        return {"error": "staff_name required"}, 400

    # cek sudah pernah enroll belum
    if Fingerprint.query.filter_by(staff_name=staff_name).first():
        return {"error": "Fingerprint already enrolled"}, 400

    fp = get_fingerprint_service()
    result = fp.enroll(staff_name)

    record = Fingerprint(
        staff_name=staff_name,
        template=result["template"],
        device=result.get("device", "MOCK"),
    )
    db.session.add(record)
    db.session.commit()

    return {"message": "Fingerprint enrolled", "staff": staff_name}
