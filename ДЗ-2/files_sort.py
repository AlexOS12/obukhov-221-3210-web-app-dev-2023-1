import os
from sys import argv

def sortFiles(files : dict[str, list[str]]) -> dict[str, list[str]]:
    """Sorts files groupped by their extension.
    Returns sorted list of files"""

    #sort by extension
    sorted_keys = sorted(files)

    sorted_files = {}

    #sort by filename
    for key in sorted_keys:
        sorted_files[key] = sorted(files[key])

    return sorted_files


def getFiles(path : str) -> list[str]:
    """Gets a path to some directory.
    Returns dict of file names and groupped by their extensions"""
    files = {}

    for file in os.listdir(path):
        if os.path.isfile(f"{path}\\{file}"):
            if '.' in file:
                filename, extension = file[:file.rfind('.')], file[file.rfind('.') + 1:]
            else:
                filename, extension = file, ''
            if extension in files:
                files[extension].append(filename)
            else:
                files.update({extension : [filename]})

    sortedFilesDict = sortFiles(files)
    sortedFiles = []
    
    for extension in sortedFilesDict:
        for filename in sortedFilesDict[extension]:
            if extension:
                sortedFiles.append(f"{filename}.{extension}")
            else:
                sortedFiles.append(filename)

    return sortedFiles

if __name__ == "__main__":
    if len(argv) == 1:
        argv.append(os.curdir)
    print(*getFiles(argv[1]), sep='\n')
