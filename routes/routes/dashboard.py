from flask import Blueprint, render_template
from flask_login import login_required
from models import KeyLog, LaptopLog

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
@login_required
def index():
    total_key_borrowed = KeyLog.query.filter_by(status="borrowed").count()
    total_laptop_borrowed = LaptopLog.query.filter_by(status="borrowed").count()

    last_key_logs = KeyLog.query.order_by(KeyLog.created_at.desc()).limit(5).all()
    last_laptop_logs = LaptopLog.query.order_by(LaptopLog.created_at.desc()).limit(5).all()

    return render_template(
        "dashboard.html",
        total_key_borrowed=total_key_borrowed,
        total_laptop_borrowed=total_laptop_borrowed,
        last_key_logs=last_key_logs,
        last_laptop_logs=last_laptop_logs,
    )
