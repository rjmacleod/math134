# computes g^A mod N

print("Computes g^A mod N")
A = input("A is: ")
A = str(bin(int(A))[2:]) # A is taken as a string of binary digits
g = int(input("g is: "))
N = int(input("N is: "))

# n is g to ascending powers of 2 mod N
# if the binary digit is 1, g_a gets hit with n.
n = g
g_a = 1

for i in range(0,len(A)):
    if(A[len(A) - 1 - i] == "1"):
        g_a = (g_a * n) % N
    n = (n * n) % N

print(g_a)
    