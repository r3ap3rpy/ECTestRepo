import sys

if len(sys.argv) != 3:
    print("The script needs a filename and a mode to operate!")
    sys.exit(1)

scriptname, file, mode = sys.argv
allowed_modes = ['r','w','x','a','b','t','+','rb','wb']

if mode not in allowed_modes:
    print(f"The specified mode is invalid.")
    print(f"Allowed modes: {','.join(allowed_modes)}")
    sys.exit(1)

print(f"Scriptname: {scriptname}\nFile: {file}\nMode: {mode}")

with open(file, mode) as my_file:
    if mode == 'r':
        print(my_file.read())
    else:
        my_file.write("This seems to be working!\n")