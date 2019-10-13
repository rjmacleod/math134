# Takes 2 natural numbers a,b and computes gcd(a,b)
# in form g = ax + by for integers x,y.

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

x = max(a,b)
y = min(a,b)
(q,r) = dwr(x,y)
temp_r = 0

while(r > 1):
    last_r = r
    x = y
    y = r
    (q,r) = dwr(x,y)

if(r == 0):
    g = last_r
else:
    g = 1

print("gcd({}, {}) = {}.".format(a,b,g))