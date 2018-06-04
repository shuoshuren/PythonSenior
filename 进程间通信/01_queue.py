#coding=utf-8

from multiprocessing import Queue


q = Queue(3)

q.put("haha1")
q.put("haha2")
q.put("haha3")
print("size:%d"%q.qsize())

print(q.get())

q.empty()# 队列是否为空
q.full() # 队列是否满了
