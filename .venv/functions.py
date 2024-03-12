FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text File and return a list of to-do items
    :param filepath: todos.txt
    :return: todos_item_list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write todos list to the file todos.txt
    :param todos_arg: todos_list
    :param filepath: todos.txt
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
