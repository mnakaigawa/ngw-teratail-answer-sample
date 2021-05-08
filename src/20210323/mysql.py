#!/usr/bin/env python
# -*- coding:utf-8-*-
import pymysql
# MySQLに接続する
connection = pymysql.connect(host='localhost',
                            user='ユーザー名',
                            password='パスワード',
                            db='データベース名',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)
# SQLを操作する
with connection.cursor() as cursor:
    #「my_table」から「tw_id」が重複を省いた仮テーブル「my_table_temp」を作成する
    sql = "select * from START_END_ITEM where Start_datetime >= '2021/3/1 00:00:00' order by Start_datetime;"
    cursor.execute(sql)
    records = cursor.fetchall()

    new_records = [[records[idx]['End_datetime'], records[idx+1]['Start_datetime'], records[idx]['Item']] for idx in range(len(records)-1)]

# MySQLから切断する
connection.close()

# 結果表示
for record in new_records:
    print(record[0].strftime("%Y/%m/%d %H:%M:%S"), record[1].strftime("%Y/%m/%d %H:%M:%S"), str(record[2]))
