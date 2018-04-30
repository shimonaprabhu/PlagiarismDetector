'''execute commands using python'''
#import os
#i=0
#cdcmd="cd File"
#os.system(cdcmd)
#cmd = "ls -p File | grep -v /" #list the files
#listfiles=os.system(cmd)
#print(listfiles)
#print(type(listfiles))	# returns the exit code in unix
#print('returned value:', returned_value)
'''opening index file and storing size of all files in an index file'''
#handle=open('indexfile.txt')
#statinfo = os.stat('page1.txt')
#statinfo.st_size
#from os import walk
#for dirpath,dirnames,filenames in walk('/home/shimona/fs'):
#    print(filenames)
#    statinfo = os.stat(filenames[2])
#    statinfo.st_size
#    i=i+1; 
#if index_entry.has_key(os.stat(arr[i]).st_size):

import os
'''Create a dictionary to enter values of the size of files as keys and names of the files as the values'''
index_entry = {}
'''List all the files in the current directory, that are text files'''
arr = [x for x in os.listdir("/home/shimona/fs") if x.endswith(".txt")]
#print(arr)
'''Open the index file for writing'''
handle=open('indexfile','a')
'''for every file, we check if the size is already present as a key. If not, we add an entry. If yes, we append. We use os system methods for the same.'''
for i in range(len(arr)):
	#print(os.stat(arr[i]).st_size)
	if (os.stat(arr[i]).st_size in index_entry):
		index_entry[os.stat(arr[i]).st_size].append(arr[i])
	else:
		index_entry[os.stat(arr[i]).st_size] = [ arr[i] ]
'''For every key, every file name is mapped to it's key in the index file.'''
index_keys = index_entry.keys()
for i in index_keys:
            list_index = index_entry[i]
            handle.write(str(i)+ " ")
            for index in list_index:
                handle.write(index+" ")
            handle.write("\n")
'''Successful completion of index file.'''


	
	


