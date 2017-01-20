from Tkinter import *
from tkFileDialog import *

filename = "Untitled"
docTitle = ""
lastName = ""
fullName = ""
teachName = ""
className = ""
dueDate = ""


def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops", message="Unable to save file")

def openFile():
    global filename
    f = askopenfile(mode='r')
    t = f.read()
    filename = f.name
    text.delete(0.0, END)
    text.insert(0.0, t)

def printTest():
    print("It Worked!")
    return

def popupTitle():
    popup = Tk()
    def titleChange():
        global docTitle
        docTitle = eBox.get()
        popup.quit()
        popup.destroy()
    popup.minsize(width=200,height=80)
    popup.maxsize(width=200,height=80)
    popup.title("Title")
    label = Label(popup, text="Enter Your Document Title")
    label.pack(side=TOP)
    v = StringVar()
    eBox = Entry(popup, textvariable=v)
    eBox.pack()
    OK = Button(popup, text="O.K.", command=titleChange)
    OK.pack(side=BOTTOM)
    popup.mainloop()

def popupName():
    popup = Tk()
    def nameChange():
        global lastName
        lastName = eBox.get()
        popup.quit()
        popup.destroy()
    popup.minsize(width=200,height=80)
    popup.maxsize(width=200,height=80)
    popup.title("Title")
    label = Label(popup, text="Enter Your Last Name")
    label.pack(side=TOP)
    v = StringVar()
    eBox = Entry(popup, textvariable=v)
    eBox.pack()
    OK = Button(popup, text="O.K.", command=nameChange)
    OK.pack(side=BOTTOM)
    popup.mainloop()

def popupFullName():
    popup = Tk()
    def fullNameChange():
        global fullName
        fullName = eBox.get()
        popup.quit()
        popup.destroy()
    popup.minsize(width=200,height=100)
    popup.maxsize(width=200,height=100)
    popup.title("Full Name")
    label = Label(popup, text="Enter Your Full Name \n Ex: \"Steven P. Jobs\"")
    label.pack(side=TOP)
    v = StringVar()
    eBox = Entry(popup, textvariable=v)
    eBox.pack()
    OK = Button(popup, text="O.K.", command=fullNameChange)
    OK.pack(side=BOTTOM)
    popup.mainloop()

def popupteachName():
    popup = Tk()
    def teachNameChange():
        global teachName
        teachName = eBox.get()
        popup.quit()
        popup.destroy()
    popup.minsize(width=200,height=100)
    popup.maxsize(width=200,height=100)
    popup.title("Teahers Name")
    label = Label(popup, text="Enter Your Teachers Name \n Ex: \"Prof.Jobs\"")
    label.pack(side=TOP)
    v = StringVar()
    eBox = Entry(popup, textvariable=v)
    eBox.pack()
    OK = Button(popup, text="O.K.", command=teachNameChange)
    OK.pack(side=BOTTOM)
    popup.mainloop()

def popupClassName():
    popup = Tk()
    def classNameChange():
        global className
        className = eBox.get()
        popup.quit()
        popup.destroy()
    popup.minsize(width=200,height=100)
    popup.maxsize(width=200,height=100)
    popup.title("Class Name")
    label = Label(popup, text="Enter The Name Of The Class \n Ex: \"CS 201\"")
    label.pack(side=TOP)
    v = StringVar()
    eBox = Entry(popup, textvariable=v)
    eBox.pack()
    OK = Button(popup, text="O.K.", command=classNameChange)
    OK.pack(side=BOTTOM)
    popup.mainloop()

def popupDueDate():
    popup = Tk()
    def dueDateChange():
        global dueDate
        dueDate = eBox.get()
        popup.quit()
        popup.destroy()
    popup.minsize(width=200,height=100)
    popup.maxsize(width=200,height=100)
    popup.title("Due Date")
    label = Label(popup, text="Enter Your Assignments due date")
    label.pack(side=TOP)
    v = StringVar()
    eBox = Entry(popup, textvariable=v)
    eBox.pack()
    OK = Button(popup, text="O.K.", command=dueDateChange)
    OK.pack(side=BOTTOM)
    popup.mainloop()
# menu tab functons
#file tab
def cut():
    root.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST,index2=SEL_LAST)
def copy():
    root.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
def paste():
    text.insert(INSERT, root.clipboard_get())
def delete():
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)
def selectAll():
    text.tag_add(SEL, "1.0", END)
def APA():
    text.config(font=("Times New Roman", 12))
    popupTitle()
    global docTitle
    text.insert(0.0,"\t\t\t\t\t1\n\n\t\t\t" + docTitle + "\n")
def MLA():
    text.config(font=("Times New Roman", 12))
    global teachName
    global lastName
    global fullName
    global className
    global dueDate
    global docTitle
    popupName()
    popupFullName()
    popupClassName()
    popupteachName()
    popupDueDate()
    popupTitle()
    text.insert(0.0, "\t\t\t\t\t" + lastName + " 1\n" + fullName + "\n" + teachName + "\n" + className + "\n" + dueDate + "\n" + "\t" + docTitle + "\n" + "\t")
def bold():
    current_tags = text.tag_names("sel.first")
    if "bt" in current_tags:
        text.tag_remove("bt", "sel.first", "sel.last")
    else:
        text.tag_add("bt", "sel.first", "sel.last")
def leftMargin():
    print("APA")
def rightMargin():
    print("APA")
def itallic():
    print("APA")
def underLine():
    print("APA")
def fontSize():
    print("APA")
def font():
    print("APA")

root = Tk()
root.title("College Ruled")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.minsize(width=400, height=400)
root.maxsize(width=3840, height=2160)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
#file tab
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
#edit tab
editmenu = Menu(menubar)
editmenu.add_command(label="Undo", command=text.edit_undo)
editmenu.add_command(label="Redo", command=text.edit_redo)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_command(label="Delete", command=delete)
editmenu.add_command(label="Select All", command=selectAll)
menubar.add_cascade(label="Edit", menu=editmenu)
#format tab
formatmenu = Menu(menubar)
formatmenu.add_command(label="APA", command=APA)
formatmenu.add_command(label="MLA", command=MLA)
formatmenu.add_command(label="Left Margin", command=leftMargin)
formatmenu.add_command(label="Right MArgin", command=rightMargin)
formatmenu.add_command(label="Bold", command=bold)
formatmenu.add_command(label="Itallic", command=itallic)
formatmenu.add_command(label="Under Line", command=underLine)
formatmenu.add_command(label="Font Size", command=fontSize)
formatmenu.add_command(label="Font", command=font)
menubar.add_cascade(label="Format", menu=formatmenu)
root.config(menu=menubar)
root.mainloop()