from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M;%S")
print("It is" , now)
while True:
    user_action = input("Type add or show, edit, complete or exit:").strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()
        todos.append(todo)
        write_todos(todos)


    elif user_action.startswith('show'):

        todos = get_todos()

        todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            print("{0}-{1}".format(index + 1, item))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            new_todo = input('Enter new todo: ') + '\n'
            todos = get_todos()
            todos[number] = new_todo
            write_todos(todos)
        except ValueError:
            print('Your command is not vaild.')


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            r_item = todos.pop(number - 1)
            write_todos(todos)

            print("{} was removed".format(r_item.strip('\n')))
        except IndexError:
            print('There is no Item with that number.')
    elif user_action.startswith('exit'):
        break

    else:
        print('Command is not valid')
print('bye!')
