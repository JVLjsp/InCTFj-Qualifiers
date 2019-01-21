import string
ct = "11161b0c1e12031d0c270c0d271a0a0d0c1d272d271f170c27110c270a0c05"
ct=ct.decode('hex')
possible_char = string.ascii_lowercase 
for i in possible_char:
	k=''
	for j in range(40):
		k+=i
	print '#'+k+"\n"
	pt = "".join(chr(ord(i) ^ ord(j)) for i,j in zip(ct,k))
	print pt