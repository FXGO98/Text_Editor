from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("SWord - Text Editor")
root.iconbitmap(r'C:\Users\franc\Desktop\Text_Editor\Custom-Icon-Design-Flatastic-1-Edit.ico')
root.geometry("1000x610")


# Create Main Frame
main_frame = Frame(root)
main_frame.pack(pady=(5, 2))


# Create our Scrollbar For the Text Box
text_scroll = Scrollbar(main_frame)
text_scroll.pack(side=RIGHT, fill=Y)


# Create Text Box
my_text = Text(main_frame, width=80, height=23, font=("Helvetica", 16), selectbackground="grey", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()


# Configure our Scrollbar
text_scroll.config(command=my_text.yview)


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)


# Add File Mneu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# Add File Mneu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")


# Add Status Bar To Bottom of App
status_bar = Label(root, text="Ready   ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


root.mainloop()