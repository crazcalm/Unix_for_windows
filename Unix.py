"""
                Unix
                ----

Introduction:
-------------

  I an currently at a 24 hour hackathons (with 16 hours left) and I would like
to create a Unix class that allows me to use my typical Unix commands on my
Windows machines (Laptop, and old XP). 

  I originally was going to create a wrapper for the Windows termanal, but
then I remembered that the list of windows commands for my laptop and XP
are not the same.

  So, I am goint to write this class using only the python standard library.
Wish me luck!


Current functionality:
----------------------


Wanted functionality:
---------------------

ls
cd
mkdir
"""

import os

class Unix(object):
    """
    Porting a number of the unix commands to Windows
    """
    def __init__(self):
        print "You now have access to the a few linux commands!"

    def ls(self):
        dirs = os.listdir(os.getcwd())
        print_to_screen(dirs)


def print_to_screen(stack):
    """
    Formats the output
    """
    if len(stack)>=3:
        print "{0[0]:<15} {0[1]:^40} {0[2]:>5}".format(stack)
        return print_to_screen(stack[3:])

    elif len(stack) == 2:
        print "{0[0]:<20} {0[1]^20}".format(stack)

    elif len(stack) == 1:
        print stack[0]




