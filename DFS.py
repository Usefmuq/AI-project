class DFS:
    def __init__(self, n):
        self.N = n
        self.G = [[False] * self.N] * self.N
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
        self.G[0][1] = self.G[1][0] = True
        self.G[0][8] = self.G[8][0] = True
        self.G[0][4] = self.G[4][0] = True
        self.G[1][2] = self.G[2][1] = True
        self.G[1][3] = self.G[3][1] = True
        self.G[2][6] = self.G[6][2] = True
        self.G[3][4] = self.G[4][3] = True
        self.G[3][5] = self.G[5][3] = True
        self.G[6][7] = self.G[7][6] = True
        self.G[8][9] = self.G[9][8] = True
        self.G[9][10] = self.G[10][9] = True
        self.G[10][11] = self.G[11][10] = True

    def retCity(self, i):
        if i == 0:
            return "Buraydah"
        elif i == 1:
            return "Unayzah"
        elif i == 2:
            return "AlZulfi"
        elif i == 3:
            return "Al-Badai"
        elif i == 4:
            return "Riyadh-Alkhabra"
        elif i == 5:
            return "AlRass"
        elif i == 6:
            return "UmSedrah"
        elif i == 7:
            return "Shakra"
        elif i == 8:
            return "Al-Bukayriyah"
        elif i == 9:
            return "Sheehyah"
        elif i == 10:
            return "Dhalfa"
        else:
            return "Mulida"


def main():
    ob = DFS(12)
    print("\n\nChoose a city to start with(its number): \n")
    for i in range(12):
        print(f"{ob.retCity(i)} city[{i}]")
    cityChoice = int(input("\nInput: "))
    print("\nChoose a city to be the goal(its number): ")
    goal = int(input("\nInput: "))

    if cityChoice < 0 or cityChoice >= 12:
        print("Mistake,run the program again")
        return

    ob.DFS_(cityChoice, goal)


if __name__ == "__main__":
    main()
