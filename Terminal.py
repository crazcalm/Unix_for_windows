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
import os

class Terminal(object):

    def __init__(self):
        self.dic = {"ls": self.ls}
        self.dic_args_1 = {"cd": self.cd}
        self.unix = Unix()

    def ls(self):
        self.unix.ls()

    def cd(self, path):
        if path.find("/") != -1:
            path = path.replace("/",os.sep)
        try:
            self.unix.cd(path)
        except:
            print "Not a valid path"

