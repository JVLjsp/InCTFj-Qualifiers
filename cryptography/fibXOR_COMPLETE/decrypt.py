import itertools
import string
ct = "010f00170d011059375f0058140609563e50153e1457103c1050001611503c0b531c340f5a0f34125b1e340919585f00345a1f54164b31581d48091a5b4809480f5b06591d1b494831581d480c590c4809480f1a5b091c480b510340412952551315184102510f06130056140d005650510f1241510f4112510d17080f064115095012410209550d0d520f06524040".decode('hex')
n=10
def fibonacci(n):
	ar = []
	a,b = 1,1
	ar.append(a)
	ar.append(b)
	for i in range(n-2):
		c = a + b
		ar.append(c)
		a = b
		b = c	
	return ar

def keygeneration(k):
	assert len(k) == 4
	key = ""
	ar = fibonacci(n)
	for i in range(len(ar)):
		key = key + k[i%len(k)]*ar[i]
	return key
def decrypt(ct,k):
	pt = ""
	flag = "".join(chr(ord(i) ^ ord(j)) for i,j in zip(ct,k))
	if "inctfj" in flag:
		print flag
myalphabet = string.ascii_lowercase 
def crack(maxlen, alphabet=myalphabet):
  for i in range(4,5):
    for s in itertools.product(alphabet, repeat=i):
      k= ''.join(s)
      k=keygeneration(k)
      decrypt(ct,k)



word_list=crack(4)
print word_list

