from os.path import isdir, isfile, join, getsize, splitext
from os import listdir, remove, rename
from filecmp import cmp
import ntpath

reservedwords = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by']

def detectspecialchar(fpath: str, specialchar):
    onlyfiles = [join(fpath, f) for f in listdir(fpath) if isfile(join(fpath, f))]
    
    for f in onlyfiles:
        for c in ntpath.basename(f):
            if '0' <= c <= '9':
                continue
            if 'a' <= c <= 'z':
                continue
            if 'A' <= c <= 'Z':
                continue
            if u'\u4e00' <= c <= u'\u9fff':
                continue
            if c == ' ':
                continue
            if c == '#':
                continue
            if c == '+':
                continue
            if c == '\'':
                continue
            if c == '&':
                continue
            if not c in specialchar:
                specialchar.append(c)

    onlydirs = [join(fpath, d) for d in listdir(fpath) if isdir(join(fpath, d))]
    for d in onlydirs:
        detectspecialchar(d, specialchar)

def process(fpath: str, specialchar):
    onlyfiles = [join(fpath, f) for f in listdir(fpath) if isfile(join(fpath, f))]
    
    for f in onlyfiles:
        filename, ext = splitext(f)
        basename = ntpath.basename(filename)
        arr = []

        for c in basename:
            if not c in specialchar:
                arr.append(c)
            else:
                arr.append(' ')

        newbasename = ''.join(arr)
        if not basename == newbasename:
            print(basename)
            newfilename = fpath + '\\' + newbasename + ext
            print(newfilename)
            print('==============================')
            rename(f, newfilename)

        basename = newbasename
        arr = []
        for w in basename.split():
            if w.lower() in reservedwords:
                arr.append(w.lower())
            else:
                neww =w[0].capitalize() + w[1:].lower()
                arr.append(neww)
        newbasename = ' '.join(arr)
        if not basename == newbasename:
            print(basename + ext)
            newfilename = fpath + '\\' + newbasename + ext
            print(newfilename)
            print('==============================')
            rename(fpath + '\\' + basename + ext, newfilename)

    onlydirs = [join(fpath, d) for d in listdir(fpath) if isdir(join(fpath, d))]
    for d in onlydirs:
        process(d, specialchar)