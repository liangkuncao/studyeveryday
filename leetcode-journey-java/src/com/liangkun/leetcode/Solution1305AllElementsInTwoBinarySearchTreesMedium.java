import java.util.ArrayList;
import java.util.List;

public class Solution1305AllElementsInTwoBinarySearchTreesMedium {
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> list1 = helperDfs(root1);
        List<Integer> list2 = helperDfs(root2);
        List<Integer> res = new ArrayList<>();
        while (list1.size() > 0 && list2.size() > 0) {
            if (list1.get(0) <= list2.get(0)) {
                res.add(list1.remove(0));
            } else {
                res.add(list2.remove(0));
            }
        }
        if (list1.size() > 0) {
            res.addAll(list1);
        }
        if (list2.size() > 0) {
            res.addAll(list2);
        }
        return res;
    }

    private List<Integer> helperDfs(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<Integer> res = new ArrayList<>();
        res.addAll(helperDfs(root.left));
        res.add(root.val);
        res.addAll(helperDfs(root.right));
        return res;
    }
}
