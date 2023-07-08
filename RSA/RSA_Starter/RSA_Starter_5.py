import greatest_common_divisor as gcd
from Crypto.Util import number
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
N = p * q
e = 65537
phi = (p-1) * (q-1)
d = gcd.extendedEuclideanAlgo(e, phi)
c = 77578995801157823671636298847186723593814843845525223303932

print(pow(c, d, N))
