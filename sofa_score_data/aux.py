import os
from os import listdir
from os.path import isfile, join


def obtain_downloaded_files(path) -> list:
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    fixture = [int(f.split(".")[0].split("_")[-1]) for f in onlyfiles if f.split(".")[1] == "json"]
    fixture = list(set(fixture))
    return fixture