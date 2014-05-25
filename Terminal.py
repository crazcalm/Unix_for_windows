"""
                    Terminal:
                    ---------

Goal:
----

  I would like to write a script to create a artificial termial window.

Plan:
-----

  I will create a looping input that closes when the "exit" is typed.
"""

import sys, os
from Unix import Unix


def parse_input(string):
    return string.split(" ")


class Terminal(object):

    def __init__(self):
        print "Termainal instance created"
        self.dic = {"ls": self.ls}
        self.unix = Unix()

    def ls(self):
        raw_input("ls ing")
        self.unix.ls()


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
            terminal.dic[user_input]()


if __name__ == "__main__":
    main()

