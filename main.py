from Commands import AbstractCommand
from Commands import CommandFactory
import sys

if __name__ == '__main__':
    factory = CommandFactory()
    print("Hello! I'm Virtual Assistant. \nInput 'HELP' for more information or 'EXIT' to exit the program")

    while True:
        line = input('==> ')
        if line == 'EXIT':
            sys.exit()
        command: AbstractCommand = factory.get_command(line)
        command.execute()