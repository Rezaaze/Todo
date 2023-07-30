def get_todos():
    """
    Read a text file and return the list of to-do items.
    """
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos):
    """
    Write teh to-do items list in the text file.
    """
    with open('todos.txt', 'w') as file:
        file.writelines(todos)
