
from app import flask_app
from app.master.views import send_mails
flask_app.register_blueprint(send_mails)

if __name__ == "__main__":
    flask_app.run(debug=True, port=5000)
