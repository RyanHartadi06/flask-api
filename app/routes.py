from app import app
from app.controller import DosenController


@app.route('/')
def index(): 
    return "Hello, s!"

@app.route('/dosen', methods=['GET'])
def dosen():
    return DosenController.index()
