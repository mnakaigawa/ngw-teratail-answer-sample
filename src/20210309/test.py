#!/usr/bin/env python
# -*- coding:utf-8-*-

#リスト作り方①
a_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#リスト作り方②
b_list = []
c_list = []
for i in range(3):
    b_list.append(0)
for j in range(3):
    c_list.append(b_list)

#リスト作り方③
d_list = [[0]*3]*3

a_list[1][1] = 1
c_list[1][1] = 1
d_list[1][1] = 1

print(a_list)
print(c_list)
print(d_list)

e_list = [[0]*3 for _ in range(3)]
e_list[1][1] = 1
print(e_list)