import sys
import os
import subprocess
from functools import lru_cache

BUILTIN_COMMANDS = ['echo', 'type', 'exit']

@lru_cache(maxsize=50)
def get_executable(directories, command):
    for directory  in directories:
        full_path = os.path.join(directory, command)

        if os.path.isfile(full_path):
            if os.access(full_path, os.X_OK):
                return full_path
            
            continue

    return None

def main():
    path_directories = tuple(os.environ.get("PATH", "").split(os.pathsep))


    while True:
        sys.stdout.write("$ ")
        line = input()
        args = line.split(" ")
        command = args[0]

        if line == 'exit':
            break

        match command:
            case 'echo':
                sys.stdout.write(" ".join(args[1:]))
                sys.stdout.write("\n")
            case 'type':
                query = args[1]
                if query in BUILTIN_COMMANDS:
                    sys.stdout.write(f"{query} is a shell builtin\n")
                else:
                    exec_path = get_executable(path_directories, query)
                    if exec_path is not None:
                        sys.stdout.write(f"{query} is {exec_path}\n")
                    else: 
                        sys.stdout.write(f"{query}: not found\n")
            case _:
                exec_path = get_executable(path_directories, command)
                if exec_path:
                    subprocess.run([command, *args[1:]])
                else:
                    sys.stdout.write(f"{line}: command not found\n")
            


if __name__ == "__main__":
    main()
