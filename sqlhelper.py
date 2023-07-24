from dbutils.pooled_db import PooledDB
import pymysql
from config import *


class MySqlHelper(object):
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            blocking=True,
            ping=0,
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PWD,
            database=DB_BASE,
            charset='utf8'
        )
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor()

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()
