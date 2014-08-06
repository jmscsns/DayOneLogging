# Grabs all the files in a directory, consolidates them, chucks them in Day One.
# One day.
#
# Assumes files are *.txt

import glob
import subprocess

# Set directory
dir = '/Users/James/GitHub/DayOneLogging/testfiles/'

# Create text chunks and append to final.txt
dlist = glob.glob(dir + '*.txt')
for i in dlist:
    h = '#### ' + i[len(dir):-4:]
    t = open(i, 'r')
    r = open(dir + 'final.txt', 'a')
    r.write(str(h) + '\n')
    r.write(t.read() + '\n\n')

