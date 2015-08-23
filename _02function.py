#-*- coding:utf-8 -*-
'''
100
 ∑ （n+1）
n=1

以上西格玛符号表示 从n=1开始，（1+1）+（2+1）+（3+1）。。。一直加到n=100
函数是最基本的一种代码抽象方式
'''
print abs(-100)			##求绝对值函数
print cmp(3,1)			##比较函数，如果3>1 ， 返回1 ；如果3==1返回0；如果3<1,返回-1
print int(3.14)			##类型转换：把其他数据类型转换为int
print float(10)			##类型转换：把其他数据类型转换为float
print str(1.23)			##类型转换：把其他数据类型转换为字符串
print unicode(100)		##类型转换：把其他编码类型转换为unicode
print bool('')			##类型转换：把其他数据类型转换为bool(非零、空即真)

### 函数名其实就是指向一个函数对象的引用，完全可以吧函数名赋给一个变量，相当于给函数起“别名”

### 自定义函数范例
### 自定义函数范例

### 空函数 pass语句什么都不做，只是占位符，让代码先运行起来
def nullfun():
	pass
	if age>18:
		pass

def my_abs(x):
	if not isinstance(x , (int , float)):		###内置类型检查函数
		raise TypeError('bad operand type')		###抛出一个错误
	if x>=0:
		return x
	else:
		return -x
### 函数体内部的语句在执行时遇到return，函数就执行完毕，并将结果返回。如果没有return语句，函数执行完毕也会返回None 。return None 可简写为return
print my_abs(4)

def move(x , y):
	move_x = x+y
	move_y = x*y
	return move_x , move_y

print move(3,3)
i , k =move(5,6)
print i
print k
### 函数可以返回多个值，但其实时一个tuple。多个变量可同时按顺序接收一个tuple

'''
	函数默认参数，降低调用难度，如需要更改默认参数，则按顺序传参即可
	必选参数在前，默认参数在后
	默认参数必须指向不变对象！！
	为什么要设计str、None这样的不变对象呢？
	因为不变对象一旦创建，对象内部的数据就不能修改，
	这样就减少了由于修改数据导致的错误。
	此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
	同时读一点问题都没有。
	我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
'''
def power(x , n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print power(4)
print power(4,3)
print '----'*20

### 可变参数
def calc1(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print calc1([1,2,3]) 		### 参数为list
def calc2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	print sum
calc2(1,2,3,4)			###可变参数。代码完全不变，但调用函数可传入任意个参数，包括零个
nums = [1 , 2 , 4 , 5]
calc2(*nums)				###list 或tuple元素变为可变参数传递入函数！！这种方法很常见

print '----'*20
def person(name , age , **kw):	###关键字参数，允许传入任意含参数名的参数
	print name , age , kw
person('Joker' , 32 , city='Beijing' , gender='M')

### 参数组合 参数顺序必须是：：必选参数、默认参数、可变参数、关键字参数
def func(a , b , c=0 , *args , **kw):
	print 'a=' , a , 'b=' , b , 'c=' , c , 'args=',args , 'kw=' , kw

func(1 , 2 , 3 , 'a' , 'b' , x=23 , y=24 , z=25)

'''
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，
但最好使用习惯用法。
'''


### 递归函数
### 递归函数
def fact(n):				### 阶乘
	if n==1:
		return 1
	return n*fact(n-1)
#       print fact(1000)      栈溢出！！！ 解决方法：尾递归优化
'''
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，
没有循环语句的编程语言只能通过尾递归实现循环。
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
'''