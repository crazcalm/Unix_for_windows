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

from Unix import Unix


class Terminal(object):

    def __init__(self):
        print "Termainal instance created"
        self.dic = {"ls": self.ls}
        self.unix = Unix()

    def ls(self):
        raw_input("ls ing")
        self.unix.ls()

