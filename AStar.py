# N = 13;
# G = new boolean[N][N];
# setupGraph();
# estCost = new int[N];
# setupEstCost();
# toCityCost = new int[N][N]; // cost among cities
# btwCities();
# funcGCost = new int[N]; // The cost so far to reach a city
# funcFCost = new int[N]; // The estimated total cost through a city to the goal
# calc = new boolean[N];
# list_ = new Arraylist_<Integer>();

N = 10
G = [[0] * 10] * 10
estCost = [0] * 10
toCityCost = [[0] * 10] * 10
funcGCost = [0] * 10
funcFCost = [0] * 10
calc = [0] * 10
list_ = []


def hFunc(i):
    return estCost[i]


def retFCost(city):
    return funcFCost[city]


def btwCost(first, second):
    return toCityCost[first][second]


def retGCost(city):
    return funcGCost[city]


def compTwoCities(from_, to):
    newR = retGCost(from_) + btwCost(from_, to) + hFunc(to)
    if newR < funcFCost[to]:
        funcFCost[to] = newR


def assignFCost(city):
    global funcFCost
    funcFCost[city] = retGCost(city) + hFunc(city)


def assignGCost(from_, to):
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
    print("The current location: " + retCity(Loc))
    print(f"F(n):{retFCost(Loc)}= G({retGCost(Loc)}) + H({hFunc(Loc)})\n")

    if Loc == 2:
        print("now in Bucharest, The goal has been reached")
        return 1

    for i in range(N):
        if G[Loc][i] == True and list_.contains(i):
            compTwoCities(Loc, i)
        elif G[Loc][i] == True:
            list_.append(i)
            assignGCost(Loc, i)
            assignFCost(i)

    list_.remove(Loc)

    print("---------------Expansion--------------")
    for i in list_:
        print(
            "|"
            + retCity(i)
            + " F(n): "
            + retFCost(i)
            + " = G("
            + retGCost(i)
            + ") + H("
            + hFunc(i)
            + ")|"
        )

    print("----------------------------------------\n\n")

    dest = list_[0]

    for i in list_.size():
        if retFCost(list_[i]) < retFCost(dest):
            dest = list_[i]
    AStar(dest)


def setupGraph():
    G[0][1] = G[1][0] = True
    G[0][3] = G[3][0] = True
    G[1][5] = G[5][1] = True
    G[1][7] = G[7][1] = True
    G[2][8] = G[8][2] = True
    G[2][5] = G[5][2] = True
    G[3][4] = G[4][3] = True
    G[4][6] = G[6][4] = True
    G[5][7] = G[7][5] = True
    G[6][10] = G[10][6] = True
    G[7][9] = G[9][7] = True
    G[8][9] = G[9][8] = True
    G[9][10] = G[10][9] = True
    G[9][12] = G[12][9] = True
    G[10][11] = G[11][10] = True
    G[11][12] = G[12][11] = True


def setupEstCost():
    estCost[0] = 242
    estCost[1] = 160
    estCost[2] = 0
    estCost[3] = 241
    estCost[4] = 244
    estCost[5] = 98
    estCost[6] = 329
    estCost[7] = 193
    estCost[8] = 178
    estCost[9] = 253
    estCost[10] = 366
    estCost[11] = 374
    estCost[12] = 380


def btwCities():
    toCityCost[0][1] = toCityCost[1][0] = 120
    toCityCost[0][3] = toCityCost[3][0] = 75
    toCityCost[1][5] = toCityCost[5][1] = 138
    toCityCost[1][7] = toCityCost[7][1] = 146
    toCityCost[2][8] = toCityCost[8][2] = 211
    toCityCost[2][5] = toCityCost[5][2] = 101
    toCityCost[3][4] = toCityCost[4][3] = 70
    toCityCost[4][6] = toCityCost[6][4] = 111
    toCityCost[5][7] = toCityCost[7][5] = 97
    toCityCost[6][10] = toCityCost[10][6] = 118
    toCityCost[7][9] = toCityCost[9][7] = 80
    toCityCost[8][9] = toCityCost[9][8] = 99
    toCityCost[9][10] = toCityCost[10][9] = 140
    toCityCost[9][12] = toCityCost[12][9] = 151
    toCityCost[10][11] = toCityCost[11][10] = 75
    toCityCost[11][12] = toCityCost[12][11] = 71


def main():
    print("------------")
    start = int(input("enter the start"))
    funcGCost[start] = 0
    assignFCost(start)
    calc[start] = True
    # list_.append(10)
    list_.append(start)
    AStar(start)
    print("\n\n")


if __name__ == "__main__":
    main()
