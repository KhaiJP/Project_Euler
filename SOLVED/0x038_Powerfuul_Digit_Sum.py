import time

begin = time.time()
    
M = 1
for a in range(2,100):
    for b in range(2,100):
        ref=sum([int(k) for k in str(pow(a,b))])
        if ref > M:
            M = ref
            i=a
            j=b

print(M , i, j)
print(time.time()-begin)
