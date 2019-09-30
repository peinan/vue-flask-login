from config import *
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from views.auth import *
from views.hello import *

# API設定
app = Flask(__name__)
jwt = JWTManager(app)
CORS(app)
app.config['SECRET_KEY'] = 'hello'

# views読み込み
app.register_blueprint(auth)
app.register_blueprint(hello)

if __name__ == "__main__":
    app.run(debug=True)
