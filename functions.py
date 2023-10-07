FILEPATH = "todos.txt"


def get_todos(path=FILEPATH):
    """Gets list of todos from text file and returns them in a list"""
    with open(path, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos_to_write, path=FILEPATH):
    """Writes todos to a text file"""
    with open(path, "w") as file:
        file.writelines(todos_to_write)
