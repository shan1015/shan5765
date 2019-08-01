n1,s2=map(str,input().split())
c=max(len(n1),len(s2))
s=0
for i in range(c):
	if n1[i]!=s2[i]:
		s=s+1
if s==1:
	print("yes")
else:
	print("no")
