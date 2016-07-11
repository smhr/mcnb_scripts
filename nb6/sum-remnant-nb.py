#!/usr/bin/python 

import numpy as np
import os

remnant_in_file = 'remnant.txt'
bremnant_in_file = 'bremnant.txt'
escaped_in_file = 'escaped.txt'
total_in_file = 'total.txt'
#tot_f = open('./total.txt', 'w')

T_remnant, NHWD, NCOWD, NONWD, NWD, NN, NBH = np.loadtxt(remnant_in_file, unpack=True, usecols=(0,2,3,4,5,6,7), skiprows=1)
T_bremnant, NBHBH, NBHR, NBHMs, NRR, NMsR, NMsMs = np.loadtxt(bremnant_in_file, unpack=True, usecols=(0,1,2,3,4,5,6), skiprows=1) 
#print T_bremnant[0]
T_escaped, NHWDesc, NCOWDesc, NONWDesc, NWDesc, NNesc, NBHesc = np.loadtxt(escaped_in_file, unpack=True, usecols=(0,1,2,3,4,5,6), skiprows=1)
#print T_escaped[0]
#print T_remnant.size
#print T_bremnant.size
#print T_escaped.size
k = 0

for i in range(len(T_remnant)):
  #print 'i = ',i
  for j in range(len(T_escaped)) :
    if T_escaped[j] == T_remnant[i] :
      #print T_escaped[j],T_remnant[i]
      #print k,j,i
      k = k + 1
      
print 'k = ',k
      
NHWDtot = np.zeros(k)
NCOWDtot = np.zeros(k)
NONWDtot = np.zeros(k)
NWDtot = np.zeros(k)
NNtot = np.zeros(k)
NBHtot = np.zeros(k)
T_escaped2 = np.zeros(k)
k = 0
for i in range(len(T_remnant)):
  for j in range(len(T_escaped)) :
    if T_escaped[j] == T_remnant[i] :
      
      T_escaped2[k] = T_remnant[i]
      #print T_escaped2[k]
      NHWDtot[k] = NHWD[i] + NHWDesc[j]
      NCOWDtot[k] = NCOWD[i] + NCOWDesc[j]
      NONWDtot[k] = NONWD[i] + NONWDesc[j]
      NWDtot[k] = NWD[i] + NWDesc[j]
      NNtot[k] = NN[i] + NNesc[j]
      NBHtot[k] = NBH[i] + NBHesc[j]
      print k,j,i
      print 'NBHtot[k],NBHesc[j],NBH[i]',NBHtot[k],NBHesc[j],NBH[i]
      
      k = k + 1

#newline = os.linesep # Defines the newline based on your OS.
#row = '##  Time    NHWD   NCOWD  NONWD    NWD     NN    NBH     N_other    N_all'
#tot_f.write(row + newline)
#tot_f.write ( '%9.1f %6d %6d %6d %6d %6d %6d \n' % (T_escaped2, NHWDtot, NCOWDtot, NONWDtot, NWDtot, NNtot, NBHtot) )
      

##numpy.savetxt(tot_file, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')

##np.savetxt(total_in_file, fmt='%6d %6d %6d %6d %6d %6d', (np.transpose([NHWDtot,NCOWDtot,NONWDtot,NWDtot,NNtot,NBHtot])))

np.savetxt(total_in_file, np.transpose([T_escaped2, NHWDtot,NCOWDtot,NONWDtot,NWDtot,NNtot,NBHtot]),\
  fmt='%6.1f %7d %7d %7d %7d %7d %7d', header='Time    NHWD     NCOWD   NONWD    NWD     NN     NBH')