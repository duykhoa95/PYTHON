so = [1,2,3,6,5]
chu = ["khoa","hung","hoang","tung"]
chu_so = ["khoa",1,"hung",2]

for i in so:
	print "day la so %d " % i
	
for i in chu :
	print "Chu  la   %s " % i
	
for i in chu_so :
	print " Chu so %r " % i
	
append = []

for i in range(0,6) :
	append.append(i)
	
for i in append :
	print "append %r" % i