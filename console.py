#!/usr/bin/python3
""" Module for the entry point of the command interpreter """
import cmd
import json
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self):
        """Exits console"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """"Provide help"""
        print("Quit command to exit the program")

    def do_show(self, args):
        """description for the methode"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        o_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        key = args[0] + "." + args[1]
        try:
            value = o_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
