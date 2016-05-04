#-*- coding:utf-8 -*-
'''
函数式编程
允许吧函数本身作为参数传入另一个函数,还允许返回一个函数
由于Python允许使用变量,因此python不是纯函数式编程语言(输入确定,输出不一定)
'''
##绝对值函数 abs()
print '\n\n' , abs
f = abs			###变量可以指向函数 , 函数名也是变量,abs可以看成指向可以计算绝对值函数的变量
print f
print f(-10)

#### 一个函数接受另一个函数作为参数,这种函数称之为 高阶函数 --此时f代表abs函数
def add(x , y , f):
	return f(x) + f(y)
print add(-3 , -5 , f) 

'''
map()  函数接收两个参数,一个是函数,一个是序列.
		map将传入的函数依次作用到每个元素 ,并把结果作为新list返回
'''
def map_func(x):
	return x*x
print map(map_func , [i for i in range(10)])	##1~10分别平方组成新list
print map(str , [i for i in range(10)])			##1~10分别变成字符串组成新list

'''
reduce 把一个函数作用在一个序列上,函数必须接收两个参数,
		reduce把结果继续和序列的下一个元素做累积计算
		reduce(f , [x1 , x2 , x3 , x4]) = f(f(f(x1 , x2) , x3) , x4)
'''

def add_num(x , y):
	return x+y
print reduce(add_num , [i for i in range(101)])
###等价于下面:sum()函数的参数是一个list
print sum([i for i in range(101)])


def fn(x , y):
	return x*10+y
print reduce(fn , [1,3,5,7,9])			##把序列变成整数

l = [i for i in range(10)]


def str2num(s):
	return {'0':0 , '1':1 , '2':2 , '3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9}[s]
print str2num('5')

print  {'0':0 , '1':1 , '2':2 , '3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9}['1']
print '----00000000--------'
def str2int(s):
	pass
'''
filter()函数用于过滤序列 , 函数接收一个函数和一个序列,
		函数依次作用于序列,根据返回bool决定保留还是丢弃元素
'''
def is_odd(n):
	return n%2 == 1
print filter(is_odd , [i for i in range(20,30)])

def not_empty(s):				##把序列中的空字符串去掉
	return s and s.strip()
print filter(not_empty , ['A' , ' ' , 'B' , None , 'C' , ' '])

'''
sorted 排序 如果两个元素x , y x>y 返回1 , x<y返回-1 ,x=y返回0
'''
l = [34,12,52,66,3,7]
print sorted(l)
def reversed_cmp(x , y):		##倒序
	if x>y:
		return -1
	if x<y:
		return 1
	return 0
print sorted(l , reversed_cmp)

print sorted(['Bob' , 'about' , 'Zoo' , 'Creadl']) ##按首字母ACSII排序

def cmp_ignore_case(s1 , s2):	##忽略大小写排序
	u1 = s1.upper()
	u2 = s2.upper()
	if u1<u2:
		return -1
	if u1>u2:
		return 1
	return 0
print sorted(['Bob' , 'about' , 'Zoo' , 'Creadl'] , cmp_ignore_case)

'''
返回函数
其代码不会立即执行,而是调用函数后才会执行
'''
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f1 = lazy_sum(1,3,5,7,9)				##调用lazy_sum不会得到函数计算结果,而是得到函数本身
f2 = lazy_sum(1,3,5,7,9)
print f1
print f1()								##调用函数后得到结果
print f1 == f2							##每次调用都会返回一个新的函数			

'''
闭包		返回函数时,相关参数和变量都保存在返回的函数中
'''
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1 , f2 , f3 = count()
print f1() , f2() , f3()		## 闭包时,函数引用了变量 i 但并非立即执行,等到3个函数都返回时,i=3才执行
								## !!--返回函数尽量不要引用任何循环变量,或者后续会发生变化的变量--!!
## 若闭包中一定引用循环变量:-----再创建一个函数,用该函数的参数绑定循环变量当前值(可用lambda函数缩短代码)
def count_t():
	fx = []
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		fx.append(f(i))
	return fx
ft1 , ft2 , ft3 = count_t()
print ft1() , ft2() , ft3()


'''
匿名函数 lambda
	当传入函数时,不需要显式地定义函数,直接传入匿名函数更方便
	匿名函数只能有一个表达式,不用return,返回值就是表达式的结果
	pythong对匿名函数支持有限,只能一些简单情况下只用.....
'''
print map(lambda x: x*x , [1,2,3,4,5,6,7,8,9])		##冒号前x为函数参数
##匿名函数不必担心函数名冲突,另,匿名函数也是一个函数对象
fa_lambda = lambda x:x*x
fb_lambda = lambda x:x+x
print fa_lambda , fb_lambda
print fa_lambda(5) , fb_lambda(5)
##同样可以把匿名函数作为返回值
def  build(x , y):
	return lambda:x*x+y*y

print '----'*10
'''
装饰器 ------(◎﹏◎)比较复杂....
	在代码运行期间动态 增加 功能的方式称之为"装饰器"(Decorator)
	本质上装饰器是一个返回函数的高阶函数
	在OOP中decorator称为装饰模式,通过继承和组合实现.而Python除了支持OOP的decorator外
	直接从语法层次支持decorator.Python的decorator可以用函数实现,也可以用类实现
'''
def log(func):
	def wrapper(*args , **kw):
		print 'call %s():' %func.__name__
		return func(*args , **kw)
	return wrapper
@log		##把@log放到函数定义处相当于 now = log(now)
def now():
	print '2015-08-09'
now()

'''
偏函数
	functools.partial 帮助我们创建一个偏函数,
	把一个函数的某些参数给固定住(设置默认值),
	返回一个新的函数,从而调用这个函数会更简单
'''
##int()函数有一个base参数,可以做N进制转换
print int('010001011' , base = 2)

def int2(x , base=2):
	return int(x , base)
print int2('10001011')		
##设置偏函数::
import functools
int2_funct = functools.partial(int , base=2)
print int2_funct('1100110')
## 创建偏函数,实际上可以接受函数对象 *args 和 **kw 这三个参数
## 当函数参数过多,需要化简可以使用functools.partial创建一个新函数,从而在调用时更简单






