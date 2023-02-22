from termcolor import colored
import os


#funkció létrehozása
print(colored('Funkció létrehozása \n', attrs=['bold', 'underline']))
print(colored("---------CODE---------", "green"))
print(colored("def my_function():", "green"))
print(colored("    print('Hello from a function')", "green"))
print(colored("---------OUTPUT---------", "yellow"))
def my_function():
    print(colored('Hello from a function', 'yellow'))


#funkció meghívása
print(colored('\n Funkció meghívása \n', attrs=['bold', 'underline']))
print(colored("---------CODE---------", "green"))
print(colored("my_function()", "green"))
print(colored("---------OUTPUT---------", "yellow"))
my_function()


#funkció paraméterezése
print(colored('\n Funkció paraméterezése \n', attrs=['bold', 'underline']))
print(colored("---------CODE---------", "green"))
print(colored("def my_function(fname):", "green"))
print(colored("    print(fname + ' Refsnes')", "green"))
print(colored("\nmy_function('Emil')", "green"))
print(colored("my_function('Tobias')", "green"))
print(colored("my_function('Linus')", "green"))
print(colored("---------OUTPUT---------", "yellow"))
def my_function(fname):
    print(colored(fname + ' Refsnes', 'yellow'))

my_function('Emil')
my_function('Tobias')
my_function('Linus')


#funkció paraméterezése több paraméterrel
print(colored('\n Funkció paraméterezése több paraméterrel \n', attrs=['bold', 'underline']))
print(colored("---------CODE---------", "green"))
print(colored("def my_function(fname, lname):", "green"))
print(colored("    print(fname + ' ' + lname)", "green"))
print(colored("\nmy_function('Emil', 'Refsnes')", "green"))
print(colored("---------OUTPUT---------", "yellow"))
def my_function(fname, lname):
    print(colored(fname + ' ' + lname, 'yellow'))

my_function('Emil', 'Refsnes')


