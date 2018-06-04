from threading import Thread,Lock
import time

# 线程之间共享全局变量，进程之间不共享全局变量
g_num = 0

def work1():
	global g_num
	
	for i in range(1000000):
		#上锁，如果有一方成功上锁，导致另外一方等待，直到这个锁被解开
		mutex.acquire()
		g_num+=1
		# 解锁，只要开了锁，那么接下来会让所有因为被上锁而阻塞的线程，进行抢着上锁
		mutex.release()
	
	print("----in work1,g_num is %d---"%g_num)


def work2():
	global g_num
	
	for i in range(1000000):
		mutex.acquire()
		g_num+=1
		mutex.release()

	print("----in work2,g_num is %d---"%g_num)


print("-------线程创建前g_num is %d----"%g_num)

#创建互斥锁
mutex = Lock()

t1 = Thread(target=work1)
t1.start()

#time.sleep(3)

t2 = Thread(target=work2)
t2.start()

print("-------线程创建后g_num is %d----"%g_num)









