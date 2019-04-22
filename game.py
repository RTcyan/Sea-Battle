import generate

def print_a(a):

    a_time=[[0 for j in range(11)] for i in range(11)]

    for i in range(len(a_time)):
        for j in range(len(a_time[i])):
            if i==0 and j==0:
                a_time[i][j]=' '
            elif i==0:
                a_time[i][j]=j
            elif j==0:
                a_time[i][j]=i

    for i in range(len(a)):
        for j in range(len(a)):
            a_time[i+1][j+1]=a[i][j]

    for i in range(len(a_time)):
        print('\t'.join(list(map(str, a_time[i]))))


def secretField(a):
    return [['~' for j in range (len(a[i]))] for i in range(len(a))]

def killShip(secretMap,i_s,j_s):
    secretMap[i_s][j_s] = 'X'
    for i in range(-1,2):
        for j in range(-1,2):
            if i!=0 or j!=0:
                if i_s+i>=0 and i_s+i<10 and j_s+j>=0 and j_s+j<10:
                    if secretMap[i_s + i][j_s + j] == '+':
                        killShip(secretMap,i_s+i,j_s+j)
                    elif secretMap[i_s + i][j_s + j]!='X':
                        secretMap[i_s+i][j_s+j]='x'

def verif(i_s,j_s,secretMap,shipMap,i_pred=-1,j_pred=-1):
    for i in range(-1,2):
        if i!=0:
            if i_s+i>=0 and i_s+i<10:
                if shipMap[i_s+i][j_s]==1 and i_s+i!=i_pred:
                    return 1
            if j_s + i >= 0 and j_s + i < 10:
                if shipMap[i_s][j_s+i]==1 and i_s+i!=i_pred:
                    return 1

    for i in range(-1,2):
        if i != 0:
            if j_s+i>=0 and j_s+i<10:
                if secretMap[i_s][j_s+i]=='+' and j_s+i!=j_pred:
                    return verif(i_s, j_s + i, secretMap, shipMap, i_s, j_s)
            if i_s + i >= 0 and i_s + i < 10:
                if secretMap[i_s+i][j_s]=='+' and i_s+i!=i_pred:
                    return verif(i_s+i,j_s,secretMap,shipMap,i_s,j_s)
    return 0


def shot(shipMap,secretMap):
    while True:
        try:
            i, j = map(int, input('Введите координаты через пробел: ').split())
            if shipMap[i - 1][j - 1] == 1:
                secretMap[i - 1][j - 1] = '+'
                shipMap[i - 1][j - 1] = 0
                print('Попал!')
                if verif(i - 1, j - 1, secretMap, shipMap) == 0:
                    print('Убил!')
                    killShip(secretMap, i - 1, j - 1)
                    if max(max(shipMap))==0:
                        print('Вы победили!')
                        return False
                print_a(secretMap)
            elif secretMap[i - 1][j - 1] != '~':
                print('Сюда нельзя стрелять')
            elif shipMap[i - 1][j - 1] == 0:
                secretMap[i - 1][j - 1] = 'O'
                print('Не попал!')
                return True
        except:
            print('Введите корректные значения')




shipMapFirst = generate.generate()
secretMapFirst =secretField(shipMapFirst)
shipMapSecond = generate.generate()
secretMapSecond =secretField(shipMapFirst)
first=True


print('Ход первого игрока: ')
print_a(secretMapFirst)
while shot(shipMapFirst if first else shipMapSecond, secretMapFirst if first else secretMapSecond):
    if first:
        first=False
        print('Ход второго игрока')
        print_a(secretMapSecond)
    else:
        first=True
        print('Ход первого игрока: ')
        print_a(secretMapFirst)
