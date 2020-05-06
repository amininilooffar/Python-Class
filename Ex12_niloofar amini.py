import tkinter as tk
win = tk. Tk()
lb1= tk.Label (win, text= 'User Name: ')
en1= tk.Entry(win)
lb1.config(background = "red")
lbl2= tk.Label (win, text = "Pass word: ")
lbl2.config(background= "red")
en2= tk.Entry(win)
def change():
	if en1.get()== "Admin" and en2.get()== "12345":
		btn1.config(bg="green")
	else:
		btn1.config(bg="red")

btn1= tk.Button(win, text= "log in", command= change)
lb1.pack()
en1.pack()
lbl2.pack()
en2.pack()
btn1.pack()
