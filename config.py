def get_db_uri(dbinfo):
    engine = dbinfo.get('ENGINE')
    driver = dbinfo.get('DRIVER')
    userid = dbinfo.get('USER')
    pwd = dbinfo.get('PASSWORD')
    host = dbinfo.get('HOST')
    port = dbinfo.get('PORT')
    dbname = dbinfo.get('NAME')
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, userid, pwd, host, port, dbname)


class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'XXYYAABCD*@2SYXKD'


class DEVConfig(BaseConfig):
    DEBUG = True
    db_info = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'gz.1234',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'qianfeng'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + r'F:/Database_Files/sqlite/qianfeng.db'
    print('SQLALCHEMY_DATABASE_URI=' + SQLALCHEMY_DATABASE_URI)


class UATConfig(BaseConfig):
    DEBUG = True
    db_info = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'gz.1234',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'qianfeng'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


class PRODConfig(BaseConfig):
    DEBUG = False
    db_info = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'gz.1234',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'qianfeng'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


envs = {
    'dev': DEVConfig,
    'uat': UATConfig,
    'prod': PRODConfig
}
