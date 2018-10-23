P=[]
for j in range(1,102):
    X=[]
    a=j
    for i in range(a-1,1,-1):
        c= a%i
        X.append(c)
    if all ([c!=0 for c in X]):
        P.append(a)
print(P)

        
    
