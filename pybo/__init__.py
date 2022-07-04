from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


# app = Flask(__name__)  # 플라스크 애플리케이션 생성코드, __name__에 모듈명 담김(pybo)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    # @app.route('/')  # url 매핑해 다음줄 함수 실행
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    return app
