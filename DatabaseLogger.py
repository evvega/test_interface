from LoggerInterface import ImplementLogger
import psycopg2

DB_HOST = ''
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = '####'
DB_PORT = '5432'


class DatabaseLogger(ImplementLogger):

    def connectar(self, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT):
        connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER,
                                      password=DB_PASSWORD, port=DB_PORT)
        return connection

    def log(self, msg: str):
        connection = self.connectar(DB_HOST=DB_HOST, DB_NAME=DB_NAME, DB_USER=DB_USER, DB_PASSWORD=DB_PASSWORD, DB_PORT=DB_PORT)
        cur = connection.cursor()
        sql_statement = "INSERT INTO test_interface (id, dato)VALUES (%s, %s)"

        cur.execute(sql_statement, (1, msg))
        connection.commit()
        count = cur.rowcount
        print(sql_statement, count)
