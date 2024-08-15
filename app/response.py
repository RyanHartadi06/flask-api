from flask import jsonify, make_response

def success(values, message):
  res = {
    'message': message,
    'values': values
  }
  return make_response(jsonify(res), 200)

def bad_request(values, message):
  res = {
    'message': message,
    'values': values
  }
  return make_response(jsonify(res), 400)