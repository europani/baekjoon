import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, Integer> map = new HashMap();
        
        for (String num : phone_book) {
            map.put(num, 0);
        }
        
        for (String num : phone_book) {
            String tmp = "";
            for (int i=0; i < num.length()-1; i++) {
                tmp+=num.charAt(i);

                if (map.containsKey(tmp)) {
                    return false;
                }
            }
        }
        
        
        return true;
    }
}