#!/usr/bin/env python
# -*- coding:utf-8-*-

old_list=[[0.0,1.0,2.0,3.0],[2.0,3.0,4.0,5.0],[4.0,5.0,6.0,7.0]]  
new_list=[]
for j in range(3):  
  if j<=(1):
    new_list=old_list[0][j]  
  elif j>(1) and j<=(3) :  
    new_list=old_list[0][j]+old_list[1][j-2]  
  elif j>(3) and j<=(5) :  
    new_list=old_list[1][j]+old_list[2][j-4]  
  else:  
    new_list=old_list[2][j] 
print(new_list)

n = 4  # 重ね合わせ対象の1リストに含まれる要素数(サンプルのデータはすべて4個だったので。)
new_list=[]
overlap_num = n//2 # 重ね合わせのレートが50% (// は、割り切れない場合を考慮して整数にしています)
for old in old_list:
    if len(new_list) > overlap_num:
        prefix_index = len(new_list) - overlap_num # 重ね合わせをしない、すでに決まった先頭部分のインデックスを探査
        # 重ね合わせをしないすでに決まった先頭部分のリスト + 重ね合わせする部分のリスト + 重ね合わせしない追加分のリスト
        new_list = new_list[:prefix_index] + [ new_list[prefix_index + idx] + old[idx] for idx in range(overlap_num)] + old[overlap_num:]
    else:
        new_list = old
    print(new_list)
print(new_list)