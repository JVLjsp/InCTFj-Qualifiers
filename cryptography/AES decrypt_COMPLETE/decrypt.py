from Crypto.Cipher import AES

def padding(message, block_size):    
	ch = block_size - len(message) % block_size
	return message + bytes(chr(ch) * ch)


def AES_decrypt(key, message):
	a = AES.new(key,AES.MODE_ECB)
	pt= a.decrypt(padding(message,16))
	return pt

if __name__=="__main__":
	key = "fq3tjj#fm3)49faf"
	ct = "cd4718367a60b379f74e999ae41d8daeb1c65cc012ef4edbc1a21da74390ba0b07d82ea636b6bd7ab877000220f13e02"
	ct = ct.decode('hex')
	pt = AES_decrypt(key,ct)
	print pt
	