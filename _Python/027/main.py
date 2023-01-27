import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Day 27")
window.minsize(width=500, height=300)


label = tkinter.Label(text='this is label by me', font=('Nunito', 24, 'italic'))
label.pack()

label['text'] = "this is new text"
label.config(text='this is another new text')

def button_clicked():
    label['text'] = 'button got clicked'
    print("button clicked")
    user_input = input.get()
    label.config(text=user_input)

button = tkinter.Button(text='hello', command=button_clicked)
button.pack()


input = tkinter.Entry(width=200)
input.pack()
user_input = input.get()

def spinBox_used():
    print('hello from spin box', spinBox.get())

spinBox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinBox_used)
spinBox.pack()

def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

def checkButton_used():
    print(checkedState.get())

checkedState = IntVar()
checkBox = tkinter.Checkbutton(text="is On?", variable=checkedState, command=checkButton_used)
checkedState.get()
checkBox.pack()

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radioBtn1 = tkinter.Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radioBtn2 = tkinter.Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radioBtn1.pack()
radioBtn2.pack()

def listBox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ['Apple', 'Mango', 'Banana', 'Orange']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listBox_used)
listbox.pack()





window.mainloop()