class Config(object):
    API_URL = ''
    DEBUG = False
    SECRET_KEY = "167d4848233d5db21725b1cc042f50fe"
    TESTING = False


class ProductionConfig(Config):
    API_URL = 'http://ec2-54-184-147-64.us-west-2.compute.amazonaws.com:8080/shopped-api/api/v1'


class DevelopmentConfig(Config):
    API_URL = 'http://localhost:8080/api/v1'
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    API_URL = 'localhost'
    DEBUG = True
