from logging import root
from tkinter import *
from tkinter import ttk
y = 0
a = ttk.Notebook()

frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root = ttk.Frame()

def quiz(y):
    a.add(frame1, text = "Q1")
    a.add(frame2, text = "Q2")
    a.add(frame3, text = "Q3")
    a.add(frame4, text = "Q4")
    a.add(frame5, text = "Q5")

    Label(frame1, text = "Which is a leyword?", font=("Arial", 50, "bold")).grid(row=2, column=2)
    Button(frame1, text="33", font=("Arial", 30, "bold"), bg="light blue", command=a1_right).grid(row=3, column=1)
    Button(frame1, text="31", font=("Arial", 30, "bold"), bg="light green", command=a1_wrong).grid(row=3, column=2)
    Button(frame1, text="33", font=("Arial", 30, "bold"), bg="light pink", command=a1_wrong).grid(row=3, column=3)

    Label(frame2, text="Output of 2**3 ?", font=("Arial", 50, "bold")).grid(row=2, column=2)
    Button(frame2, text="6", font=("Arial", 30, "bold"), bg="light blue",command=a2_wrong).grid(row=3, column=1)
    Button(frame2, text="8", font=("Arial", 30, "bold"), bg="light green", command=a2_right).grid(row=3, column=2)
    Button(frame2, text="9", font=("Arial", 30, "bold"), bg="light pink", command=a2_wrong).grid(row=3, column=3)

    Label(frame3, text="Output of np.arange (1,5) ?", font=("Arial", 50, "bold")).grid(row=2, column=2)
    Button(frame3, text="[1,2,3,4]", font=("Arial", 30, "bold"), bg="light blue",command=a3_wrong).grid(row=3, column=1)
    Button(frame3, text="[0,1,2,3,4]", font=("Arial", 30, "bold"), bg="light green", command=a3_right).grid(row=3, column=2)
    Button(frame3, text="[1,2,3,4,5]", font=("Arial", 30, "bold"), bg="light pink", command=a3_wrong).grid(row=3, column=3)

    Label(frame4, text="Keybword use to declare a function ?", font=("Arial", 50, "bold")).grid(row=2, column=2)
    Button(frame4, text="define", font=("Arial", 30, "bold"), bg="light blue",command=a4_wrong).grid(row=3, column=1)
    Button(frame4, text="def", font=("Arial", 30, "bold"), bg="light green", command=a4_right).grid(row=3, column=2)
    Button(frame4, text="None", font=("Arial", 30, "bold"), bg="light pink", command=a4_wrong).grid(row=3, column=3)

    Label(frame5, text="Output of 2*12 ?", font=("Arial", 50, "bold")).grid(row=2, column=2)
    Button(frame5, text="16", font=("Arial", 30, "bold"), bg="light blue", command=a5_wrong).grid(row=3, column=1)
    Button(frame5, text="24", font=("Arial", 30, "bold"), bg="light green",command=a5_right).grid(row=3, column=2)
    Button(frame5, text="59", font=("Arial", 30, "bold"), bg="light pink", command=a5_wrong).grid(row=3, column=3)


def a1_right():
    Label(frame1, text="Correct", font=("Arial", 50, "bold"),background="green",fg="yellow").grid(row=1, column=2)
    Label(frame1, text="Marks obtained : 1", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)

def a1_wrong():
    Label(frame1, text="Incorrect", font=("Arial", 50, "bold"),background="red",fg="yellow").grid(row=1, column=2)
    Label(frame1, text="Marks obtained : 0", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)




def a2_right():
    Label(frame2, text="Correct", font=("Arial", 50, "bold"),background="green",fg="yellow").grid(row=1, column=2)
    Label(frame2, text="Marks obtained : 1", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)

def a2_wrong():
    Label(frame2, text="Incorrect", font=("Arial", 50, "bold"),background="red",fg="yellow").grid(row=1, column=2)
    Label(frame2, text="Marks obtained : 0", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)




def a3_right():
    Label(frame1, text="Correct", font=("Arial", 50, "bold"),background="green",fg="yellow").grid(row=1, column=2)
    Label(frame1, text="Marks obtained : 1", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)

def a3_wrong():
    Label(frame3, text="Incorrect", font=("Arial", 50, "bold"),background="red",fg="yellow").grid(row=1, column=2)
    Label(frame3, text="Marks obtained : 0", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)




def a4_right():
    Label(frame4, text="Correct", font=("Arial", 50, "bold"),background="green",fg="yellow").grid(row=1, column=2)
    Label(frame4, text="Marks obtained : 1", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)

def a4_wrong():
    Label(frame4, text="Incorrect", font=("Arial", 50, "bold"),background="red",fg="yellow").grid(row=1, column=2)
    Label(frame4, text="Marks obtained : 0", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)




def a5_right():
    Label(frame5, text="Correct", font=("Arial", 50, "bold"),background="green",fg="yellow").grid(row=1, column=2)
    Label(frame5, text="Marks obtained : 1", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)

def a5_wrong():
    Label(frame5, text="Incorrect", font=("Arial", 50, "bold"),background="red",fg="yellow").grid(row=1, column=2)
    Label(frame5, text="Marks obtained : 0", font=("Arial", 50, "blod"), background="black", fg="white").grid(row=1,column=3)

quiz(y)

a.pack()

a.mainloop()
