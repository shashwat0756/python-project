import function
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todoss.txt"):
    with open("todoss.txt","w") as file:
       pass

sg.theme("Black")
clock = sg.Text("",key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo",key = "todo")
add_button = sg.Button("Add" ,tooltip = "Add items",key = "Add")
list_box = sg.Listbox(values=function.get_todos(),key = "todos",enable_events = True,size =[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-do App",layout=[[clock],[label],[input_box],[add_button],[list_box,edit_button,complete_button],[exit_button]],font=("vintage",20))
while True:
   event,values = window.read(timeout=200)
   window["clock"].update(value=time.strftime(("%b %d %Y %H %M: %S")))
   print(event)
   print(values)
   match event:
       case "Add":
           todos = function.get_todos()
           new_todo = values["todo"] + "\n"
           todos.append(new_todo)
           function.write_todos(todos)
           window["todos"].update(values=todos)

       case "Edit":
           try:
               todo_1 = values["todos"][0]
               new_todo = values["todo"]
               todos = function.get_todos()
               index = todos.index(todo_1)
               todos[index] = new_todo + "\n"
               function.write_todos(todos)
               window["todos"].update(values=todos)
           except IndexError:
               sg.popup("Please select an item",font =("helvetica",20))

       case "Complete":
           try:
               todos_to_complete = values["todos"][0]
               todos = function.get_todos()
               todos.remove(todos_to_complete)
               function.write_todos(todos)
               window["todos"].update(values=todos)
           except IndexError:
               sg.popup("Please select an item",font =("helvetica",20) )

       case "Exit":
           break


       case sg.WIN_CLOSED:
           break
print("bye")
window.close()