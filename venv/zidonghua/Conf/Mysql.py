import pymysql
class MysqlConnectCom(object):

    def __init__(self, db, user, passwd, host, port=3306, charset='utf8'):
        self.db = db
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.charset = charset
        self.connect = None
        self.cursor = None

    def _connect_db(self):
        params = {
            "db": self.db,
            "user": self.user,
            "passwd": self.passwd,
            "host": self.host,
            "port": self.port,
            "charset": self.charset
        }
        self.connect = pymysql.connect(**params)
        self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)

    def _close_db(self):
        """
        关闭数据库
        """
        self.cursor.close()
        self.connect.close()

    def select_operation(self, sql):
        if not sql.upper().startswith('SELECT'):
            return Exception('sql not right!')
        try:
            self.cursor.execute(sql)
        except Exception as e:
            return e
        else:
            return self.cursor.fetchall()
        finally:
            self._connect_db()

    def insert_operation(self, sql):
        if not sql.upper().startswith('INSERT'):
            return Exception('sql not right!')
        try:
            count = self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            return False
        else:
            return count
        finally:
            self._connect_db()

    def update_operation(self, sql):
        if not sql.upper().startswith('UPDATE'):
            return Exception('sql not right!')
        try:
            count = self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            return False
        else:
            return count
        finally:
            self._connect_db()

    def delete_operation(self, sql):
        if not sql.upper().startswith('DELETE'):
            return Exception('sql not right!')
        try:
            count = self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            return False
        else:
            return count
        finally:
            self._connect_db()
