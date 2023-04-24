from dotenv import dotenv_values

envs = dotenv_values(".env")

SQLALCHEMY_DATABASE_URI = envs['DATABASE_URI']

SECRET_KEY = envs['SECRET_KEY']

mail_setting = {
    'MAIL_SERVER':  envs['MAIL_SERVER'],
    'MAIL_PORT': int(envs['MAIL_PORT']),
    'MAIL_USE_TLS': True,
    #bool(envs['MAIL_USE_TLS']),
    'MAIL_USE_SSL': False,
    #bool(envs['MAIL_USE_SSL']),
    'MAIL_USERNAME': envs['MAIL_USERNAME'],
    'MAIL_PASSWORD': envs['MAIL_PASSWORD']
}
