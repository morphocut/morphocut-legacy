from leadeagle.processing.graph import *

s = Sequential()
s.append(LocalDirectoryInput("/path/to/images"))

for wp in s.process():
    print(wp)