l=int(input())
k=""
for i in range(1,l+1):
	for j in range(1,l+1):
		if i*j==l:
			if i%2==0:
				k=k+str(i)+" "
print(k.strip())
