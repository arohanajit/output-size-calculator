from tkinter import *
window = Tk()
window.title("Deep Learning Image Size Calculator")
window.geometry('500x300')
title_lbl = Label(window, text="Convolution Values",font=('bold',15))
title_lbl.grid(column=0,row=0)
lbl0 = Label(window, text="Image size: ")
lbl0.grid(column=0, row=1)
txt0 = Entry(window,width=10)
txt0.grid(column=1, row=1)
lbl1 = Label(window, text="Kernel Size: ")
lbl1.grid(column=0, row=2)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=2)
lbl2 = Label(window, text="Padding: ")
lbl2.grid(column=0, row=3)
txt2 = Entry(window,width=10)
txt2.grid(column=1, row=3)
lbl3 = Label(window, text="Stride: ")
lbl3.grid(column=0, row=4)
txt3 = Entry(window,width=10)
txt3.grid(column=1, row=4)
lbl4 = Label(window, text="")
lbl4.grid(column=5, row=3, padx=120)


def Convclicked():
	W,K,P,S = txt0.get(),txt1.get(),txt2.get(),txt3.get()
	flag = 0
	if len(W)==0 and len(S)==0 and len(P)==0 and len(S)==0:
		flag=1
		lbl4.configure(text="")
	if len(W)==0 or len(K)==0 or W=="0" or K=="0":
		lbl4.configure(text="Image/Kernel Size missing")
		flag = 1
	if len(S)==0:
		S="1"
	if len(P)==0:
		P="0"

	if flag==0:
		W,K,P,S = int(W),int(K),int(P),int(S)
		res = int(((W-K+(2*P))/S)+1)
		lbl4.configure(text=str(res)+"x"+str(res))

btn = Button(window, text="Output Size", command=Convclicked)
btn.grid(column=5, row=2, padx=120)


title_lbl1 = Label(window, text="Pooling Values",font=('bold',15))
title_lbl1.grid(column=0,row=5)
lbl5 = Label(window, text="Image size: ")
lbl5.grid(column=0, row=6)
txt5 = Entry(window,width=10)
txt5.grid(column=1, row=6)
lbl6 = Label(window, text="Kernel Size: ")
lbl6.grid(column=0, row=7)
txt6 = Entry(window,width=10)
txt6.grid(column=1, row=7)
lbl7 = Label(window, text="Padding: ")
lbl7.grid(column=0, row=8)
txt7 = Entry(window,width=10)
txt7.grid(column=1, row=8)
lbl8 = Label(window, text="Stride: ")
lbl8.grid(column=0, row=9)
txt8 = Entry(window,width=10)
txt8.grid(column=1, row=9)
lbl9 = Label(window, text="")
lbl9.grid(column=5, row=8, padx=120)


def Convclicked2():
	W,K,P,S = txt5.get(),txt6.get(),txt7.get(),txt8.get()
	flag = 0
	if len(W)==0 and len(S)==0 and len(P)==0 and len(S)==0:
		flag=1
		lbl9.configure(text="")
	if len(W)==0 or len(K)==0 or W=="0" or K=="0":
		lbl9.configure(text="Image/Kernel Size missing")
		flag = 1
	if len(S)==0:
		S="2"
	if len(P)==0:
		P="0"

	if flag==0:
		W,K,P,S = int(W),int(K),int(P),int(S)
		res = int(((W-K)/S)+1)
		lbl9.configure(text=str(res)+"x"+str(res))

btn2 = Button(window, text="Output Size", command=Convclicked2)
btn2.grid(column=5, row=7, padx=120)

window.mainloop()