from flask import Flask
from flask import request,jsonify
from service.messageService import MessageService
import json
import jsonpickle
import os
app=Flask(__name__)
app.config.from_pyfile('config.py')
messageService=MessageService()
@app.route('/v1/ds/message/',methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = messageService.process_message(message)
    if  result is not None:
        serialized_Result=result.serialize()
        return jsonify(serialized_Result)
    else:
        return jsonify({'error' : 'Invalid mssg format'}), 400
@app.route('/',methods=['GET'])
def handle_get():
    print("Hello World")
if __name__ == "__main__":
    app.run(host="localhost",port=8000,debug=True)