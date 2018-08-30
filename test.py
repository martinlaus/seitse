import os
import sys
import glob
import platform
from subprocess import call
from seven_zip import SevenZip


# data = 'test data'
file_name = 'multfiles.7z'
# add_to_archive = ['7za', 'a', '-t7z', file_name, '*.txt']
# call(add_to_archive)
# extract_from_archive = ['7z', 'x', file_name]
# call(extract_from_archive)
files = glob.glob('*.txt')
print(files)
seven = SevenZip()
# seven.create_archive_with(file_name, files)
destination = seven.extract_archive(file_name)
print('Files Extracted to: {0}'.format(destination))