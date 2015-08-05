#-*- coding:utf-8 -*-
print 'hello , World'
print 'The quick brown fox' , 'jumps over' , 'the lazy dog' 
#python会依次打印，遇到,会输出一个空格
print 400
print 100+102
print '100+200 =' , 100+200
var = 30
print var
print '--'*20
firstName = raw_input('please input your firstName\n')
print '\n\nHello , ' , firstName , '!!\n\n'
print '--'*20 , u'以上'
#由于cmd不支持utf-8 所以直接print '中文' 会显示乱码
#可以使用   u'中文字符串'.encode("GBK")   方式解决 或直接 u'中文字符'

a = -100
if a>0:
	print a
else:
	print -a

DateTypeInt = 1000
DateTypeFloat = 1.23e9
DateTypeString = 'abcdefg'
print u'数据类型：' , DateTypeInt , DateTypeFloat , DateTypeString

#转义字符
print '\nI\'m \"ok\"\n'
print r'\\\\\\' 		#为了简化，Python允许r''表示引号内部的字符串默认不需要转义
print r'My\nfuck\tdon\'t tell me why'
#为了简化\n的使用，Python允许用'''.....'''格式表示多行内容
print '''
lin\te1		
line2
line3
'''
DateTypeBoolTrue = True
DateTypeBoolFalse = False
print DateTypeBoolFalse and DateTypeBoolTrue 		#逻辑与
print DateTypeBoolFalse or DateTypeBoolTrue			#逻辑或
print not DateTypeBoolTrue 							#逻辑非
print 3>2 		##返回布尔值
age = raw_input('\nplease input your age:\n\t')
if age>=18:
	print 'you are adult!'
else:
	print 'you are teenager!'
DatetypeNone = None 								##Python中特殊的值，空值。类似于NULL
print DatetypeNone

##变量名必须是英文、数字和下划线_的组合，且不能是数字开头

##当定义一个变量时，即1、内存创建了变量内容2、内存创建了变量并指向其内容
##通常用大写表示常量
PI = 3.1415 
##但实际上PI仍然是一个常量，Python没有任何机制保证PI不会被改变
##所以Python中“常量”用大写表示只是习惯


##编码问题##
##编码问题##
##编码问题##
'''''
开始计算机只支持英文即一些符号，由此有了 ASCII 码，由一个字节可表示
中文需要至少两个字节，由此中国制定了 GB2312 编码
全世界百种语言在同一文档里这样必定乱码，由此 Unicode 编码把所有语言同一到一起
Unicode默认两个字节，如一篇英文文档使用该编码会增加存储和网络传输，
由此产生 UTF-8 ，对Unicode进行“压缩” 

'''''

print u'中文显示！！'		##Python后来添加了对unicode的支持，以Unicode表示字符串用u'.....'表示
print ord('A')				##ord('d') 转换为字符的ASCII编码
print chr(65)				##chr(65)  转换为数字的ASCII值
print u'中文'.encode('utf-8')##把Unicode 的“中文”转换为UTF-8编码的“中文”
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')##把UTF-8的“中文”转换成Unicode字符

'''
为了让Python解释器读取源代码时是按照utf-8编码读取，通常在文件开头写上：
#!/usr/bin/env python
#-*- coding:utf-8 -*-
第一行告诉Linux/OS X系统这是个Python可执行程序，Windows系统会自动忽略
第二行告诉Python解释器，按照UTF-8读取源码，否则中文可能乱码

'''

##编码问题##
##编码问题##
##编码问题##

#格式化输出 %d整数  %f浮点数  %s字符串  %x十六进制   
lastName = raw_input('please input your lastName:\n')
print '\nYour LastName is %s , How old are you?\n' %lastName
old = int(raw_input())  		##或直接使用input()
print '%d years old , Good Luck!!\n' %old
string = '123456789'
print u'字符串%s的长度为%d' %(string , len(string))	#计算并返回字符串长度


print '\n','###'*20
print u'\nlist 是一种有序的集合，可以随时添加和删除其中的元素.（有序列表）'
classmates = ['Michael' , 'Bob' , 'Tracy']
print classmates , u'长度（len()函数）为%d'%len(classmates)
print u'''索引方式访问list中的每一个位置的元素，
从0开始
classmates[0]=%s
classmates[1]=%s
classmates[2]=%s'''%(classmates[0],classmates[1],classmates[len(classmates)-1])
		###为了确保索引不超出范围，最后一个元素的索引是 len(ListName)-1 或直接[-1] 以此类推

print u'倒数第二个元素classmates[-2]：' , classmates[-2]
classmates.append('Adam')		##往list中追加元素到末尾
classmates.append('Appler')
classmates.insert(1 , 'Jack')	##往list中1的位置添加元素（从0开始）
classmates.pop()				##删除list末尾的元素
classmates.pop(1)				##删除指定位置的元素
classmates[1] = 'Sarah'			##替换元素直接赋值
classmates[2] = ['1' , '2' , '3']
print classmates

##另一种有序列表 tuple ，区别于list：一旦初始化，就无法修改 ,访问元素方式与list一致
onather = ('Michael' , 'Bob' , 'Tracy')
t = ()
t1 = (1 , ) ######若要定义一个元素的tuple ，必须加 ， 否则Python规定 t1=1

##“可变”的tuple ：
tup = ('a' , 'b' , ['C' , 'D'])
tup[2][0] = 'X'
tup[2][1] = 'Y'
print tup , u'tuple不可修改 指的是不可修改tuple元组指向的元素（即指针不变）'
tup[2].append('wtf')	###tup 指向的第三个元素为list 它的地址没有发生变化！！
##！！错误！！##tup[1] = 'g'
print tup

''' 
for...in... 依次把list 或tuple 中的每个元素迭代出来
'''
names = ['Michael' , 'Bob' , 'Sarah']
for name in names:
	print name
for tu in tup:
	print tu
sum = 0
for num in range(101): 		##range(9)生成一个从零开始小于9的整数list
	sum = sum + num
print sum


'''
while 循环，只要满足条件就不断循环，条件不满足退出循环
'''
sum = 0
n = 100
while n>0:
	sum = sum + n
	n = n - 1
print sum

##http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868193482529754158abf734c00bba97c87f89a263b000