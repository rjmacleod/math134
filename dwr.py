# Takes 2 natural numbers a and b and
# computes integers q and r st a = qb * r and 0 <= r < b.

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

print("Enter natural numbers a and b, a > b.")
while (a < 2):
    a = input("a =  ")
    a = int(a)

while (b < 2):
    b = input("b =  ")
    b = int(b)

(q,r) = dwr(a,b)

print("{} = {} * {} + {}".format(a,q,b,r))