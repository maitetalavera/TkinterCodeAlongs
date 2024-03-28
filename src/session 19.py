import tkinter as tk

window = tk.Tk()

# text_box=tk.Text()
# text_box.pack()

# text_box.insert("1.0", "Hello")
# text_box.insert("2.0", "\nWorld")
# text_box.insert(tk.END, "\nPut me at the end!")

# text=text_box.get("1.0")
# # text=text_box.get("2.0", tk.END)

# text_box.delete("1.0", "1.5")
# text_box.delete("1.0", tk.END)
# print(text)

frm_a=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
frm_b=tk.Frame()

lbl_a=tk.Label(master=frm_a, text="I'm in Frame A", bg="red")
lbl_a.pack()
lbl_b=tk.Label(master=frm_b, text="I'm in Frame B", bg="blue")
lbl_b.pack()

frm_a.pack()
frm_b.pack()

border_effects={
    "flat":tk.FLAT, 
    "sunken":tk.SUNKEN, 
    "raised":tk.RAISED,
    "groove":tk.GROOVE,
    "ridge":tk.RIDGE
}

window.mainloop()