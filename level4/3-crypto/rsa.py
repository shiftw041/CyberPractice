from Crypto.Util.number import *
from sympy import nextprime

flag = 'vmc{****************}'

part1 = flag[:19]
part2 = flag[19:]
assert (len(flag) == 37)

p1 = getStrongPrime(1152)
p2 = nextprime(p1)
try:
    if p2 - p1 > 1000:
        raise Exception("Error")
except:
    exit()

q1 = getStrongPrime(512)
q2 = nextprime(q1)

n1 = p1 * p1 * q1
e1 = getStrongPrime(1024)
msg1 = bytes_to_long(part1.encode())
c1 = pow(msg1, e1, n1)

n2 = p2 * p2 * q2
e2 = nextprime(e1)
msg2 = bytes_to_long(part2.encode())
c2 = pow(msg2, e2, n2)

output = open('secret.txt', 'w')
output.write('n1=' + str(n1) + '\n')
output.write('c1=' + str(c1) + '\n')
output.write('e1=' + str(e1) + '\n')
output.write('n2=' + str(n2) + '\n')
output.write('c2=' + str(c2) + '\n')
output.write('e2=' + str(e2) + '\n')
output.close()
