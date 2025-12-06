import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import webbrowser
def open_website():
  url=simpledialog.askstring("Open Website","رابط الموقع")
  if url:
    if not url.startswith("http"):
      url="https://"+url
     webbrowser.open(url)
      print(f"Opening URL:{url}")
def click_me_command():
    print("Button Clicked")
root = tk.Tk()
root.title("My Custom GUI")
root.geometry("300x500")
root.configure(bg="#f7f7f7") 
btn = tk.Button(root, text="Click Me", fg="white", bg="#d6336c")
btn.pack(pady=8)
lbl = tk.Label(root, text="This is a label", bg="#ffeb99")
lbl.pack(pady=8)
entry_box = Entry(root, width=20)
entry_box.pack(pady=8)
txt_box = Text(root, width=20, height=10)
txt_box.pack(pady=8)
option_var = tk.StringVar(root)
radio1 = tk.Radiobutton(root, text="Option A", variable=option_var, value="A")
radio1.pack()
radio2 = tk.Radiobutton(root, text="Option B", variable=option_var, value="B")
radio2.pack()
check = tk.Checkbutton(root, text="I Agree")
check.pack(pady=8)
lst = Listbox(root)
lst.pack(pady=8)
lst.insert(1, "First")
lst.insert(2, "Second")
lst.insert(3, "Third")
lst.config(font=("Consolas", 12))
def open_website():
  url = simpledialog.askstring("Open Website","رابط الموقع")
  if url:
    if not url.startswith("http"):
      url = "https://" + url
    webbrowser.open(url)
    print(f"Opening URL:{url}")
open_btn = tk.Button(root, text="Open Website", bg="#4c6ef5", fg="white", command=open_website)
open_btn.pack(pady=10)
root.mainloop()
