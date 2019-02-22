import os
from leadeagle.processing.pipeline import *
from timer_cm import Timer

input_path = "/data1/mschroeder/Datasets/18-10-15_Sediment_Trap_Fred_LeMoigne/*/"
export_path = "/tmp/M138_T4_200A_cleaned.zip"

num_workers = None

try:
    os.remove(export_path)
except OSError:
    pass

with Timer("Total time"):
    pipeline = Pipeline([
        DataLoader(input_path),
        Progress("loaded"),
        # MultiThreadPipeline([
        VignetteCorrector(),
        Processor(),
        # ], num_workers),
        Exporter(export_path)
    ])

    for x in pipeline():
        print(x)
