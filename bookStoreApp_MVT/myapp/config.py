class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    UPLOAD_FOLDER = "D:\\Project\\Flask\\bookStoreApp_MVT\\app\\static\\bookImages\\"


class ProductionConfig(Config):
    DEBUG = False
    """postgresql://username:password@localhost:portnumber/database_name """
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:120699@localhost:5432/flask_db"
    UPLOAD_FOLDER = "D:\\Project\\Flask\\bookStoreApp_MVT\\app\\static\\bookImages\\"


AppConfig = {"dev": DevelopmentConfig, "prd": ProductionConfig}
