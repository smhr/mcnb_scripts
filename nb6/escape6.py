#! /usr/bin/env python
import fileinput, os
import sys

remnant_f = open('nb-escaped', 'w')
newline = os.linesep # Defines the newline based on your OS.

k0 = 0 # Number of deeply or fully convective low mass ms star
k1 = 0 # Number of main sequence stars
k2 = 0 # Number of hertzsprung gap stars
k3 = 0 # Number of first giant branch stars
k4 = 0 # Number of core helium burning stars
k5 = 0 # Number of first AGB branch stars
k6 = 0 # Number of second AGB branch stars
k7 = 0 # Number of ms naked helium stars
k8 = 0 # Number of hertzsprung gap naked helium stars
k9 = 0 # Number of giant branch naked helium stars
k10 = 0 # Number of helium white dwarfs (KSTAR = 10)
k11 = 0 # Number of carbon oxygen white dwarfs (KSTAR = 11)
k12 = 0 # Number of oxygen neon white dwarfs (KSTAR = 12)
WD = 0 # Total number of white dwarfs
k13 = 0 # Number of neutron stars (KSTAR = 13)
k14 = 0 # Number of Black holes (KSTAR = 14)
k15 = 0
N_all = 0

#Time = 137.2
Time = float(sys.argv[1])

i = 0
k = 0
row = '#  Time       k0     k1     k2     k3    k4      k5     k6     k7     k8     k9     k10    k11    k12    WD    k13    k14 k15   N_all_esc'
remnant_f.write(row + newline)
for line in fileinput.input(['ESC']) : 
#	print (line)
	#print type(line)
	a = line.split()
	#print (a)
	#print (type(a[3]))
	#i = i + 1
	
	tt = float(a[0])
	
	#print "***",tt,Time,a[-2]
	if tt == Time : 
		
		if a[-2] == "0" :
			#print a[0],a[-2],"@@@@"
			k0 = k0 + 1 
		elif a[-2] == "1" :
			#print a[0],a[-2],"qqqq"
			k1 = k1 + 1
		elif a[-2] == "2" : 
			k2 = k2 + 1
		elif a[-2] == "3" :
			k3 = k3 + 1
		elif a[-2] == "4" : 
			k4 = k4 + 1
		elif a[-2] == "5" :
			k5 = k5 + 1
		elif a[-2] == "6" : 
			k6 = k6 + 1
		elif a[-2] == "7" :
			k7 = k7 +1
		elif a[-2] == "8" : 
			k8 = k8 + 1
		elif a[-2] == "9" :
			k9 = k9 +1
		elif a[-2] == "10" :
			k10 = k10 + 1 
		elif a[-2] == "11" :
			k11 = k11 + 1
		elif a[-2] == "12" : 
			k12 = k12 + 1
		elif a[-2] == "13" :
			k13 = k13 + 1
		elif a[-2] == "14" : 
			k14 = k14 + 1
		elif a[-2] == "15" :
			k15 = k15 + 1
	        else :
	                print 'ERROR'
	                print (line)
	                exit ()
		WD = k10 + k11 + k12
		N_all = k0 + k1 + k2 + k3 + k4 + k5 + k6 + k7 + k8 + k9 + WD + k13 + k14 + k15
			
	else :
		remnant_f.write ( '%9.1f %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %2d %8d \n' % \
		  (Time, k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, WD, k13, k14, k15, N_all) )
		
		if a[-2] == "0" :
			#print a[0],a[-2],"@@@@"
			k0 = k0 + 1 
		elif a[-2] == "1" :
			#print a[0],a[-2],"qqqq"
			k1 = k1 + 1
		elif a[-2] == "2" : 
			k2 = k2 + 1
		elif a[-2] == "3" :
			k3 = k3 + 1
		elif a[-2] == "4" : 
			k4 = k4 + 1
		elif a[-2] == "5" :
			k5 = k5 + 1
		elif a[-2] == "6" : 
			k6 = k6 + 1
		elif a[-2] == "7" :
			k7 = k7 +1
		elif a[-2] == "8" : 
			k8 = k8 + 1
		elif a[-2] == "9" :
			k9 = k9 +1
		elif a[-2] == "10" :
			k10 = k10 + 1 
		elif a[-2] == "11" :
			k11 = k11 + 1
		elif a[-2] == "12" : 
			k12 = k12 + 1
		elif a[-2] == "13" :
			k13 = k13 + 1
		elif a[-2] == "14" : 
			k14 = k14 + 1
		elif a[-2] == "15" :
			k15 = k15 + 1
	        else :
	                print 'ERROR'
	                print (line)
	                exit ()
			
		WD = k10 + k11 + k12
		N_all = k0 + k1 + k2 + k3 + k4 + k5 + k6 + k7 + k8 + k9 + WD + k13 + k14 + k15
		
		print ( '%9.1f %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %2d %8d \n' % \
		  (Time, k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, WD, k13, k14, k15, N_all) )
			
		Time = tt

remnant_f.write ( '%9.1f %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %2d %8d \n' % \
		  (Time, k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, WD, k13, k14, k15, N_all) )
		
		

