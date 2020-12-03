class BFS:
    def __init__(self, n):
        self.N = n
        self.G = [[False for x in range(self.N)] for y in range(self.N)]
        self.Acc = [False] * self.N
        self.Q = []
        self.setupGraph()

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

    def BFS_(self, start, g):
        print("---------- The BFS, as follows --------------------")
        addToQu = " "
        self.Q.append(start)
        self.Acc[start] = True
        print("The content of the queue as follows:")
        print(f"[{self.retCity(self.Q[-1])}]\n")

        while self.Q:
            at = self.Q.pop(0)
            if g == at:
                print(f"\nThe goal (  {self.retCity(g)}  )has been reached\n\n")
                return

            print(f"\n-->At  {self.retCity(at)}  city now")
            addToQu = self.retCity(at) + " has not been the goal,children ["

            for i in range(self.N):
                if self.G[at][i] and not self.Acc[i]:
                    self.Q.append(i)
                    addToQu += self.retCity(i) + " "
                    self.Acc[i] = True

            addToQu += "]'v been added to the queue"
            print(addToQu)

            print("The Queue: [(Front)", end="")
            for i in self.Q:
                print(f"..{self.retCity(i)}", end="")
            print("]")

        print(
            f"Finished with the BFS from start node {start}, without reaching the goal"
        )
        return

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

    schBFS = BFS(10)
    print("\n\nChoose a city to start with(its number): \n")
    for i in range(10):
        print(f"{schBFS.retCity(i)} city[ {i} ]")
    cityChoice = int(input("\nInput: "))
    print("\nChoose a city to be the goal(its number): ")
    goal = int(input("\nInput: "))

    if cityChoice < 0 or cityChoice >= 10:
        print("Mistake,run the program again")
        return
    schBFS.BFS_(cityChoice, goal)


if __name__ == "__main__":
    main()