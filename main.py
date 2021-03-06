
import tkinter as tk
# from scale.s1 import window

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_all_widgets()

    def create_all_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(
            self, text="QUIT", fg="red", 
            command=self.master.destroy
        )
        self.quit.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x200') 
    app = Application(master=root)
    app.mainloop()
