class TRA:
    N = None
    G = []
    currpos = None
    c = [
        "0- Buraydah",
        "1- Unayzah",
        "2- Alzulfi",
        "3- Albadai",
        "4- Riyadh-Alkhabra",
        "5- Alrass",
        "6- Um Sedrah",
        "7- Shakra",
        "8- Albukayriah",
        "9- Sheehyah",
        "10- Dhalfa",
        "11- Mulaida",
    ]

    def __init__(self, size, loc):
        self.N = size
        self.currpos = loc
        self.setupgraph()
        print("---Traverse---")

    def setupgraph(self):
        self.G = {x: [] for x in self.c}
        self.G[self.c[0]].append(self.c[1])
        self.G[self.c[0]].append(self.c[4])
        self.G[self.c[0]].append(self.c[8])
        self.G[self.c[1]].append(self.c[0])
        self.G[self.c[1]].append(self.c[2])
        self.G[self.c[1]].append(self.c[3])
        self.G[self.c[2]].append(self.c[1])
        self.G[self.c[2]].append(self.c[6])
        self.G[self.c[3]].append(self.c[1])
        self.G[self.c[3]].append(self.c[4])
        self.G[self.c[3]].append(self.c[5])
        self.G[self.c[4]].append(self.c[0])
        self.G[self.c[4]].append(self.c[3])
        self.G[self.c[5]].append(self.c[3])
        self.G[self.c[6]].append(self.c[2])
        self.G[self.c[6]].append(self.c[7])
        self.G[self.c[7]].append(self.c[6])
        self.G[self.c[8]].append(self.c[0])
        self.G[self.c[8]].append(self.c[9])
        self.G[self.c[9]].append(self.c[8])
        self.G[self.c[9]].append(self.c[10])
        self.G[self.c[10]].append(self.c[9])
        self.G[self.c[10]].append(self.c[11])
        self.G[self.c[11]].append(self.c[10])

    def tra(self):
        print("Current loc is " + self.c[self.currpos])
        ch = int(
            input(
                "Moving to the next destination: \n..[0] manually\n..[1] First In First Out (FIFO)\n..[2] Last In First Out (LIFO)]\n..[-1] Stop"
            )
        )
        while ch != -1:
            if ch == 0:
                l = {}
                for i in range(self.currpos, self.N):
                    if self.c[i] in self.G[self.c[self.currpos]]:
                        l[i] = self.c[i]

                if not l:
                    print("Done")
                    break
                print("Choose one of the following connected cities: ")
                print(l)
                ch = int(input())
                self.currpos = ch
            elif ch == 1:
                addtoq = "[(Front) "
                q = []
                for i in range(self.currpos, self.N):
                    if self.c[i] in self.G[self.c[self.currpos]]:
                        q.append(i)
                        addtoq += self.c[i] + "\t"
                if not q:
                    print("Done")
                    break
                addtoq += "]"
                print(addtoq)
                print(self.c[q[0]] + " is the destination")
                self.currpos = q[0]
            elif ch == 2:
                addtosta = "["
                sta = []
                for i in range(self.currpos, self.N):
                    if self.c[i] in self.G[self.c[self.currpos]]:
                        sta.append(i)
                        addtosta += self.c[i] + "\t"
                if not sta:
                    print("Done")
                    break
                addtosta += "top=>]"
                print(addtosta)
                self.currpos = sta[-1]
            else:
                print("Done")
                break

            ch = int(
                input(
                    "Moving to the next destination: \n..[0] manually\n..[1] First In First Out (FIFO)\n..[2] Last In First Out (LIFO)]\n..[-1] Stop"
                )
            )


print("Choose a city number to start with: ")
for _ in TRA.c:
    print(_)

citychoice = int(input())
tragraph = TRA(12, citychoice)
tragraph.tra()
