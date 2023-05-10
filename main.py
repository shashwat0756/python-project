import function
import time

now = time.strftime("%b %d %Y %H %M: %S")
print(now)

while True:
    """
    Read input from function file"""
    user_action = input("type add ,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]+"\n"

        todos = function.get_todos()



        todos.append(todo)

        function.write_todos(todos,"todoss.txt")


    elif user_action.startswith("show"):

        todos = function.get_todos()

        for index, i in enumerate(todos):
            i = i.strip("\n")
            row = f"{index + 1}-{i}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = function.get_todos()
            print(todos)
            new_todo = input("enter todo") + "\n"
            todos[number] = new_todo
            function.write_todos(todos, "todoss.txt")
            print(todos)
        except ValueError:
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = function.get_todos()
            todos.pop(number)

            function.write_todos(todos, "todoss.txt")
        except IndexError:
            print("invalid command")
            continue
    elif "exit" in user_action:
       break
print("bye")
print("gui interface")
