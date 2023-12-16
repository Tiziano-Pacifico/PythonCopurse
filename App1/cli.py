from modules import functions as f
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add,show, edit, exit, complete: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = f.get_todos()

        todos.append(todo)

        f.write_todos(todos)

    elif user_action.startswith("show"):
        todos = f.get_todos()

        new_todos = [item.strip("\n") for item in todos]

        for i, item in enumerate(new_todos):
            row = f"{i+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = f.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            f.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = f.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            f.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid")


print("Bye")
