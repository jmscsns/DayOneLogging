# Grabs all the files in a directory, consolidates them, chucks them in Day One.
# One day.
#
# Assumes files are *.txt and requires DayOne CLI be installed.
#
# This will delete all *.txt files in the specified directory, use with care.
# NB Does not, for some reason, include the last file in the generated entry

import glob
import os

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
#    os.remove(i)

# Run DayOne CLI
os.system('/usr/local/bin/dayone new <' + '"' + dir + '"' + 'final.txt')

# Remove created file
os.remove(dir + 'final.txt')



