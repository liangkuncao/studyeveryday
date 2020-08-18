import java.util.HashSet;
import java.util.Set;

class Solution1346Easy {
    public boolean checkIfExist(int[] arr) {
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < arr.length; i++) {
            if (seen.contains(arr[i] * 2) || (arr[i] % 2 == 0 && seen.contains(arr[i] / 2))) return true;
            seen.add(arr[i]);
        }
        return false;
    }
}