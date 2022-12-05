from sqlalchemy import ForeignKey
from db import db


class AccountModel(db.Model):
    __tablename__ = "account"

    ID = db.Column(db.Integer, primary_key=True)

    User_ID = db.Column(
        db.Integer,
        ForeignKey("user.ID", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    Balance = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship("UserModel", foreign_keys=User_ID, back_populates="account")
