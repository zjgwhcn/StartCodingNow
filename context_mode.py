#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import contextlib

class MyOpen(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_handler = None
        return

    def __enter__(self):
        print("enter:", self.file_name)
        self.file_handler = open(self.file_name, "r")
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit:", exc_type, exc_val, exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return True


with MyOpen("movie.txt") as file_in:
    for line in file_in:
        print(line)
        raise ZeroDivisionError


@contextlib.contextmanager
def open_func(file_name):
    print("open file", file_name, "in __enter__")
    file_handler = open(file_name, "r")

    yield file_handler

    print("close file", file_name, "in __exit__")
    file_handler.close()
    return


with open_func("movie.txt") as file_in:
    for line in file_in:
        print(line)
        break



class MyOpen2(object):

    def __init__(self, file_name):
        self.file_handler = open(file_name, "r")
        return


    def close(self):
        print("call close in MyOpen2")
        if self.file_handler:
            self.file_handler.close()
        return


with contextlib.closing(MyOpen2("movie.txt")) as file_in:
    pass