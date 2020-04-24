import os, json

usage = '''
Usage:
python "path_to_this_folder/main.py" [Option]

Option:
-n --new <name> <path>: Create a new shortcut
-o --open <name>: Open a shortcut
-i --info <name>: View the information of a shortcut
-l --list: View the list of shortcuts
-m --modify [-n --name][-p --path] <name> <change>: Modify the name and/or the path of a shortcut
-d --delete <name>: Delete a shortcut
-b --base: Show the directory in which this script is saved
'''

path = os.path.join(os.path.dirname(__file__), 'data.json')

data = {}

def exist(name):
    return name in data

def data_exist():
    if not os.path.isfile(path):
        with open(path, 'w') as file:
            file.write('{}')
            print('Initialized new data.')

def split_dir(name):
    return name.replace('\\', '/').split('/')

def join_path(name):
    path = data[name[0]]
    it = iter(name)
    _ = next(it)
    for subdir in it:
        path = os.path.join(path, subdir)
    return path

def load():
    global data
    data_exist()
    with open(path, 'r') as file:
        data = json.loads(file.readline())

def save(data):
    data_exist()
    with open(path, 'w') as file:
        file.write(json.dumps(data, sort_keys=True))

def error(id, msg=''):
    error_list = {
        1: 'Parameter <name> is not specified.',
        2: 'Parameter <path> is not specified.',
        3: 'Parameter <change> is not specified.',
        4: 'Modification option is not specified.',
        5: f'Unrecognized modification option: {msg}.',
        6: f'Unrecognized flag: {msg}.',
        7: f'"{msg}" is not found in database.',
        8: f'"{msg}" already exists.',
        9: 'Name cannot exceed 15 characters.',
        10: f'The system cannot find the file specified: "{msg}".'
    }

    print(error_list.get(id, 'Unknown error.'))
    if id in [1, 2, 3, 4, 5]:
        print(usage)

def opt_new(name, path):
    if len(name) < 16:
        data[name] = path
        # print('Added element {name}.')
    else:
        error(9)

def opt_open(name):
    # print(f'Opening element {name}...')
    path = data[name[0]]
    if len(name) > 1:
        path = join_path(name)
        if os.path.exists(path):
            os.startfile(path)
        else:
            error(10, path)
    else:
        os.startfile(path)

def opt_info(name):
    print(f'Name: {name}')
    print(f'Path: {data[name]}')

def opt_list():
    print('Name\t\tPath')
    print('-' * 80)
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
    # print('Deleted element {name}.')
