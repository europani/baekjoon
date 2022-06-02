import java.io.*;

class Main {
    
    static int result;

    static int check(String word) {
        boolean[] alpha = new boolean[26];
        char prev = word.charAt(0);
        for (int i=0; i < word.length(); i++) {
            char letter = word.charAt(i);

            if (prev!=letter && alpha[letter-'a']) return 0;
            
            alpha[letter-'a']=true;
            prev = letter;
        }
        return 1;
    }
  
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i=0; i<N; i++) {
            String word = br.readLine();
            result+=check(word);
        }
        System.out.println(result);
    }
}