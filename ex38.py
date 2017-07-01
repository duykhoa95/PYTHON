tudien = " doan duy khoa"

print tudien

tudien2 = tudien.split(' ')

more_tudien2 = ["duy","hung","hoan"]

while True :
	next_one = more_tudien2.pop(0)
	print "Adding %r" % next_one
	tudien2.append(next_one)
	print "lengt %r" %len(tudien2)
	
	if len(tudien2) == 5 :
		break
		
		
print(tudien2[-1])
print(tudien2[1])