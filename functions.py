FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """reads the todos from the file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local,filepath=FILEPATH):
    """writes a list to a file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)
