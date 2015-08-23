#-*- coding:utf-8 -*-
'''

'''
class Student(object):
	"""docstring for Student"""
	pass
s = Student()
s.name = 'Joker'		# 动态给实例绑定一个属性
print s.name
def set_age(self , age):
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age , s , Student)	#给实例绑定一个方法
s.set_age(25)		##调用实例方法
print s.age 		##测试结果

#但给一个实例绑定方法,对另一个实例不起作用
s2 = Student()
# s2.set_age(24)	尝试调用方法,报 AttributeError

#为了给所有实例都绑定方法,可以给class绑定方法:
def set_score(self , score):
	self.score = score
Student.set_score = MethodType(set_score , None , Student)
#绑定方法后,实例均可以使用
s.set_score(100)
s2.set_score(88)
print s.score
print s2.score
#动态绑定允许我们在程序运行的过程中动态给class加上功能


'''如果想要限制class的属性,只允许对student实例添加name和age属性'''
'''python允许定义class的时候,定义一个特殊变量__slots__ , 来限制class能添加的属性'''
class Students(object):
	"""docstring for Students"""
 	__slots__ = ('name' , 'age') 	#用tuple定义允许绑定的属性名称

c = Students()
c.name = 'Michael'	#动态绑定属性name
s.age = 22
# s.score = 89	报错AttributeError
'''
	只用__slots__注意:
	__slots定义的属性仅对当前类起作用,对继承的子类不起作用!!
'''

'''
	Python 内置的 @property装饰器负责把一个方法变成属性调用
'''
class Studen(object):
	"""docstring for Studen"""
	@property  				# @property把一个getter方法变成属性
	def score(self):
	    return self._score
	
	@score.setter   		# @score.setter把 setter方法变成属性
	def score(self , value):
		if not isinstance(value , int):
			raise ValueError('score must be an integer!')
		if (value<0 or value>100):
			raise ValueError('score must between 0-100')
		self._score = value

s = Studen()
s.score = 60
print s.score
#s.score = 99999		##报错ValueError
## @property广泛应用在类的定义中,可以让调用者写出简短的代码,
##  同时保证对参数进行必要的检查


'''
多继承
	class Dog(Animal , Flying):
		"""docstring for Dog"""
		pass
	通过多继承,一个子类就可以同时获得多个父类的所有功能
'''
'''
Mixin
	在设计类的继承关系时，通常，主线都是单一继承下来的，
	如果需要“混入”额外的功能，通过多重继承就可以实现，
	这种设计通常称之为 Mixin。

	Mixin的目的就是给一个类增加多个功能，
	这样，在设计类的时候，我们优先考虑通过多重继承选择组合不同的类的功能，
	而不是设计多层次的复杂的继承关系。
'''

"""
######           定制类
__str__
__iter__
__getitem__
__getattr__
__call__
######           定制类
"""
# type() 函数可以查看一个类型或变量的类型
# __metaclass__ : metaclass 允许你创建类或者修改类,或者:类可以看成是metaclass的"实例"
