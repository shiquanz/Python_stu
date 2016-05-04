tupl = 'city' , 'name' , 'age'
lis1 = ['city' , 'name' , 'age']
dic = {}
#print len(tupl)
print len(lis1)
for x in tupl:
    print x
    dic.update([(x , "None") ])
print dic
