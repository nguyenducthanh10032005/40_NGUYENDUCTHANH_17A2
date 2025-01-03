from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
#định nghĩa một lớp con có tên là Example, kế thừa từ lớp Frame trong Tkinter.
# Lớp Example đại diện cho ứng dụng.
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Ví dụ sử dụng Frame & Button")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=True)
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)
windows = Tk()
windows.geometry("300x200+300+300")
app = Example(windows)
windows.mainloop()