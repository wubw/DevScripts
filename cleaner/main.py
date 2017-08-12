"""This module runs the cleaner."""

import dupfile
import filterfile
import cleandir
import namingconv

fpath = 'D:\\Private\\02 Books'

'''
fmap = {}
cnt = dupfile.getfilesizemap(fpath, fmap)
print('getfilesizemap: in total ' + str(cnt) + ' files')
dupfile.cleanupfiles(fmap)

unexpectedExt = filterfile.handleunexpectedext(fpath, ['.pdf', '.mobi', '.txt', '.chm', '.doc', '.ppt', '.pptx'])
print(unexpectedExt)
'''
specialchar=[]
namingconv.detectspecialchar(fpath, specialchar)
#print(specialchar)
namingconv.process(fpath, specialchar)

cleandir.process(fpath)