import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int findMaximumXOR(int[] nums) {
        int res = 0;
        for (int i = 31; i > -1; i--) {
            res <<= 1;
            Set<Integer> pre = new HashSet<>();
            for (int n : nums) {
                pre.add(n >> i);
            }
            for (int p : pre) {
                if (pre.contains(res ^ 1 ^ p)) {
                    res += 1;
                    break;
                }
            }
        }
        return res;
    }
}