import hashlib
from getpass import getpass

validPass = b"ECCouncil2021"

hasher = hashlib.sha256()
hasher.update(validPass)
validPassHash = hasher.digest()

input_pass = getpass("Give me your password: ")
input_hasher = hashlib.sha256()
input_hasher.update(bytes(input_pass,'utf-8'))
input_pass_hash = input_hasher.digest()

if validPassHash == input_pass_hash:
    print(f"The password you entered is valid!")
else:
    print(f"Invalid password was specified!")