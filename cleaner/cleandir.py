from os import listdir, rmdir
from os.path import isdir, isfile, join

def process(fpath: str):
    if not listdir(fpath):
        print('delete empty dir: ' + fpath)
        rmdir(fpath)
        return

    onlydirs = [join(fpath, d) for d in listdir(fpath) if isdir(join(fpath, d))]
    for d in onlydirs:
        process(d)
