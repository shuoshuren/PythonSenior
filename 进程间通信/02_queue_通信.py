#coding=utf-8
from multiprocessing import Queue,Process
import os,time,random

# д���ݽ���
def write(q):
	for value in ['a','b','c']:
		print("put %s to queue..." %value)
		q.put(value)
		time.sleep(random.random())


# �����ݽ���
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

	#����д
	pw.start()
	pw.join()

	#������
	pr.start()
	pr.join()

	print("���е����ݶ�д�벢�Ҷ���")
