# -*- coding: utf-8 -*-

"""
连接数据库

"""
import pymysql
from Common import Log
class connMysql:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host='gz-cdb-pqp4a8vn.sql.tencentcdb.com',port=62331,user = "chenshuze",passwd = "5de09f9fb50f", charset='utf8')
            self.cursor = self.connection.cursor()
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_data(self, sql_code, count=0):
        print(sql_code)
        # sql_code = 'select employee.pin,employee.emp_name,iclock.sn,area.area_name from transaction, employee, iclock, area where transaction.employee_id=employee.id and transaction.iclock_id=iclock.id and iclock.area_id=area.id;'
        self.cursor.execute(sql_code)
        if int(count):
            return self.cursor.fetchmany(count)
        else:
            return self.cursor.fetchall()



    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        # print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.cursor.close()
        self.connection.close()







