import functions
import PySimpleGUI as sg


label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button('Edit')

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box,add_button],[list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, val = window.read()
    print(event)
    print(val)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = val['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = val['todos'][0]
            new_todo = val['todo'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=val['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()