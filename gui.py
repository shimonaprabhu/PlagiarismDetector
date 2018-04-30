from tkinter import *
import os
#a=10
#def donothing():
#   os.system('python hashfiles.py a')
   #print(var.get())
#os.system('python indexsize.py')
def get():
	#print(e.get())
	filenm=e.get()
	option=d.get()
	handle=open('indexfile','r')
	index_search={}
	for line in handle:
		a=line.split()
		#print(a[0])
		#print(a[1:])
		index_search[a[0]]=(a[1:])
	size=os.stat(filenm).st_size
	if str(size) in index_search.keys():
		file_list=index_search[str(size)]
	for i in file_list:
		#print(i)	
		cmd='python3 hashfiles.py '+i
		os.system(cmd)
	cmd2='python3 del.py '+option
	os.system(cmd2)
	root1=Tk()
	root1.title('Alert!')
	root1.configure(background="white")
	root1.geometry("500x50") 
	if(int(option)==1):
		Label1=Label(root1,text="Duplicate files have been deleted",bg="white",font=("Arial", 12))
		Label1.pack()
	else:
		Label2=Label(root1,text="Duplicate files have been moved to Bin folder",bg="white",font=("Arial", 12))
		Label2.pack()
	root1.mainloop()
	#print(size)
	#print(index_search)
	#cmd='python3 hashfiles.py '+e.get()
	#os.system(cmd)
root = Tk()
root.title('File Structures')
root.configure(background="white")
root.geometry("400x400") 
theLabel1=Label(root,text="FILE APPLICATION",bg="blue",fg="white",height=5,font=("Arial", 16))
theLabel1.pack(fill=X)
theLabel2=Label(root,text="Select filename",bg="white",font=("Arial", 10))
theLabel2.pack(fill=X, pady=20)

#menu=Menu(root)
#root.config(menu=menu,height=10)
arr = [x for x in os.listdir("/home/shimona/fs") if x.endswith(".txt")]
#subMenu=Menu(menu)
#menu.add_cascade(label="Choose file from current directory",menu=subMenu)
#for i in range(len(arr)):
#	subMenu.add_command(label=arr[i],command=donothing)
#var = StringVar(root)
#var.set('shimona')
e = Entry(root, width=25)
e.pack(pady=20)
theLabel3=Label(root,text="Select option 1. Delete File 2. Move to new directory",bg="white",font=("Arial", 10))
theLabel3.pack(fill=X, pady=20)
d = Entry(root, width=25)
d.pack(pady=20)
Button1 = Button(root, text="Enter", command=get)
Button1.pack()





#subMenu.add_separator()

'''topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

button1=Button(topframe,text="Button 1",fg="red")
button2=Button(topframe,text="Button 2",fg="purple")
button3=Button(bottomframe,text="Button 3",fg="green")
button4=Button(bottomframe,text="Button 4",fg="blue")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=BOTTOM)
button4.pack(side=BOTTOM)'''

root.mainloop()
