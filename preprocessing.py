#1 读文件到字符串
# cd C:\Users\goldfish\Desktop\spam
	# f_i = ""
	# f = open("1")
word_frequency = {}
def preprocessing(file_string):
	try:
		f = open(file_string)
		email_contents = f.read()
		#
		#
		#2 去标题
		#
		cut = re.search(r'\n[ \t]*\n',email_contents).span()[1] - 1
		#      \n...\n
		# cut        ↑
		email_contents = email_contents[cut:]
		#
		#
		#3 其他预处理
		#
		#小写 √
		email_contents = email_contents.lower()
		#删HTML标签 √
		#
		email_contents = re.sub(r'<[^<>]+>',' ',email_contents);
		# URL链接替换 → httpaddr √
		# http//https :// xx.xxx.xxx
		email_contents = re.sub(r'http\:\/\/[\w\.\/]+|https\:\/\/[\w\.\/]+','httpaddr',email_contents)
		# 
		# URL邮件地址替换 → emailaddr
		#
		email_contents = re.sub(r'[\w\-\_]+\@[\w]+\.[\w]+','emailaddr',email_contents)
		# 数字替换 →  number  √
		#    整数  小数
		email_contents = re.sub(r'(\d+|\d+\.\d+)','number',email_contents)
		# 美元替换 $ → dollar   √
		# 
		email_contents = re.sub(r'\$','dollar',email_contents)
		# 单词词干化
		#         实现复杂
		# 去除非单词和标点
		# 
		email_contents = re.sub(r'[\W]',' ',email_contents)
		# 删去单字母
		for i in range(50):
			email_contents = re.sub(r' [a-z] ',' ',email_contents)
		# 删去多余空格
		email_contents = re.sub(r'[\t\n ]+',' ',email_contents)
		#

		# from stemmer import PorterStemmer
		# stemmer = PorterStemmer()
		# 
		from stemmer import PorterStemmer
		stemmer = PorterStemmer()
		email_contents = stemmer.stem(email_contents)
		# 
		
		word_list = re.findall(r'\w+',email_contents)
		# return word_list
		for word in word_list:
			if(word_frequency.get(word,"None") == "None"):
				word_frequency[word] = 1;
			else:
				word_frequency[word] += 1;
		# return word_frequency
	except:
		print (file_string + "  ERROR")
		pass