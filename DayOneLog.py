# Grabs all the files in a directory, consolidates them, chucks them in Day One.
# One day.
#
# Assumes files are *.txt

import glob

# Set directory
dir = '/Users/James/Dropbox/Logging/'

# Create text chunks
dlist = glob.glob(dir + '*.txt')
print dlist
for i in dlist:
    print '####', i[len(dir):-4:]
    t = open(i, 'r')
    print t.read()
    print

