#!/usr/bin/python

import numpy as np
import os
import operator
import sys

input_file = open('./fort.10', 'r')
target_file = open('./single_nbody.dat', 'w')
target_file_masses_sorted = open('./single_nbody_mass_sorted.dat', 'w')

Nbody_masses,x,y,z,vx,vy,vz=np.loadtxt(input_file,unpack=True,usecols=(0,1,2,3,4,5,6))
#data = np.loadtxt(input_file,unpack=True,usecols=(0,1,2,3,4,5,6))
#print type(data)
masses_sum = float(sys.argv[1])
#print masses_sum
#Nbody_masses = data[0,:]
#print data[0,:]

masses = Nbody_masses * masses_sum
#print type(x)
np.savetxt(target_file, np.transpose([masses,x,y,z,vx,vy,vz]),fmt='%20.16f',delimiter=' ')

#print Nbody_masses
#print masses
#newline = os.linesep # Defines the newline based on your OS.

#data = Nbody_masses,x,y,z,vx,vy,vz
#data_masses_sorted = np.zeros(data.size)
ind=np.argsort((masses))

print 'N =', Nbody_masses.size
print 'M = ', masses_sum 
aa = Nbody_masses.size
s_masses = np.zeros((aa))
s_x = np.zeros((aa))
s_y = np.zeros((aa))
s_z = np.zeros((aa))
s_vx = np.zeros((aa))
s_vy = np.zeros((aa))
s_vz = np.zeros((aa))

#print s_masses
#print s_masses.shape
j = 0
for i in ind:
  s_masses[j] = masses[i]
  s_x[j] = x[i]
  s_y[j] = y[i]
  s_z[j] = z[i]
  s_vx[j] = vx[i]
  s_vy[j] = vy[i]
  s_vz[j] = vz[i]
  #print '%10.4f %10.4f %10.4f %10.4f %10.4f %10.4f %10.4f' %(masses[i],x[i],y[i],z[i],vx[i],vy[i],vz[i])
  j = j + 1
#print s_masses[104283]


np.savetxt(target_file_masses_sorted, np.transpose([s_masses,s_x,s_y,s_z,s_vx,s_vy,s_vz]), fmt='%20.16f', delimiter=' ')
#np.savetxt(target_file_masses_sorted, (b),fmt='%20.16f',delimiter=' ')


#l1=(linecache.getline(input_file, 1))
#l2=(linecache.getline(input_file, 2))
#l3=(linecache.getline(input_file, 3))
#l4=(linecache.getline(input_file, 4))
#l5=(linecache.getline(input_file, 5))
#l6=(linecache.getline(input_file, 6))

#ls1=l1.split()
#ls2=l2.split()
#ls3=l3.split()
#ls4=l4.split()
#ls5=l5.split()
#ls6=l6.split()
#ls7=l7.split()

#target_file.write(Nbody_masses,x,y,z,vx,vy,vz + newline)
#target_file.close()

