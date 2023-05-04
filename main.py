def get_todos(filepath="todoss.txt"):
    with open(filepath, "r") as file_local:
         todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_args,filepath="todoss.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_args)



while True:
    user_action = input("type add ,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]+"\n"

        todos = get_todos()



        todos.append(todo)

        write_todos(todos)


    elif user_action.startswith("show"):

        todos = get_todos()

        for index, i in enumerate(todos):
            i = i.strip("\n")
            row = f"{index + 1}-{i}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos()
            print(todos)
            new_todo = input("enter todo") + "\n"
            todos[number] = new_todo
            write_todos(todos, "todoss.txt")
            print(todos)
        except ValueError:
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todos.pop(number)

            write_todos(todos, "todoss.txt")
        except IndexError:
            print("invalid command")
            continue
    elif "exit" in user_action:
       break
print("bye")