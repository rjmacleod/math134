# Computes gcd(a,b) in the form of g = u * a + v * b 
# where u,v are integers, u > 0 and u is smallest possible
# int satisfying this.

# ref. An Intro. to Math. Crypt., 2nd ed, Hoffstein p50

def dwr(a, b):
    # Takes natural numb a and b, returns (q,r) such that
    # a = qb + r where q,r are integers and 0 <= r < b
    q = 1
    r = 0
    if (a > b):
        while ((q + 1) * b < a):
            q += 1
        r = a - q * b
        return q, r
    elif (a == b):
        return 1, 0
    else:
        return 0, a

a = 1
b = 1
print("Enter 2 natural numbers greater than 1.")
while (a < 2):
    a = input("a =  ")
    a = int(a)

while (b < 2):
    b = input("b =  ")
    b = int(b)

u = 1
g = a
x = 0
y = b

# Euclidean algorithm
while(y > 0):
    (q,t) = dwr(g,y)
    s = u - q * x
    (u,g) = (x,y)
    (x,y) = (s,t)

# making smallest positive u
while(u < 0):
    u += b/g
while(u - b/g > 0):
    u -= b/g
u = int(u)


v = int((g - a*u)/b)
print("gcd(a,b) = {}".format(g))
print("(u,v) = ({},{})".format(u,v))
print("{} * ({}) + {} * ({}) = {}".format(a,u,b,v,g))