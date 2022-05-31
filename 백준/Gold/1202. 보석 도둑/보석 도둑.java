import java.util.*;
import java.io.*;

class Main {

    static class Jewel implements Comparable<Jewel> {
        int weight;
        int value;

        public Jewel(int weight, int value) {
            this.weight=weight;
            this.value=value;
        }

        public int compareTo(Jewel j) {
            return this.weight - j.weight;
        } 
    }

    static int N, K;
    static long result;
    static Jewel[] jewels;
    static int[] bags;

    static void input() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        jewels = new Jewel[N];
        for (int i=0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            jewels[i] = new Jewel(w, v);
        }
        Arrays.sort(jewels);
      
        bags = new int[K];
        for (int i=0; i < K; i++) {
          bags[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(bags);
    }

    static void pro() {
        // Value 내림차순
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());

        int i = 0;
        for (int bag : bags) {
            while (i < N && jewels[i].weight <= bag) {
                pq.offer(jewels[i++].value);
            }
            if (!pq.isEmpty()){
                result+=pq.poll(); 
            }
        }
    }
  
    public static void main(String[] args) throws Exception {
        input();
        pro();
        System.out.println(result);
    }
}