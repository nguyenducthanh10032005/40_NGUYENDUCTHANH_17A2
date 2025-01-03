from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry

class Demo_2(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()
def initGUI(self):
        self.parent.title("Khoa Khoa học ứng dụng")
        self.pack(fill=BOTH, expand=True)
        frame1 = Frame(self)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Giảng viên:", width=10)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)
        frame2 = Frame(self)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Bộ môn:", width=10)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)
        lbl3 = Label(frame3, text="Dự án:", width=10)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)
windows_root = Tk()
windows_root.geometry("320x200+320+200")
app = Demo_2(windows_root)
windows_root.mainloop()