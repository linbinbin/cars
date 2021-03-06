from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Resource, Api
socketio = SocketIO()
counter = 0
def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    Api(app).add_resource(main.controllapi.Controller,'/controller')
    socketio.init_app(app)
    return app
