#coding=utf-8

from multiprocessing import Queue


q = Queue(3)

q.put("haha1")
q.put("haha2")
q.put("haha3")
print("size:%d"%q.qsize())

print(q.get())

q.empty()# �����Ƿ�Ϊ��
q.full() # �����Ƿ�����
