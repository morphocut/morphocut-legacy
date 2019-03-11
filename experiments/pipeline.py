import os
from morphocut.processing.pipeline import *
from timer_cm import Timer

input_path = "/data1/mschroeder/Datasets/18-10-15_Sediment_Trap_Fred_LeMoigne/*/"
export_path = "/tmp/M138_T4_200A_cleaned.zip"

# input_path = "/data1/mschroeder/Datasets/19-02-21-FredLeMoigne/test.jpeg"
# export_path = "/tmp/M138 T7 200A 1.zip"

num_workers = None

try:
    os.remove(export_path)
except OSError:
    pass

with Timer("Total time"):
    pipeline = get_default_pipeline(input_path, export_path)
    pipeline.execute()
