""" This script reads snapshot.dat and extract each time snapshot
    and save them in "alls" directory. It also save the projected 
    positions and velocities for each snapshot in projected_alls 
    directory.
    
    You must make alls and projected_alls directory before running
    this script."""

import fileinput
import numpy as np
from numpy.random import RandomState

TimeLimit = 400 # Myr, Time to advance in file.
TimeToWrite = 0 # Myr, Time to start writing in extracted snapshot files.
fInput = fileinput.input(['snapshot.dat'])
FileNameList = []

print("****** Reading snapshot.dat ******\n")
for line in fInput:
    a = line.split()
    aStr = '   '.join(str(ee) for ee in a)
    # print a
    if a[3] == "###":
        Ntot = int(a[0])
        Time = float(a[1])
        if Time < TimeLimit and Time >= TimeToWrite:
            print("Find header:", fileinput.lineno(), Ntot, Time)
            FileName = "alls/" + '{:09.3f}'.format(Time) 
            print("Writing to ", FileName, "\n")
            F = open(FileName, "a")
            FileNameList.append(FileName)
            # print "salam1"
            continue
        elif Time < TimeLimit and Time < TimeToWrite:
            print("Find header:", fileinput.lineno(), Ntot, Time)
            print("Skip to wirte")
            continue
        else:
            print("Stop at time", Time)
            break

    if Time >= TimeToWrite:
      # NAME(i), r(i), vr(i), vt(i), kstar(i), masses(i)
        F.write(a[0] + "\t" + a[1] + "\t" + a[2] + "\t" + a[3] + "\t" + "\t" + a[7] + "\t" + a[9] +"\n")
               
F.close()
fileinput.close()
#print(FileNameList)

seed = 10
print("\n","Converting to projected")
for fName in FileNameList:
    nameMc, rMc, vrMc, vtMc, ksMc, mMc = np.loadtxt(fName, unpack=True, usecols=(0,1,2,3,4,5))
    Size = rMc.size
    print("Number of stars is ", Size)
    randomGenerator = RandomState(seed) 
    ranA = randomGenerator.uniform(0., 1., size=Size)
    ranB = randomGenerator.uniform(0., 1., size=Size)
    #print(nameMc[0],nameMc[-1])
    #print(ranA[0],ranA[1],ranA[-1])
    #print(ranB[0],ranB[1],ranB[-1],"\n")
    
    seed = seed + 1 ## update seed number to generate a new random sequence for each time snapshot
    costheta = np.zeros(Size)
    costheta = 2.0*ranA-1.0
    sintheta = np.sqrt(1-costheta**2.)
    
    ## radial distance projection 
    rp = rMc*sintheta
    rp_los = rMc*costheta
    
    phi = ranB*2.0*np.pi
    cosphi = np.cos(phi)
    sinphi = np.sin(phi)
    rpx = rp*cosphi
    rpy = rp*sinphi
    
    vLos = vrMc*sinphi + vtMc*cosphi
    vStd = np.std(vLos)
    
    ## =============================

    fileSnapProjected = 'projected_' + fName
    print('Save to file', fileSnapProjected,"\n")
    np.savetxt(fileSnapProjected, np.column_stack((nameMc, rpx, rpy, rp_los, vrMc, vtMc, ksMc, mMc, vLos)), fmt='%9d %12.8f %12.8f %12.8f %12.8f %12.8f %3d %12.8f %12.8f')
    
        
  
 