from threading import Thread
import time


def test():
	print("------test------------")
	time.sleep(1)

start = time.time()
for i in range(5):
	t = Thread(target=test)
	t.start()

stop = time.time()

print("执行时间：%f"%(stop-start))
