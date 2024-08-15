from app import db
from datetime import datetime
from app.model.dosen import Dosen

class Mahasiswa(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  nim = db.Column(db.String(250), nullable=False)
  name = db.Column(db.String(250), nullable=False)
  phone = db.Column(db.String(250), nullable=False)
  address = db.Column(db.String(250), nullable=False)
  dosen_satu = db.Column(db.BigInteger, db.ForeignKey(Dosen.id), nullable=False)
  dosen_dua = db.Column(db.BigInteger, db.ForeignKey(Dosen.id), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
      return '<Mahasiswa {}>'.format(self.name)