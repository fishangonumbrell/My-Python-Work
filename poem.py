# coding: utf-8
from numpy.random import randint
from numpy.random import choice
#三個引號 用來分行
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止
椎間盤'''
phrase=words.split("\n")
l=randint(2,6)
ll=randint(5,8)
for i in range(l):
    egg=choice(phrase,ll) #choice(list, 取幾個)
    egg=" ".join(egg)
    print(egg)    
