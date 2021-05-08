#!/usr/bin/env python
# -*- coding:utf-8-*-

import csv
import chardet
import io

# csv_file_name="test_utf8.csv"
csv_file_name="test_sjis.csv"

with open(csv_file_name, "rb") as csv_file:
    binary = csv_file.read()
    ret_dict = chardet.detect(binary) # 文字コードを判定
    print(ret_dict) # 判定した文字コードなどの情報を出力
    reader = csv.DictReader(io.StringIO(binary.decode(ret_dict['encoding']))) # 判定した文字コードでエンコード
    for line in reader:
        print(line)
