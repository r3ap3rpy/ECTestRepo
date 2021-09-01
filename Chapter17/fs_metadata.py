import pathlib
import shutil
import sys

from datetime import datetime
from sys import path, platform

if platform.startswith('linux'):
    os = 'Linux'
elif platform == "win32":
    os = "Windows"
else:
    raise OSError("Unsupported OS found!")

try:
    if os == "Linux":
        pathlib.Path("/home/python/Documents/malicious_file.txt").touch()
    else:
        pathlib.Path("c:\\users\r3ap3rpy\\Desktop\\malicious_file.txt").touch()
except FileExistsError:
    pass

if os == 'Linux':
    tmp_dir = pathlib.Path("/tmp/tmp")
else:
    tmp_dir = pathlib.WindowsPath("c:\\users\\r3ap3rpy\\desktop\\tmp")

try:
    if tmp_dir.is_dir():
        raise FileExistsError
    else:
        tmp_dir.mkdir()
except FileExistsError:
    overwrite = input("The tmp already exists, Overwrite? (Y/N)")
    if overwrite.upper() == "Y":
        shutil.rmtree(tmp_dir)
        tmp_dir.mkdir()
    else:
        sys.exit()

try:
    if os == "Linux":
        input_file = pathli.Path("/home/python/Documents/malicious_file.txt")
    else:
        input_file = pathlib.Path("c:\\users\\r3ap3rpy\\desktop\\malicious_file.txt")
    shutil.copy2(input_file, tmp_dir)
except FileNotFoundError as e:
    print(e)

if os == 'Linux':
    linux_path = pathlib.PurePosixPath(tmp_dir).joinpath("malicious_file.txt")
    working_path = pathlib.Path(linux_path)
else:
    windows_path = pathlib.PureWindowsPath(tmp_dir).joinpath("malicious_file.txt")
    working_path = pathlib.Path(windows_path)

try:
    if not working_path.exists():
        raise FileNotFoundError
except FileNotFoundError:
    print(f"File was not created properly.")

print(working_path)
working_path.chmod(0o444)
file_mode = oct(working_path.stat().st_mode)
if file_mode[-3:] != 777:
    working_path.chmod(0o777)

if working_path.is_dir():
    print("It's a directory")
elif working_path.is_symlink():
    print("Its a symling")
elif working_path.is_file():
    print("its a file")
else:
    print("It's something else")

size = working_path.stat().st_size
if size <1024:
    print(f"{size} bytes")
elif size < 1048576:
    print(f"{size / 1024:.2f} KB")
else:
    print(f"{size / 1048576:.2f} MB")

try:
    print(f"Owner: {working_path.owner()}")
except NotImplemented as e:
    print(e)
try:
    print(f"Group: {working_path.group()}")
except NotImplemented as e:
    print(e)

print(f"Most recent access time: {datetime.fromtimestamp(working_path.stat())}")
print(f"Most recent modification time: {datetime.fromtimestamp(working_path.stat())}")
print(f"Most recent metadata change (Linux)/Creation time (Windows): ")
print(f"{datetime.fromtimestamp(working_path.stat().st_ctime)}"))
 