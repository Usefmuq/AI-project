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
# list = new ArrayList<Integer>();

N = 10
G = []
estCost = []
toCityCost = []
funcGCost = []
funcFCost = []
calc = []
list_ = []

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
