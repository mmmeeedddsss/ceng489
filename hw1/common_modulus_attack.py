import sys
sys.setrecursionlimit(15000)

CSV_FILENAME = 'crackme.csv'
BASE = 16
DEBUG = False


def gcd(a, b):
    if a == 0:
        return b, 0, 1

    _gcd, x, y = gcd(b % a, a)
    return _gcd, y - (b//a) * x, x


# taken from https://stackoverflow.com/questions/34119110/negative-power-in-modular-pow
def modinv(a, N):
    _, x, _ = gcd(a, N)
    return x % N


with open(CSV_FILENAME, 'r') as f:
    inp_dict = {}
    lines = f.readlines()
    for line in lines:
        k, v = line.split(',')
        inp_dict[k] = v
    c1 = int(inp_dict['c1'], BASE)
    c2 = int(inp_dict['c2'], BASE)
    e1 = int(inp_dict['e1'], BASE)
    e2 = int(inp_dict['e2'], BASE)
    N  = int(inp_dict['n'], BASE)

    if e1 > e2:
        temp = e1
        e1 = e2
        e2 = temp

        temp = c1
        c1 = c2
        c2 = temp

gcdd, x, y = gcd(e1, e2)

if DEBUG:
    print('e1', e1)
    print('e2', e2)
    print('gcdd', gcdd)
    print("x,y", x, y)
    print("should be 1:", e1 * x + e2 * y)


c1_x = pow(c1, x, N) if x > 0 else pow(modinv(c1, N), -x, N)
c2_y = pow(c2, y, N) if y > 0 else pow(modinv(c2, N), -y, N)
m = (c1_x * c2_y) % N


hex_str_m = hex(m)[2:]

print(bytearray.fromhex( hex_str_m ).decode('latin-1') )
