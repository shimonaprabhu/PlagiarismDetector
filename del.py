import os
import sys
option=sys.argv[1]
handle=open('hashcontent','r')
a=handle.read()
array=a.split('\n')
array.pop()

k=0
c={}
for i in array:
	(key,value)=array[k].split()
	if key in c:
		c[key].append(value)
	else:
		c[key]=[value]
	k=k+1

b=[]
for i in c:
	if (len(c[i])>1):
		b.append(c[i])

for i in b:
	for j in i[1:]:
		if(int(option)==1):
			os.remove(j)
		else:
			os.rename("/home/shimona/fs/"+j, "/home/shimona/fs/Bin/"+j)


































