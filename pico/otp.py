import hashlib
import string
import itertools
import gmpy2
from pwn import *

r = remote("mercury.picoctf.net", 27379)
data = r.recv().split()
print(data)
start = data[6][1:-1].decode("utf-8")
print(start)
hash_end = data[-1].decode("utf-8")
print(hash_end)
charset = string.ascii_letters+string.digits+string.punctuation
for i in itertools.product(charset, repeat=5):
    send = start+(''.join(i))
    hash_send = hashlib.md5(send.encode()).hexdigest()
    if hash_send[-6:] == hash_end:
        print(send)
        break
r.sendline(send)
n_data = r.recvline()
e_data = r.recvline()
print(n_data)
n = gmpy2.mpz(int(n_data[18:-1].decode("utf-8")))
print(e_data)
e = gmpy2.mpz(int(e_data[8:-1].decode("utf-8")))
m = 2

for dp in range(1,(2**20)+1):
    p = gmpy2.gcd(gmpy2.mpz(m-pow(m, e*dp, n)), n)
    if p > 1:
        print(dp, p)
        q = n//p
        print(p*q==n)
        print(int(p+q))
        break
    if dp%10000==0:
        print("Tried",dp,"numbers so far!")

r.interactive()
r.close()