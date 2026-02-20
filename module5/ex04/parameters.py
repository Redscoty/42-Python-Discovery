#! /usr/bin/env python3
#The program should display the number of parameters passed to it, followed by anewline.
#sys.argv[0] returns the name of the script.
#sys. argv[0])indicates how many arguments will be used in the running the file, the title of the script is always counted as argument 1, the following arguments would be anyhting additiional in the command line of the terminal.
# len(sys.argv) - 1) the -1 removes the title from the counting of arguments.
# argv stores the number of commads as a list, len tells us the lenght of that list.
# argv will print the commands as a string so it would for example print the system name of the file, when we add list we change it to a count of the arguments.

import sys
#print("number of parameters: ", sys.argv)
print("number of parameters: ", len(sys.argv) - 1)
