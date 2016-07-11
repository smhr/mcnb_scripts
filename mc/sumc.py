#!/usr/bin/python 

import numpy as np
import os

system_file = 'system.dat'
star_file = 'mc-star'
escaped_file = 'mc-escaped'
total_file = 'mc-total'

Time, nt, lms, lhg, lgb, lch, lfag, lsag, lhms, lhhg, lhgb, lHwd, lCOwd, lONwd, lmless,lwd, lns, lbh = np.loadtxt(system_file, unpack=True, usecols = \
(  1, 45, 138 ,142, 143, 144, 145,  146,  147,  148,  149,  265,   266,    267,   268,  139, 140, 141 ))

lmless, Mms, Mhg, Mgb, Mch, Mfag, Msag, Mhms, Mhhg, Mhgb, mHwd, mCOwd, mONwd, Mwd, Mns, Mbh, Mmless = np.loadtxt(system_file, unpack=True, usecols = \
(  268, 269, 270, 271, 272, 273,  274,  275,  276,  277,  278,  279,    280,  281, 282,  283, 284 ))
#       1     2    3    4    5     6     7     8      9     10    11     12         13   14   15


k = Time.size   
print 'size of Time = ',k
N_all = np.zeros(k)
N_all_esc = np.zeros(k)
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
totall = np.zeros(k)
sss =np.chararray(k)

for i in range(k):
  #k = k + 1
  tot1[i] = lms[i] + Mms[i]
  tot2[i] = lhg[i] + Mhg[i]
  tot3[i] = lgb[i] + Mgb[i]
  tot4[i] = lch[i] + Mch[i]
  tot5[i] = lfag[i] + Mfag[i]
  tot6[i] = lsag[i] + Msag[i]
  tot7[i] = lhms[i] + Mhms[i]
  tot8[i] = lhhg[i] + Mhhg[i]
  tot9[i] = lhgb[i] + Mhgb[i]
  tot10[i] = lHwd[i] + mHwd[i]
  tot11[i] = lCOwd[i] + mCOwd[i]
  tot12[i] = lONwd[i] + mONwd[i]
  wd_tot[i] = lwd[i] + Mwd[i]
  tot13[i] = lns[i] + Mns[i]
  tot14[i] = lbh[i] + Mbh[i]
  tot15[i] = lmless[i] + Mmless[i]
  totall[i] = tot1[i] + tot2[i] + tot3[i] + tot4[i] + tot5[i] + tot6[i] + tot7[i] + tot8[i] + tot9[i] + wd_tot[i] + tot13[i] + \
    tot14[i] + tot15[i]
  N_all[i] =  lms[i] + lhg[i] + lgb[i] + lch[i] + lfag[i] + lsag[i] + lhms[i] + lhhg[i] + lhgb[i] + lmless[i] +lwd[i] + lns[i] + lbh[i]
  N_all_esc[i] = Mms[i] + Mhg[i] + Mgb[i] + Mch[i] + Mfag[i] + Msag[i] + Mhms[i] + Mhhg[i] + Mhgb[i] + Mwd[i] +\
    Mns[i] + Mbh[i] + Mmless[i]
  sss[i] = '*'
  print 'Time = ', Time[i]
  
#newline = os.linesep # Defines the newline based on your OS.
#row = '##  Time    NHWD   NCOWD  NONWD    NWD     NN    NBH     N_other    N_all'
#tot_f.write(row + newline)
#tot_f.write ( '%9.1f %6d %6d %6d %6d %6d %6d \n' % (T_escaped2, NHWDtot, NCOWDtot, NONWDtot, NWDtot, NNtot, NBHtot) )
      

##numpy.savetxt(tot_file, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')

##np.savetxt(total_in_file, fmt='%6d %6d %6d %6d %6d %6d', (np.transpose([NHWDtot,NCOWDtot,NONWDtot,NWDtot,NNtot,NBHtot])))

np.savetxt(star_file, np.column_stack((Time, nt, lms, lhg, lgb, lch, lfag, lsag, lhms, lhhg, lhgb, lHwd, lCOwd, lONwd, lwd, lns, lbh, lmless, N_all)), \
  fmt='%9.1f %8d %13d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d  %6d %2d %8d', header = \
    '  Time      nt            k0&1     k2     k3     k4     k5     k6     k7     k8     k9     k10    k11    k12    WD    k13      k14 k15  N_all')

np.savetxt(escaped_file, np.column_stack((Time, Mms, Mhg, Mgb, Mch, Mfag, Msag, Mhms, Mhhg, Mhgb, mHwd, mCOwd, mONwd, Mwd, Mns, Mbh, Mmless, N_all_esc)), \
  fmt='%9.1f %13d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %2d %8d' , header = \
    ' Time            k0&1     k2     k3    k4      k5     k6     k7     k8     k9     k10    k11    k12    WD    k13    k14 k15   N_all_esc')

np.savetxt(total_file, np.column_stack((Time, tot1, tot2, tot3, tot4, tot5, tot6, tot7, tot8, tot9, tot10, tot11, tot12, wd_tot, tot13, tot14, tot15, totall)), \
  fmt='%6.1f %13d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %2d %9d', header = \
' Time        k0&1      k2     k3     k4     k5     k6     k7     k8     k9     k10    k11    k12    WD    k13    k14 k15   N_all_tot')
