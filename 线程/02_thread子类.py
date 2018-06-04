#coding=utf-8
import threading
import time

class MyThread(threading.Thread):
	def run(self):
		for i in range(3):
			time.sleep(1)
			msg = "i'm "+self.name+" @ "+str(i)
			print(msg)

def test():
	for i in range(5):
		t = MyThread()
		t.start()

if __name__ == "__main__":
	start = time.time()
	test()
	stop = time.time()

	print("执行时间：%f"%(stop-start))
