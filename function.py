def get_todos(filepath="todoss.txt"):
    """Read a text file and return the list of todo item
    """
    with open(filepath, "r") as file_local:
         todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_args,filepath="todoss.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_args)


print(type(__name__))
if __name__ == "__main__":
     print("hello")

