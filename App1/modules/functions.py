FILEPATH = "files/todos.txt"
def get_todos(filepath=FILEPATH):
    """

    :param filepath:
    :return:
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
else:
    print("Volevo essere main")