import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
		int[] answer = new int[commands.length];
		
		for (int i = 0; i < commands.length; i++) {
			int[] pic = new int[commands[i][1] - commands[i][0] + 1];
			for (int n = 0, j = commands[i][0]-1; j < commands[i][1]; j++, n++) {
				pic[n] = array[j];
			}
			Arrays.sort(pic);		
			answer[i] = pic[commands[i][2]-1];
		}
		return answer;
	}
}