#coding=utf-8
from multiprocessing import Queue,Process
import os,time,random

# 写数据进程
def write(q):
	for value in ['a','b','c']:
		print("put %s to queue..." %value)
		q.put(value)
		time.sleep(random.random())


# 读数据进程
def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print("get %s from ..." %value)
			time.sleep(random.random())
		else:
			break



if __name__ == "__main__":
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))

	#启动写
	pw.start()
	pw.join()

	#启动读
	pr.start()
	pr.join()

	print("所有的数据都写入并且读完")
