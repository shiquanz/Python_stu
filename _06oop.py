#-*- coding:utf-8 -*-
'''
在class内部,可以有属性和方法,
而外部代码可以通过直接调用实例变量的方法来操作数据,
这样就隐藏了内部复杂的逻辑
'''
class Student(object):
	"""docstring for Student"""
	def __init__(self, name , score):  	## __init__第一个参数永远是self表示创建的实例本身
		super(Student, self).__init__()
		self.name = name  	###在属性名钱加上两个下划线,变成一个私有变量(private)使得
		self.__score = score
	def print_score(self):
		print('%s:%s'%(self.name , self.__score))

	def get_grade(self):				##封装的好处在于可以添加方法
		if self.__score >=90:
			return 'A'
		elif self.__score >=60:
			return 'B'
		else:
			return 'C'
			'''
如果要更改private , 可添加set_score 方法
如果要访问private , 可添加get_score 方法
'''
	def get_score(self):
		return self.__score
	def set_score(self , __score):		##添加set_score 方法的好处是可以做检查
		if 0 <= __score <= 100:
			self.__score = __score
		else:
			print 'Error number!!'
		return self.__score

bart = Student('Bart Simpson' , 69)	##实例化(Instance)
lisa = Student('Lisa Simpson' , 98)
bart.print_score()
lisa.print_score()

bart.name = 'Joke Simpson'		##尝试更改public   name
bart.__score = 99				##试图更改private   __score
bart.print_score()				##score 未能更改,name成功更改

print 'bart.get_grade()' , bart.get_grade()

print 'bart.get_score()' , bart.get_score()

bart.set_score(440)		##通过set_score方法修改__score

print bart.get_score()	##得到修改后的结果

'''
在Python中，变量名类似__xxx__的，也就是以双下划线开头，
并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
不是private变量
'''
'''
继承 多态

'''
class Animal(object):
	"""docstring for Animal"""

	def run(self , whatt='Animal'):
		age = 10
		print '%s is running .....'%whatt

class Dog(Animal):
	"""docstring for Dog"""
	pass

class Cat(Animal):
	"""docstring for Cat"""
	def run(self ):					##重写父类的方法,以表现出多态
		print 'Cat is running .....'	

animal = Animal()
dog = Dog()
cat = Cat()

animal.run()
dog.run(whatt='Dog')
cat.run()

'''
获取对象信息
'''
print type('1234')
print type(Animal)
print type(abs)

print isinstance(dog , Dog)		##判断类型
print isinstance(dog , Animal)
print isinstance(dog , Cat)
print isinstance([1,2,3] , (list  , tuple))			#判断是list 或 tuple
print isinstance((1,2,3) , (list , tuple))

'''
dir()
	如果要获得一个对象的所有属性和方法，可以使用dir()函数，
	它返回一个包含字符串的list，
	比如，获得一个str对象的所有属性和方法：
'''
print dir('ABC')

print 'ABC'.__len__() ##在len()函数内部,也是调用__len__方法
print 'ABC'.lower()

'''
对属性的操作
'''
print hasattr(bart , 'name')		##判断对象是否存在属性 name
print getattr(bart , 'name' , 404)	##获取对象属性name 如果不存在返回默认值 404
print setattr(bart , 'name' , 'Joke Stven')	##修改属性  !!???打印None????


'''
实例属性和类属性

'''

class ClassName(object):
	"""docstring for ClassName"""
	name = 'nameattr'
c = ClassName()
print '--------c.name',c.name
print 'ClassName.name',ClassName.name
c.name = 'C_NameAttr'
print '--------c.name' , c.name
print 'ClassName.name' , ClassName.name

del c.name  		##删除实例属性
print '--------c.name' , c.name 		##实力属性不存在,所以输出类属性


		
