from flask_restplus import Resource

from app.main.util.dto import welcomeDto

api = welcomeDto.api
category_auth = welcomeDto.welcome


@api.route('/welcome', methods=['GET'])
class Welcome(Resource):
    @api.doc('Welcome API')
    def get(self):
        return "WelCome"
