import tkinter as tk
root = tk.Tk()

ans = 0
tocalculate = tk.IntVar()

entry = tk.Entry(root, textvariable=tocalculate)

entry.pack()

def Sum():
    global ans
    ans+=tocalculate.get()
    tocalculate.set(ans)

ansLabel = tk.Label(root, textvariable=tocalculate)
ansLabel.pack()

button_calc = tk.Button(root, text="Calculate", command=Sum)
button_calc.pack()

root.mainloop()