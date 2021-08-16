f = open('test.txt')
a = [ _.strip() for _ in f.readlines() ]
print(a)
f.close()

#result = []
#for line in f.readlines():
#    result.append(line.strip())
    
with open('test.txt') as file:
    print(file.read())

#__asd__
from datetime import datetime

class CustomLogger(object):
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
    def __enter__(self):
        self.file = open(self.file, self.mode)
        self.file.write(f"############# Start Date: {datetime.now()} #############\n")
        return self.file

    def __exit__(self,*args):
        self.file.write(f"############# End Date: {datetime.now()} #############\n")
        self.file.close()

with CustomLogger("Test2.txt","w") as file:
    file.write(f"This is the first line!\n")
    file.write(f"This is the first second!\n")
    file.write(f"This is the first third!\n")

from contextlib import contextmanager

@contextmanager
def CustomLog(*args):
    try:
        myfile = open(*args)
        myfile.write(f"############# Start Date: {datetime.now()} #############\n")
        yield myfile
    finally:
        myfile.write(f"############# End Date: {datetime.now()} #############\n")
        myfile.close()
