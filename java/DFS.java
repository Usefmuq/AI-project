package java;

import java.util.Scanner;
import java.util.*;

public class DFS {
    int N; // number of vertices in the graph
    boolean[][] G; // the graph as an adjacency matrix
    // G[i][j] is true if there is an edge from i to j
    boolean[] Acc; // a nodes takes a true value when it is visited or added to the queue
    Stack<Integer> sta; // G[i][j] is true if there is an edge from i to j

    public DFS(int size) {
        N = size;
        Acc = new boolean[N]; // a visited array to mark which vertices have been visited while doing the DFS
        sta = new Stack<Integer>();
        setupGraph(size);
        System.out.println("---------- The DFS, as follows --------------------");
        System.out.println();

    }

    // perform a DFS starting at node start
    public void DFS(int start, int g) {
        int at;
        String addToSta = " ";
        sta.push(start);
        Acc[start] = true;

        System.out.print("\t\tThe stack: ");
        System.out.println("[" + retCity(sta.peek()) + "...top=>]\n");

        do {
            at = sta.pop();

            if (g == at) {
                System.out.println("\nThe goal (" + retCity(g) + ")has been reached\n\n");
                return;
            }

            System.out.println("-->At " + retCity(at) + " city now ");
            addToSta = retCity(at) + " has not been the goal,children [";

            for (int i = 0; i < N; ++i)
                if (!Acc[i] && G[at][i]) {
                    sta.push(i);
                    addToSta += retCity(i) + " ";
                    Acc[i] = true;
                }
            addToSta += "]'v been added to the stack";
            System.out.println(addToSta);

            System.out.print("The stack: [");
            for (int i : sta)
                System.out.print(retCity(i) + "..");
            System.out.println("top=>]\n");

        } while (!sta.empty());
    }

    public void setupGraph(int size) {
        // set up a graph with a number of vertices:

        G = new boolean[N][N];

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
    }

    public static void main(String[] args) {
        int cityChoice, goal;
        Scanner inp = new Scanner(System.in);
        System.out.println("\n\nChoose a city to start with(its number): \n");
        for (int i = 0; i < 10; i++)
            System.out.println(retCity(i) + " city[" + i + "]");
        System.out.print("\nInput: ");
        cityChoice = inp.nextInt();
        System.out.println("\nChoose a city to be the goal(its number): ");
        System.out.print("\nInput: ");
        goal = inp.nextInt();

        if (cityChoice < 0 || cityChoice >= 10) {
            System.out.println("Mistake,run the program again");
            System.exit(0);
        }

        DFS schDFS = new DFS(10);
        schDFS.DFS(cityChoice, goal);

    }

    public static String retCity(int i) // the function returns city name, according to its index in V array
    {
        if (i == 0)
            return "Business and Economics";
        else if (i == 1)
            return "Science";
        else if (i == 2)
            return "Engineering";
        else if (i == 3)
            return "Architecture and Planning";
        else if (i == 4)
            return "Sharia and Islamic Studies";
        else if (i == 5)
            return "Medicine";
        else if (i == 6)
            return "Qassim University Public Library";
        else if (i == 7)
            return "Department of English & Translation";
        else if (i == 8)
            return "Parking lot 1";
        else
            return "Parking lot 2";
    }
}