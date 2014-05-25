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

def path_converter(path):
    if path.find("/") != -1:
        return path.replace("/", os.sep)
    else:
        return path

class Terminal(object):

    def __init__(self):
        self.dic = {"ls": self.ls}
        self.dic_args_1 = {"cd": self.cd, "touch": self.touch}
        self.unix = Unix()

    def ls(self):
        self.unix.ls()

    def cd(self, path):
        path = path_converter(path)
        try:
            self.unix.cd(path)
        except:
            print "Not a valid path"

    def touch(self, path):
        path = path_converter(path)
        if not path.find(os.sep) == -1:
            print "path: ", path
            path, name = os.path.split(path)
            print path, name
            self.unix.touch(path, name)
        else:
            name = path
            self.unix.touch(".", name)
