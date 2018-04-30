

handle=open('indexfile','r')
index_search={}
for line in handle:
	a=line.split()
	#print(a[0])
	#print(a[1:])
	index_search[a[0]]=(a[1:])
print(index_search)
