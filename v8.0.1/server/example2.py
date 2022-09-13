import os

path = os.getcwd()
print(path)
parent_path = os.path.dirname(path)
print(parent_path)
pparent_path = os.path.dirname(parent_path)
print(pparent_path)