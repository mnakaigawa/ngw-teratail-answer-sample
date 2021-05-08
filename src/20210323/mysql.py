#!/usr/bin/env python
# -*- coding:utf-8-*-
'''
Created on 2018/04/13

@author: nakaigawa
'''
import MySQLdb

conn = MySQLdb.connect(
 user='root',
 passwd='root',
 host='localhost',
 db='mysql')

cur = conn.cursor()
sql = "select * from START_END_ITEM order by Start_datetime;"
cur.execute(sql)

# 実行結果を取得する
rows = cur.fetchall()

# 一行ずつ表示する
for row in rows:
 print(row)

cur.close
conn.close
