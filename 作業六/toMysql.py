# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:57:09 2020

@author: Lihen
"""
"""import pymysql

con = pymysql.connect(host='192.168.0.100',
                             user='lihen',
                             password='12345678',
                             db='lihen_',)

b=input()

a=con.cursor()
# an = float(input('Enter angle between 0 & 180: '))                     
a.execute("INSERT INTO dht(dht11) VALUES (120)")
con.commit()"""

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host='192.168.0.100',
                             user='lihen',
                             password='12345678',
                             db='lihen_', charset='utf8' )

# 使用cursor()方法获取操作游标 

cursor = db.cursor()
a="幹"
try:
   
   # 执行sql语句
   cursor.execute("INSERT INTO speech(target) VALUES ('%s')" %(a))
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()