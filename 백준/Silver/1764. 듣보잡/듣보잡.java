import java.util.*;
import java.io.*;

class Main {

    static int N, M;
    static Map<String, Boolean> people;
    static List<String> result;
  
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
      
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        people = new HashMap<>();
        result = new ArrayList<>();
        for (int i=0; i < N; i++) {
            people.put(br.readLine(), true);
        }

        for (int i=0; i < M; i++) {
            String name = br.readLine();
            if (people.containsKey(name)) {
                result.add(name);
            }
        }

        System.out.println(result.size());
        Collections.sort(result);
        for (String name : result) {
            System.out.println(name);
        }
    }
}