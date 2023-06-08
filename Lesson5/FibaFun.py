def Fiba(n) : 
    print(n)
    if n in [0,1] :
        return n
    return Fiba(n - 1) + Fiba(n - 2)

