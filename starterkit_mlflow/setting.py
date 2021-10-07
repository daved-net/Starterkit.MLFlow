import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Setting(object):
    EXPERIMENT_NAME = 'example-dev'
    EXPERIMENT_VERSION = '0.0.1'
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.environ['DATABASE_URL']
    DATASET_FILEPATH =  os.path.join(basedir,'example_data/boston_housing.csv')


class ProductionSetting(Setting):
    DEBUG = False


class StagingSetting(Setting):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentSetting(Setting):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False


class TestingSetting(Setting):
    TESTING = True