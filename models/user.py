from db import db


class UserModel(db.Model):
    __tablename__ = "user"

    ID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(256), unique=True, nullable=False)

    record = db.relationship(
        "RecordModel",
        back_populates="user",
        lazy="dynamic",
    )

    account = db.relationship(
        "AccountModel",
        back_populates="user",
        lazy="dynamic",
    )
