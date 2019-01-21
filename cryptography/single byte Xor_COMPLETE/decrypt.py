ct = "1314190e1c1001024a0825194e145d0e251849251f4e091316032518084a11491407"
ct=ct.decode('hex')
k = 'z'
for i in range(20):
	k+=k
pt = "".join(chr(ord(i) ^ ord(j)) for i,j in zip(ct,k))
print pt