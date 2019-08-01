n=input()
k=""
l=[]
for i in n:
	l.append(n.count(i))
min1=min(l)
for i in n:
	if n.count(i)==min1 and i!=" ":
		k=k+i.lower()+" "
print(k.strip())
