from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.sql import func

from db import db
from models import UserModel, CategoryModel


class RecordModel(db.Model):
    __tablename__ = "record"

    ID = db.Column(db.Integer, primary_key=True)

    User_ID = db.Column(
        db.Integer,
        ForeignKey("user.ID", ondelete="CASCADE"),
        unique=False,
        nullable=False
    )

    Category_ID = db.Column(
        db.Integer,
        ForeignKey("category.ID", ondelete="CASCADE"),
        unique=False,
        nullable=False
    )

    Date = db.Column(db.TIMESTAMP, server_default=func.now())
    Amount = db.Column(db.Float(precision=2), unique=False, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            (User_ID,), ("user.ID",),
        ),
        ForeignKeyConstraint(
            (Category_ID,), ("category.ID",),
        ),
    )

    user = db.relationship(UserModel, foreign_keys=User_ID, back_populates="record")
    category = db.relationship(CategoryModel, foreign_keys=Category_ID, back_populates="record")
