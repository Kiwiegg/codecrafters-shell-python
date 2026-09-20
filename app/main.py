import sys

BUILTIN_COMMANDS = ['echo', 'type']

def main():
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
                    sys.stdout.write(f"{query}: not found\n")
            case _:
                sys.stdout.write(f"{line}: command not found\n")
            


if __name__ == "__main__":
    main()
