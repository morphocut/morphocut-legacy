from morphocut.processing.pipeline import *
import os
import cv2 as cv

# if os.path.exists("/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne"):
#     input = LocalDirectoryInput(
#         "/home/moi/Work/18-10-15 Sediment Trap Fred LeMoigne")
# else:
#     input = LocalDirectoryInput(
#         r"C:\Users\Christian\Documents\Masterprojekt\morphocut\Test\M138 T4 200A cleaned")

# print(input.get_options())

# importer = Importer()
# processor = Processor()

# s = Pipeline([input, importer, processor])

# for wp in s():
# print(str(wp))

dataloader = DataLoader(
    r"C:\Bibliotheken\Dokumente\hiwi_geomar\morphocut\Test\Images for Rainer\M138 T4 400A cleaned")
processor = Processor()
exporter = Exporter(
    r"C:\Bibliotheken\Dokumente\hiwi_geomar\morphocut\Test\Images for Rainer\M138 T4 400A cleaned")


#  vignettierung als eigenen node
s = Pipeline([dataloader, processor, exporter])

for wp in s():
    print(str(wp))
