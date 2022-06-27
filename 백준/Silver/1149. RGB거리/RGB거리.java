import java.util.*;
import java.io.*;

class Main {

    static int N;
    static int INF = 1_000_001;
    static int[][] graph;

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        graph = new int[N][3];
        for (int i=0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[i][0] = r;
            graph[i][1] = g;
            graph[i][2] = b;
        }
    }
  
    public static void main(String[] args) throws IOException {
        input();

        for (int i=1; i <N; i++) {
            graph[i][0] += Math.min(graph[i-1][1], graph[i-1][2]);
            graph[i][1] += Math.min(graph[i-1][0], graph[i-1][2]);
            graph[i][2] += Math.min(graph[i-1][0], graph[i-1][1]);
        }

        int result = INF;
        for (int x : graph[N-1]) {
           result = Math.min(x, result);
        }
      
        System.out.println(result);
    }
}