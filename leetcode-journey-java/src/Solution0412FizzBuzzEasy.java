import java.util.ArrayList;
import java.util.List;

public class Solution0412FizzBuzzEasy {
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            res.add(Integer.toString(i));
        }
        int idx3 = 3, idx5 = 5;
        while (idx3 <= n) {
            res.set(idx3, "Fizz");
            idx3 += 3;
        }
        while (idx5 <= n) {
            if (res.get(idx5).equals("Fizz")) {
                res.set(idx5, "FizzBuzz");
            } else {
                res.set(idx5, "Buzz");
            }
            idx5 += 5;
        }
        res.remove(0);
        return res;
    }
}

