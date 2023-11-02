from flask import request, Blueprint, make_response, jsonify
from app.celery_config.celery_tasks import send_emails
from flask_restful import Resource
from app import api

send_mails = Blueprint('registerblue', __name__)


class SendMail(Resource):
    def post(self):
    # try:
        email = request.json.get("email")
        if email:
            send_emails.delay(email)
            return make_response(jsonify({"message": f"email has been sent successfully to {email}"}))
        else:
            return make_response(jsonify({"message": f"email not security"}))
    # except Exception as e:
    #     return str(e)


api.add_resource(SendMail, "/user/sendmail")
