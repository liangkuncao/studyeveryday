import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution0763PartionLabelsMedium {
    public List<Integer> partitionLabels(String S) {
        Map<Character, Integer[]> letters = new HashMap<>();
        for (int i = 0; i < S.length(); i++) {
            if (letters.get(S.charAt(i)) == null) {
                letters.put(S.charAt(i), new Integer[]{i, i});
            } else {
                letters.get(S.charAt(i))[1] = i;
            }
        }
        List<Integer> res = new ArrayList<>();
        int start = -1, end = -1;
        for (int i = 0; i < S.length(); i++) {
            char ch = S.charAt(i);
            if (start == -1 && end == -1) {
                start = i;
                end = letters.get(ch)[1];
            }
            if (i < end && letters.get(ch)[1] > end) {
                end = letters.get(ch)[1];
            }
            if (i == end) {
                res.add(end - start + 1);
                start = -1;
                end = -1;
            }
        }
        return res;
    }
}
