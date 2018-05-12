import random
import os
import numpy as np

#consts
N = 10
iterations = 100
eps = 0.5


def print_chessboard(A):
    for j in range(len(A)):
        for i in range(A.index(j)):
            print("*", end=' ')
        print("Q" , end=' ')
        for i in range(A.index(j)+1,len(A)):
            print("*", end=' ')
        print()
        
def swap(A,i,j):
    if  i != j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
      


def f(A):
    while True:
        pos0 = random.randrange(0,len(A))
        pos1 = random.randrange(0,len(A))
        if pos0 != pos1:
            swap(A,pos0,pos1)
            break

        
def count_coll(A):
    coll = 0
    n = len(A)
    for i in range(n):
        
        k = i - 1
        l = A[i] + 1
        #move in left and down
        while l <= n-1 and k >=0:
            if A[k] == l:
                coll += 1
            k = k - 1
            l = l + 1
            
        k = i + 1
        l = A[i] + 1
        # move in right and down
        while l <= n-1 and k<=n-1:
            if A[k] == l:
                coll += 1
            k = k + 1
            l = l + 1
            
    return coll

 
def main():
    print("Wait...")
    #init of pos
    F = [x for x in range(N)] 
    energy  = count_coll(F)
    T = 100
    alpha = 0.98
    while energy != 0 and T >= 0.999:
        for i in range(iterations):   
            if energy == 0:
                os.system('cls')
                print_chessboard(F)
                print('Energy =', energy)
                return
            next = F[:]
            f(next)
            if count_coll(next) < count_coll(F):
                F = next
                energy = count_coll(F)
            elif np.exp(-(energy - count_coll(next))/T) > eps:
                F = next
                energy = count_coll(F)

        T = alpha * T
    os.system('cls')
    print_chessboard(F)
    print('Energy =', energy)


main()
