
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def toggle(tog=[0]):
    '''
    a list default argument has a fixed address
    '''
    tog[0] = not tog[0]
    if tog[0]:
        t_btn.config(text='False')
    else:
        t_btn.config(text='True')

root = tk.Tk()

t_btn = tk.Button(text="True", width=12, command=toggle)
t_btn.pack(pady=5)

root.mainloop()