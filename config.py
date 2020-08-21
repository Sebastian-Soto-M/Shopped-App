class Config(object):
    DEBUG = False
    SECRET_KEY = "167d4848233d5db21725b1cc042f50fe"
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
