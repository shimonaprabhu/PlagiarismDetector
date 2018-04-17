#indicate original file
import os
import datetime
#list all the files and find the creation time for all
arr = [x for x in os.listdir("/home/shimona/fs") if x.endswith(".txt")]
for i in range(len(arr)):
	#convert to date format yyyy-mm-dd hh:mm:ss.ms
	print(datetime.datetime.fromtimestamp(os.path.getctime(arr[i])))
