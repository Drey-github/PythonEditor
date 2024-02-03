import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
root.title("python编辑器")

text = tk.Text(root)
text.config(font=('Arial', 12), wrap='word')
text.config(height=10, width=50)
text.pack()

def save():
	filenewpath = asksaveasfilename(defaultextension='.py')
	if filenewpath != "":
		f = open(filenewpath,"w")
		f.write(text.get("1.0","end"))
		f.close()

def run():
	exec(text.get("1.0","end"))

def delet():
    text.delete('1.0', 'end')

def file():
	path = askopenfilename()
	if path != "":
		f = open(path,"r")
		a = f.read()
		f.close()
		text.insert("end",a)

botton1 = tk.Button(root,text="保存",command=save)
botton1.pack()

button2 = tk.Button(root,text="运行",command=run)
button2.pack()

button3 = tk.Button(root,text="清空",command=delet)
button3.pack()

button4 = tk.Button(root,text="打开",command=file)
button4.pack()

root.mainloop()