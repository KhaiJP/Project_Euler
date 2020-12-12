#!/usr/bin/env python
# coding: utf-8

# In[12]:

import numpy as np
def ispm(num:int)->bool:
    '''
    This fucntion is to jedge if the input is prime by means of Rabin_Miller primality test.
    '''
    import random
    if num==2: return True
    if num==1 or num&1==0: return False
    d=(num-1)//2
    while d&1==0:
        d//=2
    for j in range(100):
        rand=random.randint(1,num-1)
        t=d
        y=pow(rand,t,num)
        while t!=num-1 and y!=1 and y!=num-1:
            y=y=pow(y,2,num)
            t*=2
        if y !=num-1 and t%2==0:
            return False
    return True

def istpm(n1:int,n2:int)->bool:
    if ispm(n1) and ispm(n2):return True
    else:False

def pms(SUP:int, INF=2)->list:
    '''
    This function is to generate the list of prime numbers up to SUP (from INF if SUP>=3)
    '''
    if SUP<2: return []
    elif SUP<INF: return print("1st variavle bust be greater than or equal to 2nd variable")
    elif SUP==2: return [2]
    RESULT=[]
    if SUP>2:
        if INF==2: RESULT.append(2)
        if INF%2==0:INF+=1
        for i in range(INF,SUP+1,2):
            if ispm(i):
                RESULT.append(i)
        return RESULT
    
def npm(N:int)->int:
    '''
    This function is to generate the N-th prime.
    '''
    if N==1:return 2
    cnt=2
    n=3
    while True:
        if ispm(n):
            if cnt==num:
                return n
            cnt+=1
        n+=2

def lp(num:int)->int:
    '''
    This function is to generate the least prime factor of num
    '''
    if num%2==0:
        return 2
    for i in range(3, num+1, 2):
        if num%i==0:
            return i

def gp(num:int)->int:
    '''
    This function is to generate the greatest prime factor of num
    '''
    if ispm(num):
        return num
    while True:
        LP=lp(num)
        while num%LP==0:
            num//=LP
        if num==1:
            return LP
        if ispm(num):
            return num
        
def pfpast(num:int)->list:
    '''
    This function is to generate the list of prime factors of num
    '''
    if num==1:return []
    elif ispm(num): return [num]
    primes=pms(num//lp(num))
    return [i for i in primes if num%i==0]

def pf(num:int)->list:
    '''
    This function is to generate the prime factoring as the list of tuples.
    The first component of the tuple is the prime factor and the second is the power.
    '''
    if num==1: return []
    if ispm(num): return [(num,1)]
    result=[] #initilizing the result; the list of tuples of base and power
    while True:
        cnt=0 #the index counting the power
        LP=lp(num)
        while num%LP==0:
            num//=LP
            cnt+=1
        result.append((LP,cnt))
        if num==1:
            return result

def pfs(num:int)->list:
    return [j[0] for j in pf(num)]

# def DIV(num:int)->list:
#     if ispm(num) or num==1: return [1]+[j[0] for j in fac(num)]
#     return [1]+[j[0] for j in fac(num)]+[num]
def div(num:int)->list:
    '''
    This function is to generate the list whose components are the divisors of num.
    '''
    if num==4:
        return [1,2,4]
    cnt=1
    variable=2
    result=[1,num]
    upper_limit=num//2
    while variable<upper_limit:
        if num%variable==0:
            result.insert(cnt,variable)
            result.insert(-1*cnt,num//variable)
            cnt+=1
            upper_limit=num//variable
        variable+=1
    if num**(1/2) in result:
        result.remove(num**(1/2))
    return result

def phifunc(num:int)->int:
    '''
    This function is to calculate the result of Euler's totient(Phi) function.
    '''
    LIST_OF_PRIME_FACTORS=pf(num)
    RESULT=1
    for j in range(len(LIST_OF_PRIME_FACTORS)):
        RESULT*=LIST_OF_PRIME_FACTORS[j][0]**(LIST_OF_PRIME_FACTORS[j][1]-1)*(LIST_OF_PRIME_FACTORS[j][0]-1)
    return RESULT

def order(num:int,BASE=10)->int:
    '''
    This function is to generate the order of num in the base 10(programmable).
    '''
    if BASE==10:
        if num%2==0 or num%5==0: return print("ERROR!")
    else:
        LIST_OF_PRIME_FACTORS=pfs(BASE)
        BOOL=True
        for j in range(len(LIST_OF_PRIME_FACTORS)):
            BOOL=BOOL and (not num%LIST_OF_PRIME_FACTORS[j]==0)
        if not BOOL: return print("ERROR!")
    cnt=1
    while True:
        if BASE**cnt%num==1: return cnt
        else: cnt+=1
    
def GCD(big:int,small:int)->int:
    if small==0:
        return big
    else:
        return gcd(small,big%small)
def gcd(n1,n2):
    '''
    This function is to calculate the gcd
    '''
    return GCD(max(n1, n2),min(n1,n2))

def lcm(n1,n2):
    '''
    This function is tocalculate the lcm
    '''
    return n1*n2//gcd(n1,n2)

def cop(n1:int,n2:int)->bool:
    '''
    This function is to judge if the two numbers are coprime.
    '''
    if gcd(n1,n2)==1:
        return True
    else:
        return False
    
def prsum(num:int)->int:
    '''
    This function is to calculate the sum of the proper divisors of num.
    '''
    return sum(div(num))-num

def isdef(num:int)->bool:
    return prsum(num)<num

def isabu(num:int)->bool:
    return prsum(num)>num
    
def ispct(num:int)->bool:
    '''
    This function is to judge if the input number is the perfect.
    '''
    return prsum(num)==num
    
def isamcb(n1:int,n2:int)->bool:
    '''
    This function is to judge if the two numbers are amicable(友愛数)
    '''
    return prsum(n1)==n2 and prsum(n2)==n1


def n_base_expansion(base:int,num:int)->list:
    a=[]
    while num>0:
        a.insert(0,num%base)
        num//=base
    return a

def d_expansion(num):
    return n_base_expansion(10,num)

def b_expansion(num):
    return n_base_expansion(2,num)

def o_expansion(num):
    return n_base_expansion(8,num)

def h_expansion(num):
    return n_base_expansion(16,num)

def pal(ls:list)->bool:
    '''
    This function is to jedge if the given list is palindrome
    '''
    bl=True
    for i in range(len(ls)//2):
        bl=(ls[i]==ls[-1*(i+1)])
        if not bl:
            return False
    return True

def Sum(num):
    return num*(num+1)//2

def Fibonacci_Length(length_of_sequence:int)->list:
    '''
    This function is to return the list of Fibonacci sequence with starting a[0]=1 and a[1]=2.
    The length_of_sequence must be greater than 1
    '''
    if length_of_sequence<2:
        return print('Error! The arg must be greater than 1!')
    a=[1,2]
    for i in range(length_of_sequence-2):
        a.append(a[i]+a[i+1])
    return a

def Fibonacci_Sup(num:int)->list:
    '''
    This function is to find the length of the Fibonacci sequence 
    whose maximum value does not exeed num.
    '''
    i=0
    a=Fibonacci_Length(2)
    while a[-1]<num:
        a.append(a[i]+a[i+1])
        i+=1
    a.pop()
    return a

def fac(num:int)->int:
    '''
    This function is to calculate the factorial of num.
    '''
    if num==0 or num==1:
        return 1
    res=1
    for i in range(2,num+1):
        res*=i
    return res

def pytset(x:int,y:int)->list:
    '''
    This function is to generate the set(list) of the Pythagorean triplet
    according to the theorem that any pythagorean triplet can be represented by 
    ( (x^2-y^2) , (2xy) , (x^2+y^2) ) as (x^2-y^2)^2 + (2xy)^2 = (x^2+y^2)^2.
    '''
    if x==y:
        return print('the two input numbers must not be the same.')
    else:
        return [min(max(x,y)**2-min(x,y)**2,2*x*y),max(max(x,y)**2-min(x,y)**2,2*x*y),x**2+y**2]
    
# def perm(ls:list)->list:
#     '''
#     This function is to generate the lists that each component corresponds the list
#     whose components are the purmutaion of the original list's components.
#     If the input is [1,2], then the output is [[1,2],[2,1]]
#     '''
#     if len(ls)==1:
#         return [ls]
#     elif len(ls)==2:
#         result=[ls]
#         LS=[ls[1],ls[0]]
#         result.append(LS)
#         return result
#     elif len(ls)>2:

def cycle(lst:list)->list:
    res=[lst]
    le=len(lst)
    for i in range(1,le):
        LST=list(lst)
        for j in range(i):
            LST.append(LST[0])
            del LST[0]
        res.append(LST)
    return res



    
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   