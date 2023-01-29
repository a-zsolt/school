# 1.) Készítsd el az alábbi python állományokat a megadott w3schools link alapján:
#     ============================================================================
# "file_handling.py"			"https://www.w3schools.com/python/python_file_handling.asp"
# "read_files.py"				"https://www.w3schools.com/python/python_file_open.asp" 
# "write-create_files.py"		"https://www.w3schools.com/python/python_file_write.asp" 
# "delete_files.py"			"https://www.w3schools.com/python/python_file_remove.asp"

import os
import random
import math
from termcolor import colored

os.system("cls")

def menu():
    menupont = int(input("Add meg hogy melyik feladatatot szeretnéd futtatni (1-9):"))

    if menupont < 1 or menupont > 9:
        print("A megadott szám nem szerepel a listába.")
    elif menupont == 1:
        FileHandling()
    elif menupont == 2:
        FileReading()
    elif menupont == 3:
        FileWriting()
    elif menupont == 4:
        FileDeleting()


def FileHandling():
        os.system("cls")
        print(colored("File kezelés", attrs=["bold", "underline"]))
        print(colored("---------CODE---------", "green"))
        print(colored("file = open(""file.txt"", ""r"")", "green"))
        print(colored("---------OUTPUT-------", "yellow"))
        file = open("file.txt", "r")
        print(colored(file.read() , "yellow"))
        print(" ")


def FileReading():
        os.system("cls")
        print(colored("File kezelés", attrs=["bold", "underline"]))
        print(colored("---------CODE---------", "green"))
        print(colored("file = open(""file.txt"", ""r"")", "green"))
        print(colored("file = open(""print(file.read())"", ""r"")", "green"))
        print(colored("---------OUTPUT-------", "yellow"))
        file = open("file.txt", "r")
        print(colored(file.read() , "yellow"))
        print(" ")


def FileWriting():
        os.system("cls")
        print(colored("File írás", attrs=["bold", "underline"]))
        print(colored("---------CODE---------", "green"))
        print(colored("file = open(""file.txt"", ""a"")", "green"))
        print(colored("file.write(""Hello World!"")", "green"))
        print(colored("---------OUTPUT-------", "yellow"))
        file = open("./file.txt", "a")
        file.write("Hello World!")
        print(colored(file.read() , "yellow"))
        print(" ")

        print("File létrehozása" , attrs=["bold", "underline"])
        print(colored("---------CODE---------", "green"))
        print(colored("file = open(""file.txt"", ""a"")", "green"))
        print(colored("---------OUTPUT-------", "yellow"))
        print(colored(file.read() , "yellow"))
        print(" ")


def FileDeleting():
        os.system("cls")
        print(colored("File törlés", attrs=["bold", "underline"]))
        print(colored("---------CODE---------", "green"))
        print(colored("os.remove(""file.txt"")", "green"))
        print(colored("---------OUTPUT-------", "yellow"))
        file = os.remove("file.txt")
        print(" ")


menu()