import java.util.*;

class Solution {
    class Music implements Comparable<Music> {
        int id;
        String genre;
        int plays;

        Music(int id, String genre, int plays) {
            this.id=id;
            this.genre=genre;
            this.plays=plays;
          }

        public int compareTo(Music m) {
            return Integer.compare(m.plays, this.plays);
        }
    }

    public int[] solution(String[] genres, int[] plays) {
        // 1. 장르순 정렬
        Map<String, Integer> countMap = new HashMap<>();
        for (int i=0; i < genres.length; i++) {
            countMap.put(genres[i], countMap.getOrDefault(genres[i], 0)+plays[i]);
        }

        ArrayList<String> genre = new ArrayList<>();
        for (String key : countMap.keySet()) {
            genre.add(key);
        }
        Collections.sort(genre, (o1, o2) -> countMap.get(o2) - countMap.get(o1));


        // 2. 장르 내 재생횟수 정렬
        List<Music> music = new ArrayList<Music>();
        for (int i=0; i < genres.length; i++) {
            music.add(new Music(i, genres[i], plays[i]));
        }
    
        Collections.sort(music);
        
        ArrayList<Integer> result = new ArrayList<>();
        for (String g : genre) {
            int cnt = 0;
            for (int i=0; i < genres.length; i++) {
                if (g.equals(music.get(i).genre)) {
                    result.add(music.get(i).id);
                    cnt++;
                }
                
                if (cnt >= 2) break;
            }
        }
       
        
        int[] res_arr = new int[result.size()];
        
        for (int i=0; i < result.size(); i++) {
            res_arr[i]=result.get(i);
        }

        return res_arr;
    }
}