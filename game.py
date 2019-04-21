import generate


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


def shot(shipMap,secretMap):
    while True:
        try:
            i,j=map(int,input('Введите координаты через пробел: ').split())
            if shipMap[i-1][j-1]==1:
                secretMap[i-1][j-1]='+'
                shipMap[i-1][j-1]=0
                print('Попал!')
                if generate.verif(i-1,j-1,shipMap)==1:
                    print('Убил!')
                    killShip(secretMap,i-1,j-1)
            elif shipMap[i-1][j-1]==0:
                secretMap[i-1][j-1]='O'
                print('Не попал!')
                return False
            else:
                print('Сюда нельзя стрелять, тут обломки разрушенного корабля')
        except:
            print('Введите корректные значения')

shipMapFirst = generate.generate()
secretMapFirst =secretField(shipMapFirst)
generate.print_a(shipMapFirst)
shot(shipMapFirst, secretMapFirst)
generate.print_a(secretMapFirst)