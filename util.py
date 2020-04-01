import os, json

usage = '''Usage:
python pycut.py [Option]

Option:
-n --new <name> <path>: Create a new shortcut
-o --open <name>: Open a shortcut
-i --info <name>: View the information of a shortcut
-l --list: View the list of shortcuts
-m --modify [-n --name][-p --path] <name> <change>: Modify the name and/or the path of a shortcut
-d --delete <name>: Delete a shortcut
'''

path = os.path.join(os.path.dirname(__file__), 'data.json')

data = {}

def exist(name):
    return name in data

def load():
    with open(path, 'r') as file:
        data = json.loads(file.readline())
    return data

def save(data):
    with open(path, 'w') as file:
        file.write(json.dumps(data, sort_keys=True))

def error(id, msg=''):
    error_list = {
        1: 'Argument <name> is not specified.',
        2: 'Argument <path> is not specified.',
        3: 'Argument <change> is not specified.',
        4: 'Modification option is not specified.',
        5: 'Unrecognized modification option: ' + msg + '.',
        6: 'Unrecognized flag: ' + msg + '.',
        7: '"' + msg + '" is not found in database.',
        8: '"' + msg + '" already exists.',
        9: 'Name cannot exceed 15 characters.'
    }

    print(error_list.get(id, 'Unknown error.'))
    if id in [1, 2, 3, 4, 5]:
        print(usage)

def opt_new(name, path):
    if len(name) < 16:
        data[name] = path
        # print('Added element ' + name + '.')
    else:
        error(9)

def opt_open(name):
    # print('Opening element ' + name + '...')
    os.startfile(data[name])

def opt_info(name):
    print('Name: ' + name)
    print('Path: ' + data[name])

def opt_list():
    for key in data:
        print(key + ('\t\t' if len(key) < 8 else '\t') + data[key])

def opt_modify(option, name, change):
    if option == '-n' or option == '--name':
        if exist(change):
            error(8, change)
        elif len(change) > 15:
            error(9)
        else:
            data[change] = data.pop(name)
    elif option == '-p' or option == '--path':
        data[name] = change
    else:
        error(5, option)

def opt_delete(name):
    del data[name]
    # print('Deleted element ' + name + '.')
