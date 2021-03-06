import pymysql


class BaseConfig(object):
    SECRET_KEY = '5905f8795addbeeb0d38c8532ffff5e8'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    """
    开发环境
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/jobplus?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'developemt': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
