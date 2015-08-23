# _*_ coding: utf-8 _*_
##########################################
##                                      ##
##            专治各种不服              ##
##                                      ##
##########################################

import math
import socket


print 'I'+' am OK!!'
print "I\''' am allright!!"
print "I\'m learning Python \n \tnow and ever...."
print r'\\\\\\t\\' #Python 允许使用r''表示''内部的字符串默认不转义


for x in xrange(1,10):
	print x


def func(a , b , c=10 , *args , **kw):
	print a , b , c , args , kw

func(3 , 4 , 55 , 3 , 'a' , 'r' , 41 , x='gg' , y='bb' , z='jj')

l = [x for x in range(10)]
print l[0:10:3]

print 5**2
print math.pow(5,2)

baiduip = socket.gethostbyname('www.baidu.com')		##理由网络库获取百度的ip
print baiduip