import java.util.ArrayList;
import java.util.List;

public class Solution0967Medium {
    public int[] numsSameConsecDiff(int N, int K) {
        List<Integer> res = new ArrayList<>();
        if (N == 1) {
            res.add(0);
        }
        for (int i = 1; i < 10; i++) {
            dfs(res, N - 1, K, i);
        }
        return res.stream().mapToInt(i -> i).toArray();
    }

    private void dfs(List<Integer> res, int N, int K, int num) {
        if (N == 0) {
            res.add(num);
            return;
        };
        int last_digit = num % 10;
        if (last_digit + K >= 0 && last_digit + K <= 9) {
            dfs(res, N - 1, K, num * 10 + last_digit + K);
        }
        if (last_digit - K != last_digit + K && last_digit - K >= 0 && last_digit - K <= 9) {
            dfs(res, N - 1, K, num * 10 + last_digit - K);
        }
    }
}
