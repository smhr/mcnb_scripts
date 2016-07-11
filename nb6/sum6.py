#!/usr/bin/python 

import numpy as np
import os

star_file = 'nb-star'
binary_file = 'bremnant.txt'
escaped_file = 'nb-escaped'
total_file = 'nb-total'

print ''
print 'Input files are', star_file, 'and', escaped_file,'.'

Time, Ntot, k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, NWD, k13, k14, k15, N_all = \
  np.loadtxt(star_file, unpack=True, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), skiprows=1)

T_escaped, k0esc, k1esc, k2esc, k3esc, k4esc, k5esc, k6esc, k7esc, k8esc, k9esc, k10esc, k11esc, \
  k12esc, NWDesc, k13esc, k14esc, k15esc, N_allesc = np.loadtxt(escaped_file, unpack=True, usecols=\
    (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18), skiprows=1)

k = 0

for i in range(len(Time)):
  for j in range(len(T_escaped)) :
    if T_escaped[j] == Time[i] :
      k = k + 1
      
tot0 = np.zeros(k) 
tot1 = np.zeros(k)
tot2 = np.zeros(k)
tot3 = np.zeros(k)
tot4 = np.zeros(k)
tot5 = np.zeros(k)
tot6 = np.zeros(k)
tot7 = np.zeros(k)
tot8 = np.zeros(k)
tot9 = np.zeros(k)
tot10 = np.zeros(k)
tot11 = np.zeros(k)
tot12 = np.zeros(k)
wd_tot = np.zeros(k)
tot13 = np.zeros(k)
tot14 = np.zeros(k)
tot15 = np.zeros(k)
N_all_tot = np.zeros(k)

T_escaped2 = np.zeros(k)
k = 0
for i in range(len(Time)):
  for j in range(len(T_escaped)) :
    if T_escaped[j] == Time[i] :
      
      T_escaped2[k] = Time[i]
      tot0[k] = k0[i] + k0esc[j]
      tot1[k] = k1[i] + k1esc[j]
      tot2[k] = k2[i] + k2esc[j]
      tot3[k] = k3[i] + k3esc[j]
      tot4[k] = k4[i] + k4esc[j]
      tot5[k] = k5[i] + k5esc[j]
      tot6[k] = k6[i] + k6esc[j]
      tot7[k] = k7[i] + k7esc[j]
      tot8[k] = k8[i] + k8esc[j]
      tot9[k] = k9[i] + k9esc[j]     
      tot10[k] = k10[i] + k10esc[j]
      tot11[k] = k11[i] + k11esc[j]
      tot12[k] = k12[i] + k12esc[j]
      wd_tot[k] = NWD[i] + NWDesc[j]
      tot13[k] = k13[i] + k13esc[j]
      tot14[k] = k14[i] + k14esc[j]
      N_all_tot[k] = N_all[i] + N_allesc[j]
      k = k + 1
print 'First and last time in fort.83 are', Time[0], Time[-1]
print 'First and last time in ESC are', T_escaped2[0], T_escaped2[-1] 


np.savetxt(total_file, np.transpose([T_escaped2,tot0,tot1,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,wd_tot,tot13,tot14,tot15, N_all_tot]),\
  fmt='%6.1f %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %2d %9d' \
                 #137.2  86952  15704      6      0    115      3      5      0      0      0      0    265    358    623    709    167  0    104284
    , header = 'Time   k0     k1        k2    k3     k4     k5     k6     k7     k8     k9    k10    k11    k12    WD     k13    k14 k15   N_all_tot')

print 'Done! Please see',total_file,'for result.'
print ''