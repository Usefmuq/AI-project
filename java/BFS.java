package java;

import java.util.Queue;
import java.util.Scanner;
import java.util.LinkedList;

public class BFS {

    int N; // number of vertices in the graph
    boolean[][] G; // the graph as an adjacency matrix
    // G[i][j] is true if there is an edge from i to j

    boolean[] Acc; // a nodes takes a true value when it is visited or added to the queue
    Queue<Integer> Q;

    BFS(int size) {
        N = size;
        Acc = new boolean[N];
        Q = new LinkedList<Integer>(); // A queue to process nodes
        setupGraph(size);
        System.out.println("---------- The BFS, as follows --------------------");
        System.out.println();
    }

    void setupGraph(int size) {
        G = new boolean[N][N];
        G[0][1] = G[1][0] = true;
        G[0][8] = G[8][0] = true;
        G[0][4] = G[4][0] = true;
        G[1][2] = G[2][1] = true;
        G[1][3] = G[3][1] = true;
        G[2][6] = G[6][2] = true;
        G[3][4] = G[4][3] = true;
        G[3][5] = G[5][3] = true;
        G[6][7] = G[7][6] = true;
        G[8][9] = G[9][8] = true;
        G[9][10] = G[10][9] = true;
        G[10][11] = G[11][10] = true;
    }

    // perform a BFS starting at node start
    void BFS(int start, int g) {
        String addToQu = " ";
        // start with only the start node in the queue and mark it as visited
        Q.offer(start);
        Acc[start] = true;
        System.out.println("The content of the queue as follows:");
        System.out.print("[");
        System.out.print(retCity(Q.peek()));// shows the first element in the queue
        System.out.println("]\n");

        // continue searching the graph while still nodes in the queue
        while (!Q.isEmpty()) {
            int at = Q.poll(); // get the head of the queue
            if (g == at) {
                System.out.println("\nThe goal (" + retCity(g) + ")has been reached\n\n");
                return;
            }
            System.out.println("\n-->At " + retCity(at) + " city now");
            addToQu = retCity(at) + " has not been the goal,children [";

            // add any unseen nodes to the queue to process, then mark them as visited so
            // they don't get re-added

            for (int i = 0; i < N; ++i)
                if (G[at][i] && !Acc[i]) {
                    Q.offer(i);
                    addToQu += retCity(i) + " ";
                    Acc[i] = true;
                }

            addToQu += "]'v been added to the queue";
            System.out.println(addToQu);

            System.out.print("The Queue: [(Front)");
            for (int i : Q)
                System.out.print(".." + retCity(i));
            System.out.print("]\n");

        }

        System.out.printf("Finished with the BFS from start node %d%n, without reaching the goal", start);
        System.exit(0);
    }

    public static void main(String[] args) {
        int cityChoice, goal;
        Scanner inp = new Scanner(System.in);
        System.out.println("\n\nChoose a city to start with(its number): \n");
        for (int i = 0; i < 12; i++)
            System.out.println(retCity(i) + " city[" + i + "]");
        System.out.print("\nInput: ");
        cityChoice = inp.nextInt();
        System.out.println("\nChoose a city to be the goal(its number): ");
        System.out.print("\nInput: ");
        goal = inp.nextInt();

        if (cityChoice < 0 || cityChoice >= 12) {
            System.out.println("Mistake,run the program again");
            System.exit(0);
        }

        BFS schBFS = new BFS(12);
        schBFS.BFS(cityChoice, goal);
    }

    public static String retCity(int i) // the function returns city name, according to its index in V array
    {
        if (i == 0)
            return "Buraydah";
        else if (i == 1)
            return "Unayzah";
        else if (i == 2)
            return "AlZulfi";
        else if (i == 3)
            return "Al-Badai";
        else if (i == 4)
            return "Riyadh-Alkhabra";
        else if (i == 5)
            return "AlRass";
        else if (i == 6)
            return "UmSedrah";
        else if (i == 7)
            return "Shakra";
        else if (i == 8)
            return "Al-Bukayriyah";
        else if (i == 9)
            return "Sheehyah";
        else if (i == 10)
            return "Dhalfa";
        else
            return "Mulida";

    }
}