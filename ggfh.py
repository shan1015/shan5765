l=int(input())
for i in range(0,100):
	if l==2**i:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("yes")
else:
	print("no")
