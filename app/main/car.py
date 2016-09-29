from flask_restful import Resource, Api
class controller(Resource):
    def __init__(self):
        pass;

    def put(self):
        return {'Hello':'put'}

    def get(self):
        app.logger.debug('controller get() ')
        return {'Get':'me'}