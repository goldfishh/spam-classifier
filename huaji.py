#coding:utf-8

import time
import os
root = "C:\\Users\\goldfish\\Desktop\\spam"
os.chdir(root)  
from stemmer import PorterStemmer
import re
import json

class Process:
	def __init__(self):
		self.word_frequency = {}
		self.succeeded = 0
		self.abandoned = 0
		self._dir = ""

	def getreadytopreprocessing(self):
		_path = root+ '\\Temail'
		# os.chdir(_path)  
		for fpathe,dirs,fs in os.walk(_path):
			for _dir in dirs:
				self._dir = _dir
				os.chdir(os.path.join(fpathe,_dir))
				for _fpathe,_dirs,_fs in os.walk(os.path.join(fpathe,_dir)):
					for file in _fs:
						self.preprocessing(file,1)	

	def preprocessing(self,file,status):  #status = 1 内部调用 0 外部调用
		try:
			file_name = str(file)
			f = open(file_name,'r',encoding='utf-8')
			email_contents = f.read()

			#转换大小写
			email_contents = email_contents.lower()

			#删除邮件前缀
			email_contents = email_contents+"\n \n"
			cut = [0,0]
			cut = re.search("([\n])([" "]*)([\n])",email_contents).span(0)
			length=len(email_contents)
			if(cut[1]!=length):
				email_contents = email_contents[cut[1]:length]

			#删HTML标签
			email_contents = re.sub(r'<[^<>]+>',' ',email_contents)

			# URL链接替换 → httpaddr
			email_contents = re.sub(r'http\:\/\/[\w\.\/\-\=\?]+|https\:\/\/[\w\.\/\-\=\?]+','httpaddr',email_contents)

			#邮件地址替换 → emailaddr
			email_contents = re.sub(r'[\w\-\_]+\@[\w]+\.[\w]+','emailaddr',email_contents)
						
			#数字替换 →  number
			email_contents = re.sub(r'(\d+|\d+\.\d+)','number',email_contents)

			#美元替换 $ → dollar
			email_contents = re.sub(r'\$','dollar',email_contents)

			#去除非单词和标点
			email_contents = re.sub(r'[-_\']','',email_contents)
			email_contents = re.sub(r'[\W]',' ',email_contents)
							

			#删去单字母
			# for j in range(50):
			# 	email_contents = re.sub(r' [a-z] ',' ',email_contents)

			#删去多余空格
			email_contents = re.sub(r'[\t\n ]+',' ',email_contents)

			#提取词干
			stemmer = PorterStemmer()
			email_contents = stemmer.stem(email_contents)

			#测试结果
			#print(email_contents)
			#统计词频
			word_list = re.findall(r'\w+',email_contents)
			if(status == 1):			
				for word in word_list:
					if(len(word) > 30):
						#print(file)
						#print(' WARNNING:Long word existance: '+word+'\n')
						continue
					if(self.word_frequency.get(word,"None") == "None"):
						self.word_frequency[word] = 1;
					else:
						self.word_frequency[word] += 1;
			elif(status == 0):
				return word_list
			self.succeeded = self.succeeded + 1
		except Exception as e:
			with open(root+"\\error.log","a") as error_log:
				error_log.write("-------------------------------\n")
				error_log.write(str(self._dir) + " " + str(file) + " " + str(e) + '\n')
			# print(str(self._dir) + " " + str(file) + " " + str(e) + "\n")
			self.abandoned = self.abandoned + 1
			if(status == 0):
				blank_list = []
				return blank_list
			pass

	def output(self):
		self.word_frequency=sorted(self.word_frequency.items(),key=lambda item:item[1])
		print('Preprocess finished')
		print('\nsucceeded:')
		print(self.succeeded)
		print('\nabandoned:')
		print(self.abandoned)
		print('\nData has been saved in File \'frequency.json\'')
	
	def save(self):
		os.chdir(root)
		with open('frequency.json','w',encoding='utf-8') as file:  
			json.dump(self.word_frequency,file,ensure_ascii=False)
			file.write('\n')  
	def todict(self):
		 # list  last 4000
		word_dict = []
		length = len(obj.word_frequency)
		for i in range(5000):
			word_dict.append(obj.word_frequency[length-i-1][0])
		with open('dict.json','w',encoding='utf-8') as file:
			json.dump(word_dict,file,ensure_ascii=False)
			file.write('\n')  
		# tmp = json.load(open(dict.json,'r'))

if __name__ == '__main__':
	obj = Process()
	obj.getreadytopreprocessing()
	obj.output()
	obj.save()
	time.sleep(100)