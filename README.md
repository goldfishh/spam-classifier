# 简单垃圾邮件分类器实现
2017.9.4 ~ 2017.11.9  DUT 人工智能 ---3'
## 项目介绍
* 使用matlab和python两种语言分别实现
* 使用支持向量机训练分类器模型
* 后续可添加更多训练方式
## 项目流程
1. 邮件文本预处理
2. 提取高频词汇表
3. 查表建立邮件向量
4. 整理数据集
5. 训练模型
6. 交叉验证模型
7. 单一邮件测试
### 邮件文本预处理
1. 删去标题
2. 小写转换
3. 去除HTML标签
4. URL正规化
5. Email地址正规化
6. Dollars符号正规化
7. **单词提取词干**
8. 去除非单词符号
9. 空格转换
### 提取高频词汇表
使用已实现预处理程序扫描所有数据样本,建立词汇表,按照词频排序后取前N个词作为高频词汇表
### 查表建立邮件向量
邮件文本预处理后转换为字符串数组,遍历数组查词汇表
* 词汇表有这个词 p(x) = 1
* 词汇表没有这个词 p(x) = 0
### 整理数据集
随机打乱数据集,按比例分出  训练集 测试集 交叉验证集
### 训练模型
使用SVM(支持向量机)
### 交叉验证模型
测试模型泛化性
### 单一邮件测试
