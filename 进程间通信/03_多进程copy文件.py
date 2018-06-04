from multiprocessing import Pool,Manager
import os

def copyFileTask(name,oldFolderName,newFolderName,queue):
	"""完成copy一个文件的功能"""
	fr = open(oldFolderName+"/"+name);
	fw = open(newFolderName+"/"+name,"w")
	content = fr.read()
	fw.write(content)
	fr.close()
	fw.close()
	queue.put(name)


def main():

	#0.获取要copy的文件夹的名字
	oldFolderName = input("请输入文件夹的名字：")

	#1.创建一个文件夹
	newFolderName = oldFolderName+"-复件"
	print("附件:%s"%newFolderName)
	os.mkdir(newFolderName)

	#2.获取old文件夹中所有的文件名字
	fileNames = os.listdir(oldFolderName)
	print(fileNames)
	#3.使用多进程的方式copy 原文件夹中所有文件到new文件夹
	pool = Pool(3)
	queue = Manager().Queue()
	
	for name in fileNames:
		pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderName,queue,))
	
	
	num = 0
	allNum = len(fileNames)
	while num<allNum:
		queue.get()
		num+=1
		copyRate = num*100/allNum
		print("\rcopy的进度是:%.2f%%"%copyRate,end="")
		
	print("\r已完成拷贝")
		

	pool.close()
	pool.join()
	

if __name__ == "__main__":
	main()