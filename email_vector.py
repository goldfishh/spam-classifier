import numpy as np
import os 
import re
import json
import time
root = "C:\\Users\\goldfish\\Desktop\\spam"
os.chdir(root)  
from huaji import Process
word_dict = json.load(open("dict.json",'r'))
ham_paths = {root+"\\Temail\\easy_ham",
			root+"\\Temail\\easy_ham_2",
			root+"\\Temail\\hard_ham",
			root+"\\Temail\\hard_ham_2"}
spam_paths = {root+"\\Temail\\spam",
			  root+"\\Temail\\spam1",
			  root+"\\Temail\\spam2",
			  root+"\\Temail\\spam3"}
class Vectoring:
	def __init__(self):
		self.Tfeature = np.zeros((1,5000))
		self.Tlabel = np.zeros((1,1))
		self.Sfeature = np.zeros((1,5000))
		self.Slabel = np.zeros((1,1))		
		self.counter = 1

	def pipelines_boss(self):
		self.pipelines_email(ham_paths,0)
		self.pipelines_email(spam_paths,1)

	def pipelines_email(self,paths,isspam):
		for path in paths:
			os.chdir(path)
			for fpath,dirs,fs in os.walk(path):
				for file in fs:
					self.singleemailtovector(file,isspam)
					print(str(self.counter) + " files" +" done!\n")
					self.counter += 1
	def singleemailtovector(self,file,isspam):
		file_name = str(file)
		obj = Process()
		word_list = obj.preprocessing(file,0)
		if(word_list == []):
			print("ERROR in vector!")
		for i in range(len(word_dict)):
			if word_dict[i] in word_list:
				self.Sfeature[0][i] = 1;
		self.Slabel[0][0] = isspam
		self.Tfeature = np.concatenate((self.Tfeature,self.Sfeature),axis=0)
		self.Tlabel = np.concatenate((self.Tlabel,self.Slabel),axis=0)
	def email_vectoring(self):
		self.pipelines_boss()
		self.Tfeature = np.delete(self.Tfeature,0,axis=0)
		self.Tlabel = np.delete(self.Tlabel,0,axis=0)
		os.chdir(root)
		self.Tfeature.tofile("Tfeature.dat",sep=",",format='%d')
		self.Tlabel.tofile("Tlabel.dat",sep=",",format='%d')
		# np.fromfile("Tfeature.dat",dtype=np.int,sep=",")

if __name__ == '__main__':
	ob = Vectoring()
	ob.email_vectoring()
	print ("done it!")
	time.sleep(1000)