from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from db import db


class RecordModel(db.Model):
    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        unique=False,
        nullable=False
    )

    category_id = db.Column(
        db.Integer,
        ForeignKey("category.id", ondelete="CASCADE"),
        unique=False,
        nullable=False
    )

    date = db.Column(db.TIMESTAMP, server_default=func.now())
    amount = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship("UserModel", foreign_keys=user_id, back_populates="record")
    category = db.relationship("CategoryModel", foreign_keys=category_id, back_populates="record")
