from threading import Thread
import time

# 线程之间共享全局变量，进程之间不共享全局变量
g_num = 0

def work1():
	global g_num
	for i in range(1000000):
		g_num+=1

	print("----in work1,g_num is %d---"%g_num)

def work2():
	global g_num
	for i in range(1000000):
		g_num+=1
	print("----in work2,g_num is %d---"%g_num)


print("-------线程创建前g_num is %d----"%g_num)

t1 = Thread(target=work1)
t1.start()

#time.sleep(3)

t2 = Thread(target=work2)
t2.start()

print("-------线程创建后g_num is %d----"%g_num)









