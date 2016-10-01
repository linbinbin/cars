from flask_restful import Resource
from flask import session
from flask_socketio import emit
from .. import socketio
counter = 0
class Controller(Resource):
    def __init__(self):
        pass
    def put(self):
        return {'Hello':'put'}
    def get(self):
        global counter
        room = session.get('room')
        socketio.emit('message', {'msg': session.get('name') + ':' + str(counter)}, room=room, namespace='/')
        counter += 1
        return {'Get':'me'+str(counter)}
