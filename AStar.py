N = 10
G = [[0] * 10] * 10
estCost = [0] * 10
toCityCost = [[0] * 10] * 10
funcGCost = [0] * 10
funcFCost = [0] * 10
calc = [0] * 10
list_ = []


def hFunc(i):
    global estCost
    return estCost[i]


def retFCost(city):
    global funcFCost
    return funcFCost[city]


def btwCost(first, second):
    global toCityCost
    return toCityCost[first][second]


def retGCost(city):
    global funcGCost
    return funcGCost[city]


def compTwoCities(from_, to):
    global funcFCost
    newR = retGCost(from_) + btwCost(from_, to) + hFunc(to)
    if newR < funcFCost[to]:
        funcFCost[to] = newR


def assignFCost(city):
    global funcFCost
    funcFCost[city] = retGCost(city) + hFunc(city)


def assignGCost(from_, to):
    global funcGCost
    funcGCost[to] = retGCost(from_) + btwCost(from_, to)


def retCity(i):
    if i == 0:
        return "Business and Economics"
    elif i == 1:
        return "Science"
    elif i == 2:
        return "Engineering"
    elif i == 3:
        return "Architecture and Planning"
    elif i == 4:
        return "Sharia and Islamic Studies"
    elif i == 5:
        return "Medicine"
    elif i == 6:
        return "Qassim University Public Library"
    elif i == 7:
        return "Department of English & Translation"
    elif i == 8:
        return "Parking lot 1"
    else:
        return "Parking lot 2"


def AStar(Loc):
    global N, G, estCost, toCityCost, funcFCost, funcGCost, calc, list_
    print("The current location: " + retCity(Loc))
    print(f"F(n):{retFCost(Loc)}= G({retGCost(Loc)}) + H({hFunc(Loc)})\n")

    if Loc == 3:
        print(f"now in {retCity(Loc)}, The goal has been reached")
        return 1
    for i in range(N):
        if G[Loc][i] == True and i in list_:
            compTwoCities(Loc, i)
        elif G[Loc][i] == True:
            list_.append(i)
            assignGCost(Loc, i)
            assignFCost(i)

    list_.remove(Loc)

    print("---------------Expansion--------------")
    for i in list_:
        print(f"|{retCity(i)} F(n): {retFCost(i)}= G({retGCost(i)}) + H({hFunc(i)})|")

    print("----------------------------------------\n\n")

    dest = list_[0]

    for i in range(len(list_)):
        if retFCost(list_[i]) < retFCost(dest):
            dest = list_[i]
    AStar(dest)


def setupGraph():
    global G
    G[0][1] = G[1][0] = True
    G[0][5] = G[5][0] = True
    G[0][6] = G[6][0] = True
    G[1][2] = G[2][1] = True
    G[1][3] = G[3][1] = True
    G[1][6] = G[6][1] = True
    G[1][9] = G[9][1] = True
    G[2][3] = G[3][2] = True
    G[2][4] = G[4][2] = True
    G[2][6] = G[6][2] = True
    G[3][9] = G[9][3] = True
    G[4][6] = G[6][4] = True
    G[4][7] = G[7][4] = True
    G[5][6] = G[6][5] = True
    G[5][7] = G[7][5] = True
    G[6][7] = G[7][6] = True
    G[7][8] = G[8][7] = True


def setupEstCost():
    global estCost
    estCost[0] = 266
    estCost[1] = 154
    estCost[2] = 35
    estCost[3] = 0
    estCost[4] = 214
    estCost[5] = 408
    estCost[6] = 212
    estCost[7] = 306
    estCost[8] = 496
    estCost[9] = 244


def btwCities():
    global toCityCost
    toCityCost[0][1] = toCityCost[1][0] = 232
    toCityCost[0][5] = toCityCost[5][0] = 200
    toCityCost[0][6] = toCityCost[6][0] = 188
    toCityCost[1][2] = toCityCost[2][1] = 150
    toCityCost[1][3] = toCityCost[3][1] = 154
    toCityCost[1][6] = toCityCost[6][1] = 160
    toCityCost[1][9] = toCityCost[9][1] = 196
    toCityCost[2][3] = toCityCost[3][2] = 35
    toCityCost[2][4] = toCityCost[4][2] = 182
    toCityCost[2][6] = toCityCost[6][2] = 184
    toCityCost[3][9] = toCityCost[9][3] = 244
    toCityCost[4][6] = toCityCost[6][4] = 201
    toCityCost[4][7] = toCityCost[7][4] = 146
    toCityCost[5][6] = toCityCost[6][5] = 194
    toCityCost[5][7] = toCityCost[7][5] = 170
    toCityCost[6][7] = toCityCost[7][6] = 157
    toCityCost[7][8] = toCityCost[8][7] = 235


def main():
    global N, G, estCost, toCityCost, funcFCost, funcGCost, calc, list_
    setupGraph()
    setupEstCost()
    btwCities()

    print("------------")
    start = int(input("enter the start : "))
    funcGCost[start] = 0
    assignFCost(start)
    calc[start] = True
    list_.append(start)
    AStar(start)
    print("\n\n")


if __name__ == "__main__":
    main()
