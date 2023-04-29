while True:
    user_action = input("type add ,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action or "new" in user_action:
        todo = user_action[4:]+"\n"

        with open("todoss.txt", "r") as file:
             todos = file.readlines()

        todos.append(todo)

        with open("todoss.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("todoss.txt", "r") as file:
            todos = file.readlines()
        for index, i in enumerate(todos):
            i = i.strip("\n")
            row = f"{index + 1}-{i}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        with open("todoss.txt","r") as file:
            todos = file.readlines()
            print(todos)
        new_todo = input("enter todo") + "\n"
        todos[number] = new_todo
        with open("todoss.txt","w") as file:
           file.writelines(todos)
           print(todos)
    elif "complete" in user_action:
        number = int(user_action[9:])
        with open("todoss.txt","r") as file:
          todos = file.readlines()
          todos.pop(number)
        with open("todoss.txt","w") as file:
            file.writelines(todos)
    elif "exit" in user_action:
       break
print("bye")
