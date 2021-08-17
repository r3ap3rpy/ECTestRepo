import argparse

parser = argparse.ArgumentParser(description = "This is a demo for file operations!")
parser.add_argument('--file','-file', type=str, help = "This is the filename we want to manipulate!")
parser.add_argument('--mode','-mode',choices=('r','w','x','a','b','t','+','rb','wb') ,type = str, help= "This is the mode in which we want to operate on the file!")
arguments = parser.parse_args()

if arguments.file and arguments.mode:
    print(f"The filename: {arguments.file}\nMode: {arguments.mode}")
else:
    parser.print_help()

with open(arguments.file, arguments.mode) as my_file:
    if arguments.mode == 'r':
        print(my_file.read())
    else:
        my_file.write("The second version of the arugments and file manipulation!\n")
