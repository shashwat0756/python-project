def get_todos(filepath):
    with open(filepath, "r") as file_local:
         todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath,todos_args):
    with open(filepath, "w") as file:
        file.writelines(todos_args)



while True:
    user_action = input("type add ,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]+"\n"

        todos = get_todos("todoss.txt")



        todos.append(todo)

        write_todos("todoss.txt",todos)


    elif user_action.startswith("show"):

        todos = get_todos("todoss.txt")

        for index, i in enumerate(todos):
            i = i.strip("\n")
            row = f"{index + 1}-{i}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos("todoss.txt")
            print(todos)
            new_todo = input("enter todo") + "\n"
            todos[number] = new_todo
            write_todos("todoss.txt", todos)
            print(todos)
        except ValueError:
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos("todoss.txt")
            todos.pop(number)

            write_todos("todoss.txt", todos)
        except IndexError:
            print("invalid command")
            continue
    elif "exit" in user_action:
       break
print("bye")

