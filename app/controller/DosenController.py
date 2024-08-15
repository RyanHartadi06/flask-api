from app.model.dosen import Dosen

from app import response, app, db
from flask import request

def index(): 
  try: 
    dosen = Dosen.query.all()
    data = formatarray(dosen)
    return response.success(data, "success")
  except Exception as e:
    print(e)
    return response.bad_request([], "bad request")

def formatarray(datas):
  array = []
  for i in datas:
    array.append(singleObject(i))
  return array

def singleObject(data):
  data = {
    'id': data.id,
    'nidn': data.nidn,
    'name': data.name,
    'phone': data.phone,
    'address': data.address,
  }
  return data