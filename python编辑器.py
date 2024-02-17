import ttkbootstrap as tk
#from ttkbootstrap import style
from ttkbootstrap.constants import *
from tkinter.filedialog import *

#style = style.Style(theme="superhero")
#root = style.master
root = tk.Window()
root.title("python编辑器")

text = tk.Text(root)
text.config(font=('Arial', 12), wrap='word')
text.pack(side="bottom")

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

botton1 = tk.Button(root,text="保存",bootstyle=(INFO,OUTLINE),command=save)
botton1.pack(side="left")

button2 = tk.Button(root,text="运行",bootstyle=(INFO,OUTLINE),command=run)
button2.pack(side="left")

button3 = tk.Button(root,text="清空",bootstyle=(INFO,OUTLINE),command=delet)
button3.pack(side="left")

button4 = tk.Button(root,text="打开",bootstyle=(INFO,OUTLINE),command=file)
button4.pack(side="left")

root.mainloop()
