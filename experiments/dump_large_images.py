"""
Dump images for Rainer.
"""
import os
import shutil

from timer_cm import Timer

from morphocut.processing.pipeline import *


# input_path = "/data1/mschroeder/Datasets/19-02-21-FredLeMoigne/M138 T4 (wetransfer-477f42)/"
input_path = "/data1/mschroeder/Datasets/19-02-21-FredLeMoigne/M138 T4 (wetransfer-477f42)/M138 T4 300A-02.jpeg"
dump_path = "/tmp/GelDump"

try:
    shutil.rmtree(dump_path, ignore_errors=True)
except OSError:
    pass

os.makedirs(dump_path)

with Timer("Total time") as timer:
    # pipeline = get_default_pipeline(input_path, export_path)

    with timer.child("Parents"):
        print("Processing parents...")
        parents = Pipeline([
            DataLoader(input_path, output_facet="raw"),
            Progress("Loaded"),
            VignetteCorrector(input_facet="raw", output_facet="color"),
            BGR2Gray(input_facet="color", output_facet="gray"),
            ThresholdOtsu(input_facet="gray", output_facet="mask")
        ])
        parents = list(parents())

    with timer.child("Children"):
        print("Processing children...")
        children = Pipeline([
            Raw(parents),
            ExtractRegions(
                mask_facet="mask",
                intensity_facet="gray",
                image_facets=["color", "gray"],
                output_facet="roi",
                padding=10,
                min_area=30),
            DrawContoursOnParent("color", "roi", "contours")
        ])
        children.execute()

    with timer.child("Dump"):
        print("Dumping...")
        dump_parents = Pipeline([
            Raw(parents),
            DumpImages(dump_path, "raw"),
            DumpImages(dump_path, "color"),
            DumpImages(dump_path, "gray"),
            DumpImages(dump_path, "contours"),
        ])
        dump_parents.execute()
