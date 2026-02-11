from app import create_app
from extensions import db
from models import User

app = create_app()

with app.app_context():
    user = User.query.filter_by(username="noc").first()
    if user:
        user.set_password("Lantai@6")
        db.session.commit()
        print("Password berhasil diubah!")
    else:
        print("User tidak ditemukan.")
