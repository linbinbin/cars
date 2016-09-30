from flask_restful import Resource
from flask import session
from flask_socketio import emit
from .. import socketio

class Controller(Resource):
    counter = 0
    def __init__(self):
        self.couter = 0
    def put(self):
        return {'Hello':'put'}
    def get(self):
        room = session.get('room')
        socketio.emit('message', {'msg': session.get('name') + ':' + str(self.counter)}, room=room, namespace='/')
        self.counter += 1
        return {'Get':'me'}
