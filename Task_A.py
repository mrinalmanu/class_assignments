import os
import sys

from Task_9 import *


def main(args):
    cwd = os.getcwd()
    user_name = print(cwd.split(os.sep)[2] + ':')
    print("Welcome to BioShell!\n")
    while True:
        cmdtokens = input('{path}$ '.format(path=cwd)).split()
        if not cmdtokens:
            continue
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]
        if cmd == 'ls':
            dirlist = os.listdir(os.getcwd())
            print(dirlist)
        elif cmd == 'cd':
            try:
                path = str(os.getcwd())
                new_path = ''.join(cmdargs)
                if FSItem.isdirectory(new_path):
                    os.chdir('"' + new_path + '"')
                elif path == new_path:
                    pass
                else:
                    print('Error! There is no such directory!')
            except:
                print("I don't understand!")
        elif cmd == 'cat':
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                    for line in file:
                        print(line.strip('\n'))
        elif cmd == 'head':
            number_of_rows = 10
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                    while number_of_rows != 0:
                        print(file.readline())
                        number_of_rows -= 1
        elif cmd == 'tail':
            number_of_rows = 10
            new_path = ''.join(cmdargs)
            if os.path.isfile(new_path):
                with open(new_path, 'r') as file:
                    my_lines = file.readlines()
                    for line in my_lines[-number_of_rows:]:
                        print(line)
        elif cmd == 'pwd':
            print(os.getcwd())
        elif cmd == 'touch':
            try:
                new_path = ''.join(cmdargs)
                File(new_path).create()
            except:
                print("The item is already there. Don't touch!")
        elif cmd == 'find':
            find_file = ''.join(cmdargs)
            all_paths = os.listdir(cwd)
            for path in all_paths:
                if find_file in os.path.split(path)[1]:
                    print(path)
        elif cmd == 'clear':
            print('\n' * 150)
        elif cmd == 'mv':
            old_name = cmdargs[0]
            new_name = cmdargs[1]
            print(os.path.isfile(old_name))
            print(os.path.isfile(new_name))
            if os.path.exists(old_name) and os.path.exists(os.path.join(os.getcwd(), new_name)) == False:
                os.rename(old_name, new_name)
            elif os.path.isfile(old_name) and os.path.isdir(new_name):
                shutil.move(old_name, new_name)
            else:
                print("Error: wrong input")
        elif cmd == 'cp':
            old_name = cmdargs[0]
            new_name = cmdargs[1]
            shutil.copy(old_name, new_name)
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
