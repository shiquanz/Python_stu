# 我是单行注释
# _*_ coding: utf-8 _*_/# coding=utf-8

# Quick Python Script Explanation for Progeammers
# 给程序员的超快Python脚本解说

import os #导入代码模块 os.py

def main():			
	#函数名main在这里并不是必须的，调用在这段脚本的最后部分
	#Python使用缩进来代替其他语句块声明，一般建议每个层级用4个空格来缩进
	print ("Hello World")
	#声明单行字符串，使用单、双引号都可以，注意对字符串中的引号进行转义处理
	print ("这是Alice\'的问候")		
	print ('这是Bob\'的问候')
	#函数调用，声明部分在后边
	foo(5,45)
	
	#字符可乘，等于10个=
	print ('=' * 10) 		
	#调用了os模块中的函数，用 + 连接字符串
	print ('这将直接执行'+os.getcwd()) 

	
	#变量需要先实例化才可进一步计算
	counter = 0
	counter += 1
	#内置的列表类型对象，其实可以包含不同类型的数据，甚至可以包含其他列表对象
	food = ['苹果' , '杏子' , '李子' , '梨']


	#循环中 i 指代了列表中按顺序的每个“food”
	for i in food:
		print ('我就爱整只：'+i)

	print ('数到10')
	#range（）内置函数range([start,] stop[, step])根据start与stop指定的范围以及step设定的步长，生成一个序列。
	#类似[0,1,2,3,4,5]
	##range()直接返回一个数组，
	##xrange()返回一个生成器，里面的内容需要读取（性能考虑优先选择xrange）
	#注意for in 循环语句使用冒号结束声明
	for i in range(10):
		print (i+1)


#def 函数声明，注意使用冒号结束函数声明
def foo(paraml , secondParam):
	res = paraml+secondParam
	#字符串的格式化输出基本类似于C语言
	print ('%s 加 %s 等于 %s ' %(paraml , secondParam , res))
	#或字符串的format方法输出
	print('{} 加 {} 等于 {}'.format(paraml, secondParam, res))
	#判定变量大小 于C语言相同
	#用冒号结束判断句，在if elif else 行最后
	if res < 50:
		print ('这个')
	#逻辑运算符，不使用&& 和 || ，使用更直观的英文 and or 
	elif (res >=50) and ((paraml==42) or (secondParam==24)):
		print ('那个')
	else:
		print ('嗯。。。')
	return res     #这是单行注释
'''
	这是多
行注释
......
						'''
def ioFun():
	print ('print')
	name = input("wtf:")
	print (name)

'''
一般在脚本最后调用主函数main() ， 而且使用内置的脚本名来判定；
当且仅当我们直接运行脚本时，__name__才为__main__
这样当脚本被当做模块进行import 导入时，并不运行main()
所以一般这里是进行测试代码安置的
'''

if __name__=='__main__':
	main()
	ioFun()





