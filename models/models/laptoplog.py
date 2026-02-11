# models/laptoplog.py
from datetime import datetime
from extensions import db

class LaptopLog(db.Model):
    __tablename__ = "laptop_logs"

    id = db.Column(db.Integer, primary_key=True)

    # Ticket MBS (opsional)
    ticket_mbs = db.Column(db.String(50), nullable=True)

    # Data peminjam
    borrower_name = db.Column(db.String(100), nullable=False)
    borrower_division = db.Column(db.String(100), nullable=False)
    purpose = db.Column(db.String(255), nullable=False)  # keperluan singkat

    # Identitas laptop
    laptop_name = db.Column(db.String(100), nullable=False)

    # Waktu
    time_out = db.Column(db.DateTime)  # waktu laptop diberikan ke peminjam
    time_in = db.Column(db.DateTime)   # waktu laptop dikembalikan
    planned_return_date = db.Column(db.Date)  # rencana kembali (itungan hari)

    status = db.Column(db.String(20), default="borrowed")  # borrowed / returned

    # TTD saat PINJAM (keluar dari NOC)
    signature_out_borrower = db.Column(db.Text)  # peminjam pas ambil
    signature_out_staff = db.Column(db.Text)     # petugas pas serahkan
    staff_out_name = db.Column(db.String(100))   # nama petugas saat PINJAM

    # TTD saat KEMBALI (masuk ke NOC)
    signature_in_borrower = db.Column(db.Text)   # peminjam pas kembalikan
    signature_in_staff = db.Column(db.Text)      # petugas saat terima
    staff_in_name = db.Column(db.String(100))    # nama petugas saat KEMBALI

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
