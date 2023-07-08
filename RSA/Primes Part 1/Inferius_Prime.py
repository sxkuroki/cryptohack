import primefac, greatest_common_divisor, math
from Crypto.Util.number import long_to_bytes, bytes_to_long

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
start = b'crypto{'
end = b'}'
a = 0
curr = ct
while True:
    if pow(round(pow(curr, 1/e)), e) == curr  :
        print(long_to_bytes(curr))
    curr += n