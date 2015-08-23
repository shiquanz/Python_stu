#-*- coding:utf-8 -*-
'''
切片----截取列表中的某个范围的元素
'''
L = ['Michael' , 'Sarah' , 'Tracy' , 'Bob' , 'Jack']
print u'\n\n-----原始列表：-----\n\n',L
print L[0] , L[1] , L[2]
r = []
n = 3
for i in xrange(n):
	r.append(L[i])
print r

print u'前三个元素 0、1、2' , L[0:3]
print u'前三个元素' , L[:3]
print u'后三个元素' , L[-3:]	
print u'前四个元素 ， 每两个取一个(取第一个元素开始)',L[:4:2]
print u'原样复制列表' , L[:]
print u'\ntuple同样可以切片，只是切片后的列表也是tuple\n'
tuple_List = (0,1,2,3,4,5,6,7)
print tuple_List[2:6:2]
print u'字符串 或 Unicode字符串也可以看成是一种list ， \n每个元素一个字符，因此可以切片操作，结果仍是字符串：\n'
print 'ABCDEFGHIJK'[:8:3]


'''
迭代————给定一个list或tuple，通过for遍历，这种遍历成为迭代lteration
'''
d = {'a':10 , 'b':20 , 'c':30}			##常规迭代dict出来的是下标key
for key in d:
	print key
for value in d.itervalues():
	print value
for k , v in d.iteritems():
	print k , '=' ,v
for ch in 'XYZ':
	print ch

from collections import Iterable	
print u'通过colleections模块的Iterable类型判断对象是否可迭代：', isinstance(d , Iterable)

print u'enumerate函数可以把一个list变成索引-元素对' 
for i , val in enumerate(d):
	print  i , val , d[val]

print u'Python中常见的for循环里同时引用两个(多个)变量'
for x , y ,z in [(1,1,1) , (2,4,8) , (3,9,18)]:
	##可理解为x迭代第一维 ， y迭代第二维 ,维数必须与变量一致！！
	print x , y , z

'''
列表生成式 List Comprehensions 用以创建list的生成式
'''
print range(1,11)
print [x*x for x in range(1,11)]  		
print [x*x for x in range(1,11) if x%2 == 0]
print [m+n for m in 'ABC' for n in 'zyx']
### 结构##
print [m+n 
			for m in 'ABC' 
				for n in 'zyx'
		]
### 结构##

import os
print [d for d in os.listdir('.')]		###通过导入os模块列出当前目录、文件

dd = {'x':'A' , 'y':'B' , 'z':'C'}
print [k + '=' + v 
			for k , v in dd.iteritems()]


print [s.lower() for s in L] 		##L[]中的字母全部改为小写，若L中有非字母会报错！！！

int_x = 234
print isinstance(int_x , int)	###isinstance（变量 ， 类型名）判断类型函数 



'''
生成器(Generator) 在循环过程中推算(算法可以很复杂)后续元素,节省空间与时间
generator 是可迭代的对象

''' 
####把列表生成式的[] 改为(),就创建了一个简单generator
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print  L
print g
print g.next()
print g.next()
for x in g:
	print x

### 将函数的输出 print 改为 yield 即将函数变为generator. yield(产 的意思)
def fib(max):
	n , a , b = 0 , 0 , 1
	while n < max:
		yield b
		a , b = b ,  a+b
		n = n+1

print fib(10)			###输出generator
for x in fib(10):		###通过循环迭代出内容
	print x

def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 2
	print 'step 3'
	yield 3
o = odd()
print o.next()
print o.next()
print o.next()
print o.next()			##超过范围会报错

