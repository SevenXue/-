# -coding:utf-8

import pymysql
from information import *

class Acuact:
    def getCon(self):
        conn = pymysql.connect(host="59.77.36.69", user="root", port=3306, passwd="NMRdaixie123", db="acupuncture")

        return conn

    # def insertInfo(self, info):
    #     '''
    #         #插入
    #     :param info: 待插入对象
    #     :return:
    #     '''
    #
    #     #insert sql
    #     sql = 'insert into acupoint(id, chinese, vein, dissection, disease, compatibility, location, url' \
    #           'value(%s, %s, %s, %s, %s, %s, %s, %s)'
    #
    #     conn = self.getCon()
    #     if conn == None:
    #         return
    #
    #     cursor = conn.cursor()
    #     cursor.execute(sql, (info.id, info.chinese, info.vein, info.dissection,
    #                          info.disease, info.compatibility, info.location, info.url))
    #
    #     conn.commit()
    #     cursor.close()
    #     conn.close()

    def getAll(self):
        '''
         #返回表中全部信息
        :param db:
        :return:
        '''

        sql = "select id, chinese, vein, url from acupoint"

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

    def getInfoById(self, id):
        '''
            #通过idd获取信息
        :param id:
        :return:
        '''
        sql = "select * from acupoint where id=%s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return row

    # def deleteInfo(self, id):
    #     '''
    #         #通过id获取信息
    #     :param id:
    #     :return:
    #     '''
    #     sql = "delete from acupoint where id=%s"
    #
    #     conn = self.getCon()
    #     if conn == None:
    #         return
    #
    #     cursor = conn.cursor()
    #     cursor.execute(sql, (id,))
    #
    #     conn.commit()
    #     cursor.close()
    #     conn.close()

    def saveUpdate(self, id, info):
        '''
            #通过
        :param id:
        :return:
        '''
        sql = "update acupoint set chinese=%s, vein=%s, dissection=%s, disease=%s, compatibility=%s, location=%s, url=%s where id=%s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (info.chinese, info.vein, info.dissection,
                             info.disease, info.compatibility, info.location, info.url, id))

        conn.commit()
        cursor.close()
        conn.close()

if __name__ == '__main__':
    db = Acuact()
    test_info = Acupoint(2,3,4,5,6,7,8)
    db.insertInfo(test_info)
    info_list = db.getAll()
    for item in info_list:
        print(item)

