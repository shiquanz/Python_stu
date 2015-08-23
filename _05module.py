#!/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import unicode_literals
'''
在python中,一个.py文件就称之为一个模块(Module)
好处在于提高代码的可维护性,其次编写代码不必从零开始,当一个模块编写完毕就可以被其他地方引用
使用模块可以避免函数名和变量名冲突,相同的名字完全可以分别存在不用模块中

为了避免不同的人编写的模块名相同,python引入了按目录组织模块的方法 称为包(Package)

每个包目录下必须各有一个__init__.py文件 否则python把目录当成普通目录而不是包
__init__.py本身就是一个模块,而模块名誉包名相同
'''


'a test module'  ## 该行表示模块的文档注释,任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Michael'

import sys		##导入模块

def test():
	args = sys.argv
	if len(args)==1:
		print 'Hello World'
	elif len(args)==2:
		print 'Hello, %s!' %args[1]
	else:
		print 'Too many arguments!!'

if __name__ == '__main__':
	test()

'''
当我们在命令行运行hello模块文件时，
Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
最常见的就是运行测试。
'''

'''
别名
'''
try:
	import cStringIO as StringIO
except ImportError:
	import StringIO

try:
	import json
except ImportError:
	import simplejson as json

'''
作用域
	一般定义的函数和变量是公开的(public),
	而_xxx 和__xxx 的函数或变量是非公开的(private)
	不应该被直接引用----玩不不需要引用的函数全部定义为private,只有外部需要引用的才定义为public
'''
def _private_1(name):
	return 'Hello , %s' %name

def _private_2(name):
	return 'Hi , %s' %name
def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)

print greeting('Jok')
## 这也是一种有用的代码封装和抽象的方法!!!

'''
第三方模块安装
	Python 安装第三方模块 是通过setuptools工具完成,
	而python有两个封装了该工具的包管理工具:easy_install 和pip  官方推荐pip
	在python安装过程中 确保勾选了pip
	在命令行下 >>pip install xxxx
'''

'''
模块搜索路径
	默认下,python会搜索当前目录 \所有已安装的那只模块和第三方模块.
	搜索路径存放在sys模块的path变量中
	>>>import sys
	>>>sys.path
	直接修改sys.path:
	>>>sys.path.append('/user/myname/my_python_scripts')
	或修改环境变量 PYTHONPATH
'''

'''
	__future__ 模块
		把下一个新版本的特性导入到当前版本中,在当前版本中测试新特性
'''
## from __future__ import unicode_literals 此行必须在文件开头写
print '\'xxxxx\' is unicode?' , isinstance('xxxxx' , unicode)
print 'u\'xxxxx\' is unicode?' , isinstance(u'xxxxx' , unicode)
print '\'xxxxx\' is str?' , isinstance('xxxxx' , str)
print 'b\'xxxxx\' is str?' , isinstance(b'xxxxx' , str)
'''
由于Python是由社区推动的开源并且免费的开发语言，不受商业公司控制，
因此，Python的改进往往比较激进，不兼容的情况时有发生。
Python为了确保你能顺利过渡到新版本，特别提供了__future__模块，
让你在旧的版本中试验新版本的一些特性。

'''