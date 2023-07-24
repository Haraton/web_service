DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'cvml'
DB_PWD = 'cvml123456'
DB_BASE = 'data'

SECRET_KEY = 'esda412vr3fe34'
try:
    from localsettings import *
except ImportError:
    pass
