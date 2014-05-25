from Terminal import Terminal

raw_input("imports working?")

import sys, os

def user_input():
    cwd = os.getcwd()
    string = raw_input(cwd + ": ").strip()
    return string.split(" ")

def main():
    """
    This method creates the terminal
    """
    # initial user input
    inputs = ["Dummy variable"]
    terminal = Terminal()

    while(inputs[0] != "exit"):
        cwd = os.getcwd()
        inputs = user_input()
        raw_input()

        if inputs[0] in terminal.dic:
            command = inputs[0]
            terminal.dic[command]()
        elif inputs[0] in terminal.dic_args_1:
            if len(inputs) == 2:
                command, arg = inputs
                terminal.dic_args_1[command](arg)

if __name__ == "__main__":
    main()
