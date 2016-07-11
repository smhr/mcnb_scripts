#! /usr/bin/env python
import fileinput, os

remnant_f = open('./bremnant.txt', 'w')
newline = os.linesep # Defines the newline based on your OS.

NBHBH = 0
NBHR = 0
NBHMs = 0
NRR = 0
NMsR = 0
NMsMs = 0
NBall = 0

row = '##  Time     NBHBH   NBHR   NBHMs  NRR   NMsR   NMsMs  NBall'
remnant_f.write(row + newline)
for line in fileinput.input(['fort.82']) : 
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
		m1 = int(a[2])
		m2 = int(a[3])
		if ( m1 == 14 and m2 == 14 ) :
			NBHBH = NBHBH + 1
		elif ( 10 <= m1 < 14 and m2 == 14 ) or ( 10 <= m2 < 14  and m1 == 14 ) :
			NBHR = NBHR + 1
		elif ( m1 < 10  and m2 == 14 ) or ( m2 < 10  and m1 == 14 ) :
			NBHMs = NBHMs + 1
		elif ( 10 <= m1 < 14 and 10 <= m2 < 14 ) :
			NRR = NRR + 1
		elif ( m1 < 10 and 10 <= m2 < 14 ) or ( m2 < 10 and 10 <= m1 < 14 ) :
			NMsR = NMsR + 1
		if ( m1 < 10 and m2 < 10 ) :
			NMsMs = NMsMs + 1
		
		NBall = NBHBH + NBHR + NBHMs + NRR + NMsR + NMsMs
	elif a[0] == "##" and a[1] == "END" : 
		remnant_f.write ( '%9.1f %6d %6d %6d %6d %6d %6d %6d \n' % (Time, NBHBH, NBHR, NBHMs, NRR, NMsR, NMsMs, NBall) )
		print ( '%9.1f %6d %6d %6d %6d %6d %6d %6d \n' % (Time, NBHBH, NBHR, NBHMs, NRR, NMsR, NMsMs, NBall) )
		NBHBH = 0
		NBHR = 0
		NBHMs = 0
		NRR = 0
		NMsR = 0
		NMsMs = 0
		NBall = 0
