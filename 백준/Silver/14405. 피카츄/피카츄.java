import java.util.*;
import java.io.*;

class Main {
  
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();

        str = str.replaceAll("pi|ka|chu", "");
        if (str.length()==0) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}