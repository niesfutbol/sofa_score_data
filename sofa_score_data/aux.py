from os import listdir
from os.path import isfile, join


def obtain_downloaded_files(path) -> list:
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    fixture = [int(f.split(".")[0].split("_")[-1]) for f in onlyfiles if f.split(".")[1] == "json"]
    fixture = list(set(fixture))
    return fixture


def obtain_not_downloaded_files(all_files, all_downloaded_files) -> list:
    return [int(match) for match in all_files if int(match) not in all_downloaded_files]
