import java.util.*;

class Main {

    static int N, K;
    static ArrayList<Integer> people;
    static ArrayList<Integer> result;

    static void input() throws Exception {
        Scanner scan = new Scanner(System.in);
        N = scan.nextInt();
        K = scan.nextInt();

        result = new ArrayList<Integer>();
        people = new ArrayList<Integer>();
        for (int i = 0; i < N; i++) {
            people.add(i+1);
        }
    }
  
    public static void main(String[] args) throws Exception {
        input();
        int idx = -1;

        while (!people.isEmpty()) {
            idx=(idx+K)%people.size();
            result.add(people.remove(idx));
            idx-=1;
        }

        System.out.println(result.toString().replace("[", "<").replace("]", ">"));  
    }
}