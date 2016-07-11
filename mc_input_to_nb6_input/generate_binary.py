#!/usr/bin/python

import numpy as np
import os
import operator
import sys
import math
from math import *
from numpy.random import RandomState
import matplotlib.pyplot as pl

def rtnewt (ecc, ma) :
    #double x1,x2,xacc,rtnewt,f,df,dx
    #int j,jmax
    #PI = 3.14159265
    x1 = 0
    x2 = 2*pi
    xacc = 1E-6
    jmax = 20
    ma = 2*pi*ma 
    
    rtnewt=.5*(x1+x2)
    for j in range(1, jmax) :
        f = ma - rtnewt + ecc*sin(rtnewt)
        df = -1 + ecc*cos(rtnewt)
        dx=f/df
        rtnewt=rtnewt-dx
        if ((x1-rtnewt)*(rtnewt-x2)<0) :
            print ("jumped out of brackets\n")
        if (abs(dx)<xacc) :
	    return rtnewt
    
    print ("RTNEWT exceeding maximum iterations\n")
    exit(1) 
####################
input_file = open('./binary_nbody.dat', 'r')
#target_file = open('./all', 'w')
outputFile = open('./fort10_bin', 'w')
wocmFile = open('./wocm', 'w')
cmFile = open('./cm', 'w')

AUpc = 4.84814e-6 # AU to pc
RSUN = 6.96265e5 # Solar radius in km
pc = 3.08568E13 # pc in km
seed = 10

# load orbital ellipse parameter and center of mass phase space
ecc, aLog10Ro, m1Mo, m2Mo, x, y, z, vx, vy, vz = np.loadtxt(input_file,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9))
#ecc, aLog10Ro = np.loadtxt(input_file,unpack=True,usecols=(0,1-9))
#exit()
Size = ecc.size

#totalMass = float(sys.argv[1])
totalMass = 51773.830000002366
#totalMass = 51774.03
#rvir = float(sys.argv[2])
Rh = 6.65
rvir = Rh / 0.772764
rvir = 8.5
print "Total cluster mass = ", totalMass
print "Virial Radius", rvir

# initialize arrays
m1 = np.zeros(Size); m2 = np.zeros(Size)
x1 = np.zeros(Size); y1 = np.zeros(Size); z1 = np.zeros(Size)
x2 = np.zeros(Size); y2 = np.zeros(Size); z2 = np.zeros(Size)
vx1 = np.zeros(Size); vy1 = np.zeros(Size); vz1 = np.zeros(Size)
vx2 = np.zeros(Size); vy2 = np.zeros(Size); vz2 = np.zeros(Size)

star = np.zeros((2*Size, 7))
starwocm = np.zeros((2*Size, 7))

a = np.zeros(Size); ea = np.zeros(Size)
rop0 = np.zeros(Size); rop1 = np.zeros(Size)
mm = np.zeros(Size); eadot = np.zeros(Size)
vop0 = np.zeros(Size); vop1 = np.zeros(Size)
cosi = np.zeros(Size); inc = np.zeros(Size)
node = np.zeros(Size); peri = np.zeros(Size)
pmat = np.zeros((3, 2, Size))
rrel = np.zeros((3, Size)); vrel = np.zeros((3, Size))

randomGenerator = RandomState(seed) 
ranA = randomGenerator.uniform(0., 1., size=Size)
ranB = randomGenerator.uniform(0., 1., size=Size)
ranC = randomGenerator.uniform(0., 1., size=Size)
ranD = randomGenerator.uniform(0., 1., size=Size)
#print r

for i in range(Size) :
   #print i, ranA[i]
   m1[i] = m1Mo[i] / totalMass # mass in nbody unit
   m2[i] = m2Mo[i] / totalMass
   a[i] = pow(10., aLog10Ro[i]) # semi-major axis in Solar radius
   
   a[i] = a[i] * RSUN # semi-major axis in km
   a[i] = a[i] / pc # semi-major axis in pc
   a[i] = a[i] / rvir # semi-major axis in nbody unit
   
   ea[i] = rtnewt(ecc[i], ranA[i])
   #print ea[i]
   rop0[i] = a[i]*(cos(ea[i]) - ecc[i])
   rop1[i] = a[i]*sqrt(1.0-ecc[i]*ecc[i])*sin(ea[i])
   mm[i] = sqrt((m1[i]+m2[i])/pow(a[i],3))
   eadot[i] = mm[i]/(1.0 - ecc[i]*cos(ea[i]))
   vop0[i] = -a[i]*sin(ea[i])*eadot[i]
   vop1[i] = a[i]*sqrt(1.0-ecc[i]*ecc[i])*cos(ea[i])*eadot[i]
   #convert to cluster frame 
   cosi[i] = 2.0*ranB[i]-1.0
   inc[i] = acos(cosi[i])
   node[i] = 2.0*pi*ranC[i]
   peri[i] = 2.0*pi*ranD[i]

   pmat[0][0][i] = cos(peri[i])*cos(node[i]) - sin(peri[i])*sin(node[i])*cosi[i]
   pmat[1][0][i] = cos(peri[i])*sin(node[i]) + sin(peri[i])*cos(node[i])*cosi[i]
   pmat[2][0][i] = sin(peri[i])*sin(inc[i])
   pmat[0][1][i] = -sin(peri[i])*cos(node[i]) - cos(peri[i])*sin(node[i])*cosi[i]
   pmat[1][1][i] = -sin(peri[i])*sin(node[i]) + cos(peri[i])*cos(node[i])*cosi[i]
   pmat[2][1][i] = cos(peri[i])*sin(inc[i])
   
   for j in range(0, 3) :
       #print j
       rrel[j][i] = pmat[j][0][i]*rop0[i] + pmat[j][1][i]*rop1[i]
       vrel[j][i] = pmat[j][0][i]*vop0[i] + pmat[j][1][i]*vop1[i]
   #for j in range(0, 3) :
   star[2*i+1][1] = x[i] + m1[i]/(m1[i]+m2[i])*rrel[0][i]       #Star2 pos
   star[2*i+1][2] = y[i] + m1[i]/(m1[i]+m2[i])*rrel[1][i]
   star[2*i+1][3] = z[i] + m1[i]/(m1[i]+m2[i])*rrel[2][i]
   starwocm[2*i+1][1] = 0       #Star2 original pos
   starwocm[2*i+1][2] = 0
   starwocm[2*i+1][3] = 0
       #x2[i] = x[i] + m1[i]/(m1[i]+m2[i])*rrel[0][i]
       #y2[i] = y[i] + m1[i]/(m1[i]+m2[i])*rrel[1][i]
       #z2[i] = z[i] + m1[i]/(m1[i]+m2[i])*rrel[2][i]
   star[2*i+1][4] = vx[i] + m1[i]/(m1[i]+m2[i])*vrel[0][i]       #Star2 vel
   star[2*i+1][5] = vy[i] + m1[i]/(m1[i]+m2[i])*vrel[1][i]
   star[2*i+1][6] = vz[i] + m1[i]/(m1[i]+m2[i])*vrel[2][i]
   starwocm[2*i+1][4] = m1[i]/(m1[i]+m2[i])*vrel[0][i]       #Star2 original vel
   starwocm[2*i+1][5] = m1[i]/(m1[i]+m2[i])*vrel[1][i]
   starwocm[2*i+1][6] = m1[i]/(m1[i]+m2[i])*vrel[2][i]
       #vx2[i] = vx[i] + m1[i]/(m1[i]+m2[i])*vrel[0][i]
       #vy2[i] = vy[i] + m1[i]/(m1[i]+m2[i])*vrel[1][i]
       #vz2[i] = vz[i] + m1[i]/(m1[i]+m2[i])*vrel[2][i]
   star[2*i][1]  = x[i] - m2[i]/(m1[i]+m2[i])*rrel[0][i]                        #Star1 pos
   star[2*i][2]  = y[i] - m2[i]/(m1[i]+m2[i])*rrel[1][i]
   star[2*i][3]  = z[i] - m2[i]/(m1[i]+m2[i])*rrel[2][i]
   starwocm[2*i][1]  = 0                        #Star1 original pos
   starwocm[2*i][2]  = 0
   starwocm[2*i][3]  = 0
       #x1[i] = x[i] - m2[i]/(m1[i]+m2[i])*rrel[0][i]
       #y1[i] = y[i] - m2[i]/(m1[i]+m2[i])*rrel[1][i]
       #z1[i] = z[i] - m2[i]/(m1[i]+m2[i])*rrel[2][i]
   star[2*i][4]  = vx[i] - m2[i]/(m1[i]+m2[i])*vrel[0][i]                        #Star1 vel
   star[2*i][5]  = vy[i] - m2[i]/(m1[i]+m2[i])*vrel[1][i]
   star[2*i][6]  = vz[i] - m2[i]/(m1[i]+m2[i])*vrel[2][i]
   starwocm[2*i][4]  = - m2[i]/(m1[i]+m2[i])*vrel[0][i]                        #Star1 original vel
   starwocm[2*i][5]  = - m2[i]/(m1[i]+m2[i])*vrel[1][i]
   starwocm[2*i][6]  = - m2[i]/(m1[i]+m2[i])*vrel[2][i]
       #vx1[i] = vx[i] - m2[i]/(m1[i]+m2[i])*vrel[0][i]
       #vy1[i] = vy[i] - m2[i]/(m1[i]+m2[i])*vrel[1][i]
       #vz1[i] = vz[i] - m2[i]/(m1[i]+m2[i])*vrel[2][i]
   star[2*i][0] = m1[i]
   star[2*i+1][0] = m2[i]
   starwocm[2*i][0] = m1[i]
   starwocm[2*i+1][0] = m2[i]   
   
#np.savetxt(target_file, np.column_stack((x, y , z, vx, vy, vz, x1, y1 , z1, vx1, vy1, vz1, x2, y2 , z2, vx2, vy2, vz2)), \
  #fmt='%10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f ', header = 'x, y , z, vx, vy, vz, x1, y1 , z1, vx1, vy1, vz1, x2, y2 , z2, vx2, vy2, vz2')

#for i in range(0, Size) :
  #print star[2*i][0]*60000, star[2*i][1], star[2*i][2], star[2*i][3], star[2*i][4], star[2*i][5], star[2*i][6]
  #print star[2*i+1][0]*60000, star[2*i+1][1], star[2*i+1][2], star[2*i+1][3], star[2*i+1][4], star[2*i+1][5], star[2*i+1][6]

np.savetxt(outputFile, (star), fmt='%19.16f %19.16f %19.16f %19.16f %19.16f %19.16f %19.16f')
np.savetxt(wocmFile, (starwocm), fmt='%11.8f %11.8f %11.8f %11.8f %11.8f %11.8f %11.8f')
np.savetxt(cmFile, np.column_stack((x, y, z, vx, vy, vz)), fmt = '%11.8f %11.8f %11.8f %11.8f %11.8f %11.8f')

#pl.plot(star[:][1], star[:][2])
#pl.show()
###############################



