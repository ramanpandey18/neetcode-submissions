class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}

// class Solution {
//     public boolean hasDuplicate(int[] nums) {
//         Map<Integer, Integer> seen = new HashMap<>();
//         for (int i = 0; i < nums.length; i++) {
//             if (seen.containsKey(nums[i])) {
//                 return true;
//             }
//             seen.put(nums[i], i);
//         }
//         return false;
//     }
// }

