import java.util.*;
import java.io.*;

class Main {
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> queue = new LinkedList<Integer>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String type = st.nextToken();

            if (type.equals("push_front")) {
                queue.offerFirst(Integer.parseInt(st.nextToken()));
            } else if (type.equals("push_back")) {
                queue.offer(Integer.parseInt(st.nextToken()));
            } else if (type.equals("pop_front")) {
                sb.append((queue.isEmpty())? -1 : queue.poll()).append("\n");
            } else if (type.equals("pop_back")) {
                sb.append((queue.isEmpty())? -1 : queue.pollLast()).append("\n");
            } else if (type.equals("size")) {
                sb.append(queue.size()).append("\n");
            } else if (type.equals("empty")) {
                sb.append((queue.isEmpty())? 1 : 0).append("\n");
            } else if (type.equals("back")) {
                sb.append((queue.isEmpty())? -1 : queue.peekLast()).append("\n");
            } else {
                sb.append((queue.isEmpty())? -1 : queue.peek()).append("\n");
            }
        }
        System.out.println(sb);
    }
}