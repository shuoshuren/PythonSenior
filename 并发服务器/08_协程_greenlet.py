#!/usr/bin/python

from greenlet import greenlet
import time


def test1():
	while True:
		print("------A--------")
		gr2.switch()
		time.sleep(0.5)


def test2():
	while True:
		print("------B--------")
		gr1.switch()
		time.sleep(0.5)


if __name__ == '__main__':
	gr1 = greenlet(test1)
	gr2 = greenlet(test2)
	#切换到gr1中执行
	gr1.switch()