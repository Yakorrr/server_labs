from sqlalchemy import ForeignKey
from db import db


class AccountModel(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    balance = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship("UserModel", foreign_keys=user_id, back_populates="account")
