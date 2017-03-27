#! /usr/bin/env python
""" This script reads snapshot.dat and extract each time snapshot
    and save them in "all" directory. """

import fileinput
import os

TimeLimit = 11100 # Myr, Time to advance in file.
TimeToWrite = 11000 # Myr, Time to start writing in extracted snapshot files.
fInput = fileinput.input(['snapshot.dat'])
print "****** Reading snapshot.dat ******\n"
for line in fInput:
    a = line.split()
    aStr = '   '.join(str(ee) for ee in a)
    # print a
    if a[3] == "###":
        Ntot = int(a[0])
        Time = float(a[1])
        if Time < TimeLimit and Time > TimeToWrite:
            print "Find header:", fileinput.lineno(), Ntot, Time
            FileName = "all/M60R10d103t" + '{:09.3f}'.format(Time) + "all.txt"
            print "Writing to ", FileName, "\n"
            F = open(FileName, "a")
            # print "salam1"
            continue
        elif Time < TimeLimit and Time < TimeToWrite:
            print "Find header:", fileinput.lineno(), Ntot, Time
            print "Skip to wirte"
            continue
        else:
            print "Stop at time", Time
            break
    # print type(a)
    if Time > TimeToWrite:
        F.write(a[0] + "\t" + a[1] + "\t" + a[2] + "\t" + a[3] + "\t" + "\t" + a[7] + "\t" + a[9] +"\n")
fileinput.close()
