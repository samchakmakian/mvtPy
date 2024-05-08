import pathlib
import glob
import os


def find_file(filename,pathname):
    dirpath = pathlib.Path(__file__).parent.resolve()
    os.chdir(dirpath)
    os.chdir(pathname)
    for file in glob.glob(filename):
        return file
