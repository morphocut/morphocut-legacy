from leadeagle.processing.pipeline import *
import os
import cv2 as cv

# if os.path.exists("/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne"):
#     input = LocalDirectoryInput(
#         "/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne")
# else:
#     input = LocalDirectoryInput(
#         r"C:\Users\Christian\Documents\Masterprojekt\LeadEagle\Test\M138 T4 200A cleaned")

# print(input.get_options())

# importer = Importer()
# processor = Processor()

# s = Pipeline([input, importer, processor])

# for wp in s():
# print(str(wp))

dataloader = DataLoader(
    r"C:\Users\Christian\Documents\Masterprojekt\LeadEagle\Test\M138 T4 200A cleaned")
processor = Processor()
exporter = Exporter(
    r"C:\Users\Christian\Documents\Masterprojekt\LeadEagle\Test\M138 T4 200A cleaned")


#  vignettierung als eigenen node
s = Pipeline([dataloader, processor, exporter])

for wp in s():
    print(str(wp))
