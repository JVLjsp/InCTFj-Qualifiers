cypher="474h4152444d5e3358511942433i4218554h3i4d2854285141501958525g"
x='abcdefghijklmnopqrstuvwxyz1234567890'
y="defghijklmnopqrstuvwxyzabc9012345678"
ans=''
for i in cypher:
	for j,k in zip(x,y):
		if k == i:
			ans+=j
print ans.decode('hex')