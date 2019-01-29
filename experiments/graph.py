from leadeagle.processing.graph import *

input = LocalDirectoryInput(
    "/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne")
print(input.get_options())

s = Sequential()
s.append(input)

for wp in s():
    print(wp)
