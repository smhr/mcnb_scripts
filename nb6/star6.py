#! /usr/bin/env python
import fileinput, os

remnant_f = open('nb-star', 'w')
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
Ltot = 0 # Total luminosity in solar luminosity unit
Mtot = 0 # Total mass in solar luminosity unit
MtoL = 0 # Mass to light ratio
#          0.0   104285  86952  17332      0      0      0      0      0      0      0      0      0      0      0      0      0      0  0   104284
row = '#  Time    Ntot    k0     k1        k2     k3    k4      k5     k6     k7     k8     k9     k10    k11    k12     WD    k13    k14 k15  N_all'
remnant_f.write(row + newline)
for line in fileinput.input(['fort.83']) : 
	#print (line)
	#print type(line)
	a = line.split()
	#print (a)
	#print (type(a[3]))
	#print (a[0])
	if a[0] == "##" and a[1] == "BEGIN" : 
		Ntot = int(a[2])
		Time = float(a[3])
		#print Ntot, Time
	elif a[0]!= "##" : 
		#print a[1],"******"
		Ltot = Ltot + 10.**float(a[4])
		Mtot = Mtot + float(a[3])
		MtoL = Mtot/Ltot
		if a[1] == "0" :
			#print a[0],a[1],"@@@@"
			k0 = k0 + 1 
		elif a[1] == "1" :
			#print a[0],a[1],"qqqq"
			k1 = k1 + 1
		elif a[1] == "2" : 
			k2 = k2 + 1
		elif a[1] == "3" :
			k3 = k3 + 1
		elif a[1] == "4" : 
			k4 = k4 + 1
		elif a[1] == "5" :
			k5 = k5 + 1
		elif a[1] == "6" : 
			k6 = k6 + 1
		elif a[1] == "7" :
			k7 = k7 +1
		elif a[1] == "8" : 
			k8 = k8 + 1
		elif a[1] == "9" :
			k9 = k9 +1
		elif a[1] == "10" :
			k10 = k10 + 1 
		elif a[1] == "11" :
			k11 = k11 + 1
		elif a[1] == "12" : 
			k12 = k12 + 1
		elif a[1] == "13" :
			k13 = k13 + 1
		elif a[1] == "14" : 
			k14 = k14 + 1
		elif a[1] == "15" :
			k15 = k15 + 1
		else:
			print ('ERROR')
			print (line)
			sexit ()
		WD = k10 + k11 + k12
		N_all = k0 + k1 + k2 + k3 + k4 + k5 + k6 + k7 + k8 + k9 + WD + k13 + k14 + k15
	elif a[0] == "##" and a[1] == "END" : 
		remnant_f.write ( '%9.1f %8d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %3d %3d %2d %8d %8.1f %8.1f %8.5f\n' \
		  % (Time, Ntot, k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, WD, k13, k14, k15, N_all, Ltot, Mtot, MtoL) )
		print ( '%9.1f %8d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %6d %3d %3d %2d %8d %8.1f %8.1f %8.5f\n' % \
		  (Time, Ntot, k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, WD, k13, k14, k15, N_all, Ltot, Mtot, MtoL) )
		
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
		Ltot = 0 # Total luminosity in solar luminosity unit
		Mtot = 0 # Total mass in solar luminosity unit
		MtoL = 0 # Mass to light ratio
		
