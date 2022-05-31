import java.util.*;
import java.io.*;

class Main {

    static HashSet<String> strs;

    static void input() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        strs = new HashSet<>();
        for (int i=0; i < n; i++) {
            strs.add(br.readLine());
        }
    }
  
    public static void main(String[] args) throws Exception {
        input();
        ArrayList<String> str_list = new ArrayList<>(strs);
      
        Collections.sort(str_list, (s1, s2) -> {
            if (s1.length() == s2.length()) {
                return s1.compareTo(s2);
            } else {
                return s1.length() - s2.length();
            }
        });

        for (String s : str_list) {
            System.out.println(s);
        }
    }
}