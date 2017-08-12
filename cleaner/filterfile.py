from os.path import isdir, isfile, join, getsize, splitext
from os import listdir, remove

def handleunexpectedext(fpath: str, exptectedext) -> []:
    unexpectedExt = []
    onlyfiles = [join(fpath, f) for f in listdir(fpath) if isfile(join(fpath, f))]

    for f in onlyfiles:
        filename, ext = splitext(f)
        if not ext.lower() in exptectedext:
            print('delete file: ' + f)
            remove(f)
            if not ext in unexpectedExt:
                unexpectedExt.append(ext)

    onlydirs = [join(fpath, d) for d in listdir(fpath) if isdir(join(fpath, d))]
    for d in onlydirs:
        subExt = handleunexpectedext(d, exptectedext)
        for e in subExt:
            if not e in unexpectedExt:
                unexpectedExt.append(e)

    return unexpectedExt