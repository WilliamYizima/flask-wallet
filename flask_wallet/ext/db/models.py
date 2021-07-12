from flask_wallet.ext.db import db

class Receipts(db.Model):
    __tablename__ = "tb_receipts"
    id = db.Column("id", db.Integer, primary_key=True)
    receipts_value = db.Column("rec_value",db.Float)
    receipts_month = db.Column("rec_month",db.Integer)
    receipts_year = db.Column("rec_year",db.Integer)

    @staticmethod
    def add_receipts(receipts_value: float, receipts_month: int, receipts_year: int):
        receipts = Receipts(
            receipts_value=receipts_value,
            receipts_month=receipts_month,
            receipts_year=receipts_year)
        
        db.session.add(receipts)
        db.session.commit()