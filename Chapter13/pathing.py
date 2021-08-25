import os

config_file = f".{os.path.sep}" + "settings.conf"

with open(config_file) as config:
    print(config.read())

full_path = r"C:\Users\r3ap3rpy\Desktop\ECCouncil\Chapter13\settings.conf"

with open(full_path) as config:
    print(config.read())

build_path = ['c:','Users','r3ap3rpy','Desktop','ECCouncil','Chapter13','settings.conf']

built_path = os.path.sep.join(build_path)
print(built_path)
