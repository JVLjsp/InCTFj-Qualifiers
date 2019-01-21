import random

def decrypt():
	ct ="69747b3365305f333364666e6670615f6e755f633372636a6c7364377364302e7d"
	ct=ct.decode('hex')
	pt = ""
	for i in range(3,13):
		turns = i
		print "#"+str(turns)
		for i in range(turns):
			for j in range(0,len(ct)-i,turns):
				pt+=ct[i+j]
		
		if "inctfj" in pt:
			print pt


decrypt()
