# just run this script

import __init__
import argparse
import sys
import os
import glob
import shutil

parser = argparse.ArgumentParser(
    prog="object detection metrics",
    description="evaluate the object detection model",
    epilog="author: zhongchong")
# mandatory
parser.add_argument(
    "-gt",
    "--gtfolder",
    dest="gtFoder",
    metavar="",
    help="folder containing ground truth bounding boxes")
parser.add_argument(
    "-det",
    "--detfolder",
    dest="detFolder",
    metavar="",
    help="folder containing detected bounding boxes")
# Optional
parser.add_argument(
    "-t",
    "--threshold",
    dest="iouThreshold",
    type=float,
    default=0.5,
    matavar="",
    help="IOU threshold. Default 0.5")
parser.add_argument(
    "-gtcoords",
    dest="gtCoordinates",
    metavar="",
    help="reference of the ground truth bounding box coordinates: absolute")
parser.add_argument(
    "-dtcoords",
    dest="gtCoordinates",
    metavar="",
    help="reference of the ground truth bounding box coordinates: absolute")
parser.add_argument(
    "-imgsize",
    dest="imgSize",
    matavar="",
    help="image size, Required if coords are 'rel'")
parser.add_argument(
    "-sp",
    "--savepath",
    dest="savePath",
    metavar="",
    help="folder where the plots are saved")
parser.add_argument(
    "-np",
    "--noplot",
    dest="showPlot",
    action="store_false",
    help="no plot is show during executing")
args = parser.parse_args()
