"""This module runs the cleaner."""

import dupfile

fpath = 'D:\\Private\\00 Pictures'
fmap = {}

cnt = dupfile.getfilesizemap(fpath, fmap)
print('getfilesizemap: in total ' + str(cnt) + ' files')

dupfile.cleanupfiles(fmap)
