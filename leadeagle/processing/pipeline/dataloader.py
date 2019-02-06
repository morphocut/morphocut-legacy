# {
#     object_id: ...
#     facets: {
#         # For DataLoader
#         input_data: {
#             meta: {filename: ...},
#             image: <np.array of shape = [h,w,c]>
#         },
#         # For Processor
#         raw_img: {
#             meta: {region props...},
#             image: <np.array of shape = [h,w,c]>
#         },
#         contour_img: {
#             meta: {},
#             image: <np.array of shape = [h,w,c]>
#         },
#         # Nothing for export
#     }
# }


"""
Input nodes
"""

import os
from leadeagle.processing.pipeline import NodeBase
import cv2 as cv


class DataLoader(NodeBase):
    """
    Read the contents of a local directory and yield processing objects.

    Source node (no predecessors).
    """

    def __init__(self, location, object_extensions=None):
        self.location = location
        self._index = None
        self.object_extensions = object_extensions

        self._get_index()

    def get_options(self):
        index = self._get_index()

        if self.index is None:
            self._make_index()

        extensions = set(os.path.splitext(f)[1] for f in self.index["files"])

        object_extensions = {".jpeg", ".jpg", ".png", ".gif", ".tif"}

        object_extensions &= extensions

        index_extensions = {".tsv", ".csv"}

        index_files = [f for f in self.index["files"]
                       if os.path.splitext(f)[1] in index_extensions]

        return {
            "object_extensions": object_extensions,
            "index_files": index_files,
        }

    def _get_index(self):
        """
        Scan the location for files and create index.
        """
        print("Reading location {}...".format(self.location))
        self.object_extensions = {".jpeg", ".jpg", ".png", ".gif", ".tif"}
        index = {"dirs": [], "files": [], "root_files": []}
        for root, dirs, files in os.walk(os.path.abspath(self.location)):
            rel_root = os.path.relpath(root, self.location)
            index["dirs"].extend(os.path.join(rel_root, d) for d in dirs)
            index["files"].extend(dict(
                filename=f.split('.')[0],
                filepath=os.path.join(root, f)
            ) for f in files if os.path.splitext(f)[1] in self.object_extensions)
        self.index = index

    def __call__(self, input=None):
        for file in self.index['files']:
            print('Loading file ' + file['filepath'])
            data_object = dict(
                object_id=file['filename'],
                facets=dict(
                    input_data=dict(
                        meta=dict(
                            filename=file['filename'],
                            filepath=file['filepath'],
                        ),
                        image=cv.imread(file['filepath'])
                    )
                ))
            yield data_object