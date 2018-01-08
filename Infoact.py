# -coding:utf-8

import pymysql
from information import *

class Infoact:
    def getCon(self):
        conn = pymysql.connect(host="59.77.36.1", port=22, user="root",
                               password="NMRdaixie123", db="", charset="utf8")

        return conn

    def insertInfo(self, info):
        '''
            #插入
        :param info: 待插入对象
        :return:
        '''

        #insert sql
        sql = 'insert into information(iid, typel, title, author, corauthor, dates, disease,' \
              'symptom, acupoint, location, annotation, writer) ' \
              'value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (info.idd, info.typel, info.title, info.author,
                             info.corauthor, info.dates, info.disease, info.symptom,
                             info.acupoint, info.location, info.annotation, info.writer))

        conn.commit()
        cursor.close()
        conn.close()

    def getAll(self, table):
        '''
         #返回表中全部信息
        :param db:
        :return:
        '''

        sql = "select iid, title, acupoint, writer from" + table

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql)

        #获取查询结果
        rows = cursor.fetchall()
        list = []

        for item in rows:
            list.append(item)

        conn.commit()
        cursor.close()
        conn.close()

        return list

    def getInfoById(self, idd):
        '''
            #通过idd获取信息
        :param idd:
        :return:
        '''
        sql = "select * from information where iid=%s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (idd,))
        row = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return row

    def deleteInfo(self, idd):
        '''
            #通过idd获取信息
        :param idd:
        :return:
        '''
        sql = "delete from information where iid=%s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (idd,))

        conn.commit()
        cursor.close()
        conn.close()



if __name__ == '__main__':
    db = Infoact()
    test_info = Information(1,2,3,4,5,6,7,8,9,10,11,12)
    db.insertInfo(test_info)
    info_list = db.getAll()
    for item in info_list:
        print(item)

