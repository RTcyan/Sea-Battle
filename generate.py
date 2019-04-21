import random

def print_a(a):
    for i in range(len(a)):
        print('\t'.join(list(map(str,a[i]))))

def verif(i_s,j_s,a):
    for i in range(-1,2):
        for j in range(-1,2):
            if i_s+i>=0 and i_s+i<10 and j_s+j>=0 and j_s+j<10:
                if a[i_s+i][j_s+j]==1:
                    return 0
    return 1

def generate_k(a,k):
    while True:
        horizont = random.choice([True,False])
        if horizont:
            i_s = random.randint(0,9)
            j_s = random.randint(0,10-k)
        else:
            i_s = random.randint(0,10-k)
            j_s = random.randint(0,9)
        k_v=0
        for i in range(k):
            if horizont:
                k_v+=verif(i_s,j_s+i,a)
            else:
                k_v+=verif(i_s+i,j_s,a)
        if k_v==k:
            break
    for i in range(k):
        if horizont:
            a[i_s][j_s+i]=1
        else:
            a[i_s+i][j_s]=1
    return a

def generate():
    a=[[0 for j in range (10)] for i in range (10)]
    for i in range(4,0,-1):
        for j in range(5-i):
            a=generate_k(a,i)
    print_a(a)
    k=0
    for i in range(len(a)):
        for j in range(len(a[i])):
            k+=a[i][j]
    print(k)

generate()

