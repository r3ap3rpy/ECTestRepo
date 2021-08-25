import hashlib
from getpass import getpass

validPass = b'\xdfb\xd3\xf6\xbc\x1f\xe13\xd2\x9e\xc4\x05\xfa\xae{r\x89\xf62\x94z\xe1b\xc7\xc8\xe2>>&\xd1\x96('

input_pass = getpass("Give me your password: ")
input_hasher = hashlib.sha256()
input_hasher.update(bytes(input_pass,'utf-8'))
input_pass_hash = input_hasher.digest()

if validPass == input_pass_hash:
    print(f"The password you entered is valid!")
else:
    print(f"Invalid password was specified!")
