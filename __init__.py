# set up paths for object detection metrics

import sys
import os


def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)


currentPath = os.path.dirname(os.path.realpath(__file__))

# add ./scr or ./lib to PYTHONPATH
libPath = os.path.join(currentPath, "lib")
add_path(libPath)
