"""This module detects ."""

from os.path import isdir, isfile, join, getsize, splitext
from os import listdir, remove
from filecmp import cmp

def getfilesizemap(fpath: str, filemap) -> int:
    """get files map with same size"""
    filecnt = 0
    if not isdir(fpath):
        print('folder cannot be found: ' + fpath)
        return filecnt
    onlyfiles = [join(fpath, f) for f in listdir(fpath) if isfile(join(fpath, f))]
    filecnt = len(onlyfiles)

    for f in onlyfiles:
        size = getsize(f)
        if not size in filemap.keys():
            filemap[size] = []
        filemap[size].append(f)

    onlydirs = [join(fpath, d) for d in listdir(fpath) if isdir(join(fpath, d))]
    for d in onlydirs:
        filecnt = filecnt + getfilesizemap(d, filemap)
    return filecnt

def cleanupfiles(filemap):
    for key in filemap.keys():
        if len(filemap[key]) == 1:
            continue
        if len(filemap[key]) > 1:
            for idx, val in enumerate(filemap[key]):
                idx2 = idx + 1
                while idx2 < len(filemap[key]):
                    removeduplicatedfiles(filemap[key][idx], filemap[key][idx2])
                    idx2 = idx2 + 1

def removeduplicatedfiles(file1, file2): 
    if isfile(file1) and isfile(file2) and cmp(file1, file2):
        print('delete duplicated file: ' + file2)
        remove(file2)
