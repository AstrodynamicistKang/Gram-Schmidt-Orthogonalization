print("This is a Gram-Schmidt Orthogonalization Python program.\n")

def dot(x,y):
    'Inner/dot product of vectors A and B.'
    z = 0
    for a,b in zip(x,y):
        z += a*b
    return z

def mag(x):
    'Magnitude of a vector.'
    z = 0
    for ele in x:
        z += ele**2
    return z**(0.5)

def unit(x):
    'Normalizes a vector.'
    z = []
    for a in x:
        z.append((1/mag(x))*a)
    return z

def scam(a,b):
    'Scalar multiplication'
    z = []
    for x in b:
        z.append(a*x)
    return z

def add(a,b):
    'Vector addition'
    z = []
    for x,y in zip(a,b):
        z.append(x+y)
    return z

def sub(a,b):
    'Vector subtraction'
    z = []
    for x,y in zip(a,b):
        z.append(x-y)
    return z

def ortho(x, TOL=1e-8):
    'The Gram-Schmidt orthogonalization function.'
        
    Ans = [unit(x[0])]

    for j in range(1,len(x)):
        Int = []
        for anumber in range(0, j):
            w = scam(dot(Ans[anumber],x[j]), Ans[anumber])
            Int.append(w)
        while (len(Int) > 1):
            temp = add(Int[0], Int[1])
            Int.remove(Int[0])
            Int.remove(Int[0])
            Int.insert(1, temp)
        check = sub(list(x[j]), Int[0])
        for ele in range(0, len(check)):
            if check[ele] < TOL:
                check[ele] = 0
        try:
            Ans.append(unit(check))
        except ZeroDivisionError:
            z_v = []
            for x in range(len(check)):
                z_v.append(0)
            Ans.append([z_v])

    return Ans

ld = [(1,1,-1),(1,2,1),(2,3,0)]
