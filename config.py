
class BaseConfig():
    pass

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    EXPLAIN_TEMPLATE_LOADING=True

class ProductionConfig(BaseConfig):
    pass

configuration = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}