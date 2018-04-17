# message+pad(1+0)+64 bit length is 512, block size
# each block is split into 32 bit chunks, that is 16 words
# In an array of 80 words, first 16 are those from previous step, rest are: Wi = W(i-3) xor W(i-8) xor W(i-14) xor W(i-16) where 16<i<=80
# Initialise a 160 bit shift register with values S1,S2,S3,S4,S5
# for i = 1 to 80
# 	temp <- S5 + (S1<<5) + Fi(S2,S3,S4) + Ki + Wi
#	S5 <- S4
#	S4 <- S3
#	S3 <- S2
#	S2 <- S1
#	S1 <- temp
# where Fi(S2,S3,S4) = (S2^S3)v(~S2^S4) 1<=i<=20
# 	Fi(S2,S3,S4) = S2 xor S3 xor S4 21<=i<=40
# 	Fi(S2,S3,S4) = (S2^S3)v(S2^S4)v(S3^S4) 41<=i<=60
#	Fi(S2,S3,S4) = S2 xor S3 xor S4 61<=i<=80
import textwrap

def wordret(wa,wb,wc,wd):
	a=int(wa,2)^int(wb,2)^int(wc,2)^int(wd,2)
	return '{0:032b}'.format(a)

def F1(S2,S3,S4):
	return (S2&S3)|(~S2&S4)
def F2(S2,S3,S4):
	return S2^S3^S4
def F3(S2,S3,S4):
	return (S2&S3)|(S2&S4)|(S3&S4)
def F4(S2,S3,S4):
	return S2^S3^S4

s1 = 0x67452301
s2 = 0xEFCDAB89
s3 = 0x98BADCFE
s4 = 0x10325476
s5 = 0xC3D2E1F0

message=input("Enter a message")
binmessage=''.join(format(ord(x), 'b') for x in message)
#binmessage='{0:b}'.format(ord(x) for x in message
binmessage+='1'
length=len(binmessage)
for i in range(length,448):
	binmessage+='0'
length='{0:064b}'.format(length)
binmessage+=length
#print(binmessage)
#print(len(binmessage))
words=[]
words=textwrap.wrap(binmessage, 32)
print(len(words))
for i in range(16,80):
	words.append(wordret(words[i-3],words[i-8],words[i-14],words[i-16]))

print(words)

k1=0x5A827999
k2=0x6ED9EBA1
k3=0x8F1BBCDC
k4=0xCA62C1D6

for i in range(0,20):
	temp=s5+(s1<<5)+F1(s2,s3,s4)+k1+words[i]
	s5=s4
	s4=s3
	s3=s2
	s2=s1
	s1=temp
for i in range(20,40):
	temp=s5+(s1<<5)+F2(s2,s3,s4)+k2+words[i]
	s5=s4
	s4=s3
	s3=s2
	s2=s1
	s1=temp
for i in range(40,60):
	temp=s5+(s1<<5)+F3(s2,s3,s4)+k3+words[i]
	s5=s4
	s4=s3
	s3=s2
	s2=s1
	s1=temp
for i in range(60,80):
	temp=s5+(s1<<5)+F4(s2,s3,s4)+k4+words[i]
	s5=s4
	s4=s3
	s3=s2
	s2=s1
	s1=temp
	


