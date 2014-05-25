from Terminal import Terminal

raw_input("imports working?")

import sys, os

def parse_input(string):
    return string.split(" ")

def main():
    """
    This method creates the terminal
    """
    # initial user input
    user_input = "Dummy variable"
    terminal = Terminal()

    while(user_input != "exit"):
        cwd = os.getcwd()
        user_input = raw_input(cwd + ": ").strip()

        if user_input in terminal.dic:
            raw_input("item detected")
            try:
                terminal.dic[user_input]()
            except e:
                print e

if __name__ == "__main__":
    main()
