"""This module detects ."""

from os.path import isdir, isfile, join, getsize
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
        if len(filemap[key]) is 1:
            return
        if len(filemap[key]) > 2:
            print('more than 2 files, will be handled in next run.')
        if cmp(filemap[key][0], filemap[key][1]):
            print('delete duplicated file: ' + filemap[key][1])
            remove(filemap[key][1])
