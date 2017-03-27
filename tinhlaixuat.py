def bai1(t,n,k):
	for i in range(k):
		n=n+n*t/100
	print "tong tien nhan duoc la:"
	print n
if __name__=="__main__":
	t=float(raw_input("Nhap lai suat:"))
	n=float(raw_input("nhap so tien gui ban dau:"))
	k=int(raw_input("nhap so thang gui:"))
	bai1(t,n,k)
