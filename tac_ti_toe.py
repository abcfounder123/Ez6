
"""

Step.1  -->  Create root


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

x.mainloop()

#########################################

Step.2  --> button, grid


          C0     C1     C2                C9

row 0     B1     B2     B3
row 1     B4     B5     B6
row 2     B7     B8     B9

B1 = row 0, C0
B2 = row 0, C1
B5 = row 1, C1
B9 = row 2, C2


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

Button(x, width=8, height=4, text="B1", font=('Arial', 30, 'bold')).grid(row=0, column=0)

x.mainloop()

#########################################

Step.3  -->   label


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=8, height=4, text="B1", font=('Arial', 30, 'bold'))
b1.grid(row=0, column=0)

x.mainloop()

#########################################

Step.4  -->  button 3, 9


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=8, height=4, text="B1", font=('Arial', 30, 'bold'))
b2 = Button(x, width=8, height=4, text="B2", font=('Arial', 30, 'bold'))
b3 = Button(x, width=8, height=4, text="B3", font=('Arial', 30, 'bold'))

b4 = Button(x, width=8, height=4, text="B4", font=('Arial', 30, 'bold'))
b5 = Button(x, width=8, height=4, text="B5", font=('Arial', 30, 'bold'))
b6 = Button(x, width=8, height=4, text="B6", font=('Arial', 30, 'bold'))

b7 = Button(x, width=8, height=4, text="B7", font=('Arial', 30, 'bold'))
b8 = Button(x, width=8, height=4, text="B8", font=('Arial', 30, 'bold'))
b9 = Button(x, width=8, height=4, text="B9", font=('Arial', 30, 'bold'))


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

x.mainloop()

#########################################

Step.5  -->  nested loop

for row in range(3): # 0
    for col in range(3): # 0 1 2
        print(row, col) # 0 0, 0 1, 0 2

0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2

#########################################

Step.6    -->   B1, B2, B3, ..., B9

from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

n = 1
for row in range(3):
    for col in range(3):
        Button(x, width=8, height=4, text=f"B{n}", font=('Arial', 30, 'bold')).grid(row=row, column=col)
        n += 1

x.mainloop()

#########################################

Step.7    -->  empty_text = ''


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for col in range(3):
        Button(x, width=8, height=4, text='', font=('Arial', 30, 'bold')).grid(row=row, column=col)

x.mainloop()

##################################################################################

Step.8  -->  if click b1, show X

=> command=f


def f():
    b1["text"] = 'X'
    

##################################################################################
    
from tkinter import *


def f():
    b1["text"] = "X"


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, command=f, width=8, height=4, text='', font=('Arial', 30, 'bold'))
b1.grid(row=0, column=0)

x.mainloop()

##################################################################################

Step.9  -->  Switch player   ( X and O )


def switch_player():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


s = "X"
print(s)

switch_player()
print(s)

##################################################################################

Step.8 + Step.9


from tkinter import *


s = "X"


def switch_player():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


def f():
    b1["text"] = s
    switch_player()


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, command=f, width=8, height=4, text='', font=('Arial', 30, 'bold'))
b1.grid(row=0, column=0)

x.mainloop()

##################################################################################

Step.10  -->  Control to draw once

If text value is somthing, do nothing.
Else, Draw s and Switch player.

def f():
    if b1['text']:
        pass
    else:
        b1["text"] = s
        switch_player()

#########################################

If text value is not somthing, Draw s and Switch player.

def f():
    if not b1['text']:
        b1["text"] = s
        switch_player()

#########################################

If text value is somthing, do nothing and stop function.
If not stop, continue following program.

def f():
    if b1['text']:
        return
    b1["text"] = s
    switch_player()

#########################################


from tkinter import *


s = "X"


def switch_player():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


def f():
    if b1["text"]:
        pass
    else:
        b1["text"] = s
        switch_player()


def f2():
    if b2["text"]:
        pass
    else:
        b2["text"] = s
        switch_player()


def f3():
    if b3["text"]:
        pass
    else:
        b3["text"] = s
        switch_player()


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, command=f, width=8, height=4, text='', font=('Arial', 30, 'bold'))
b1.grid(row=0, column=0)

b2 = Button(x, command=f2, width=8, height=4, text="", font=('Arial', 30, 'bold'))
b2.grid(row=0, column=1)

b3 = Button(x, command=f3, width=8, height=4, text="", font=('Arial', 30, 'bold'))
b3.grid(row=0, column=2)

x.mainloop()

##################################################################################

Step.11  -->  Functions for each data and Function for every data

Functions for each data


d1 = {'text': ''}
d2 = {'text': ''}
d3 = {'text': ''}


def f1():
    d1["text"] = 'apple'

def f2():
    d2["text"] = 'banana'

def f3():
    d3["text"] = 'orange'


f1()
f2()
f3()

print(d1)
print(d2)
print(d3)

#########################################

Function for every data


d1 = {'text': ''}
d2 = {'text': ''}
d3 = {'text': ''}


def f(x):
    x['text'] = 'apple'


f(d1)
f(d2)
f(d3)

print(d1)
print(d2)
print(d3)

#########################################

Functions for each button

def f1():
    b1["text"] = 'X'

def f2():
    b2["text"] = 'X'

def f3():
    b3["text"] = 'X'


Function for every buttons

def f(e):
    e.widget["text"] = 'X'

#########################################


def f(e):
    print(e.widget)  # .!button,  .!button2  .!button3


#########################################


def f1():
    if not b1['text']:
        b1["text"] = s
        switch_player()


def f2():
    if not b2['text']:
        b2["text"] = s
        switch_player()


def f(e):
    b = e.widget
    if not b['text']:
        b["text"] = s
        switch_player()

#########################################

Functions for each button


from tkinter import *


s = "X"


def switch_player():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


def f1():
    if not b1['text']:
        b1["text"] = s
        switch_player()


def f2():
    if not b2['text']:
        b2["text"] = s
        switch_player()


def f3():
    if not b3['text']:
        b3["text"] = s
        switch_player()


def f4():
    if not b4['text']:
        b4["text"] = s
        switch_player()


def f5():
    if not b5['text']:
        b5["text"] = s
        switch_player()


def f6():
    if not b6['text']:
        b6["text"] = s
        switch_player()


def f7():
    if not b7['text']:
        b7["text"] = s
        switch_player()


def f8():
    if not b8['text']:
        b8["text"] = s
        switch_player()


def f9():
    if not b9['text']:
        b9["text"] = s
        switch_player()

x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f1)
b1.grid(row=0, column=0)
b2 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f2)
b2.grid(row=0, column=1)
b3 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f3)
b3.grid(row=0, column=2)

b4 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f4)
b4.grid(row=1, column=0)
b5 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f5)
b5.grid(row=1, column=1)
b6 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f6)
b6.grid(row=1, column=2)

b7 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f7)
b7.grid(row=2, column=0)
b8 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f8)
b8.grid(row=2, column=1)
b9 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f9)
b9.grid(row=2, column=2)

x.mainloop()

#########################################

Function for every buttons


from tkinter import *


s = "X"


def switch_player():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


def f(e):
    b = e.widget
    if b['text']:
        pass
    else:
        b["text"] = s
        switch_player()


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for col in range(3):
        b = Button(x, width=8, height=4, text='', font=('Arial', 30, 'bold'))
        b.grid(row=row, column=col)
        b.bind("<Button-1>", f)

x.mainloop()

##################################################################################


"""
