import sys


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
            case _:
                sys.stdout.write(f"{line}: command not found\n")
            


if __name__ == "__main__":
    main()
