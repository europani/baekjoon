import java.util.*;
import java.io.*;

class Main {
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<Integer>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String type = st.nextToken();

            if (type.equals("push")) {
                stack.push(Integer.parseInt(st.nextToken()));
            } else if (type.equals("pop")) {
                System.out.println((stack.isEmpty())? -1 : stack.pop());
            } else if (type.equals("size")) {
                System.out.println(stack.size());
            } else if (type.equals("empty")) {
                System.out.println((stack.isEmpty())? 1 : 0);
            } else {
                System.out.println((stack.isEmpty())? -1 : stack.peek());
            }
        }
    }
}