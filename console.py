#!/usr/bin/python3
""" file python description """
import cmd


class HBNBCommand(cmd.Cmd):
    """class description"""

    def do_EOF(self):
        """description for EOF methode"""
        return True

    def emptyline(self):
        """decription of emptyline methode"""
        pass

    def do_quit(self, line):
        """description of quit methode"""
        return True

    def help_quit(self):
        """"description for help_quit methode"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
