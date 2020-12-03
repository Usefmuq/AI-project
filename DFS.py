class DFS:
    def __init__(self, n):
        self.N = n
        self.G = [[False for x in range(self.N)] for y in range(self.N)]
        self.Acc = [False] * self.N
        self.sta = []
        self.setupGraph()
        print("---------- The DFS, as follows --------------------")

    def DFS_(self, start, g):
        at = 0
        addToSta = " "
        self.sta.append(start)
        self.Acc[start] = True
        print(f"\t\tThe stack: [{self.retCity(self.sta[-1])}...top=>]\n")

        while True:
            at = self.sta.pop(-1)
            if g == at:
                print(f"\nThe goal ( {self.retCity(g)} )has been reached\n\n")
                return

            print(f"-->At {self.retCity(at)} city now ")
            addToSta = f"{self.retCity(at)} has not been the goal,children ["

            for i in range(self.N):
                if not self.Acc[i] and self.G[at][i]:
                    self.sta.append(i)
                    addToSta += f"{self.retCity(i)} "
                    self.Acc[i] = True
            addToSta += "]'v been added to the stack"
            print(addToSta)

            print("The stack: [ ", end="")
            for i in self.sta:
                print(f"{self.retCity(i)} ..", end="")
            print("top=>]\n")
            if not self.sta:
                break

    def setupGraph(self):
        self.G[1][0] = self.G[0][1] = True
        self.G[0][5] = self.G[5][0] = True
        self.G[0][6] = self.G[6][0] = True
        self.G[1][2] = self.G[2][1] = True
        self.G[1][3] = self.G[3][1] = True
        self.G[1][6] = self.G[6][1] = True
        self.G[1][9] = self.G[9][1] = True
        self.G[2][3] = self.G[3][2] = True
        self.G[2][4] = self.G[4][2] = True
        self.G[2][6] = self.G[6][2] = True
        self.G[3][9] = self.G[9][3] = True
        self.G[4][6] = self.G[6][4] = True
        self.G[4][7] = self.G[7][4] = True
        self.G[5][6] = self.G[6][5] = True
        self.G[5][7] = self.G[7][5] = True
        self.G[6][7] = self.G[7][6] = True
        self.G[7][8] = self.G[8][7] = True

    def retCity(self, i):
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


def main():
    ob = DFS(10)
    print("\n\nChoose a city to start with(its number): \n")
    for i in range(10):
        print(f"{ob.retCity(i)} city[{i}]")
    cityChoice = int(input("\nInput: "))
    print("\nChoose a city to be the goal(its number): ")
    goal = int(input("\nInput: "))

    if cityChoice < 0 or cityChoice >= 10:
        print("Mistake,run the program again")
        return

    ob.DFS_(cityChoice, goal)


if __name__ == "__main__":
    main()
