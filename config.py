import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "RAHASIA_GUE_RACKESS"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///rackess.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

FINGERPRINT_MODE = "MOCK"

