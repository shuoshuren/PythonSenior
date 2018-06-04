from multiprocessing import Pool,Manager
import os

def copyFileTask(name,oldFolderName,newFolderName,queue):
	"""���copyһ���ļ��Ĺ���"""
	fr = open(oldFolderName+"/"+name);
	fw = open(newFolderName+"/"+name,"w")
	content = fr.read()
	fw.write(content)
	fr.close()
	fw.close()
	queue.put(name)


def main():

	#0.��ȡҪcopy���ļ��е�����
	oldFolderName = input("�������ļ��е����֣�")

	#1.����һ���ļ���
	newFolderName = oldFolderName+"-����"
	print("����:%s"%newFolderName)
	os.mkdir(newFolderName)

	#2.��ȡold�ļ��������е��ļ�����
	fileNames = os.listdir(oldFolderName)
	print(fileNames)
	#3.ʹ�ö���̵ķ�ʽcopy ԭ�ļ����������ļ���new�ļ���
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
		print("\rcopy�Ľ�����:%.2f%%"%copyRate,end="")
		
	print("\r����ɿ���")
		

	pool.close()
	pool.join()
	

if __name__ == "__main__":
	main()