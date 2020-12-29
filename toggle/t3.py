try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def toggle():
    index_dict={"True": "False", "False": "True"}
    index[0] = index_dict[index[0]]
    t_btn['text'] = index[0]

root = tk.Tk()
index=["True"]
t_btn = tk.Button(text=index[0], width=12, command=toggle)
t_btn.pack(pady=5)

root.mainloop()