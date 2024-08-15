from app import db
from datetime import datetime


class Dosen(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  name = db.Column(db.String(250), nullable=False)
  nidn = db.Column(db.String(250), nullable=False)
  phone = db.Column(db.String(250), nullable=False)
  address = db.Column(db.String(250), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
      return '<Doseb {}>'.format(self.name)