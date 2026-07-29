class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int xor = 0;

        for (int i = 0; i <= n; i++) {
            xor ^= i;
        }

        for (int num : nums) {
            xor ^= num;
        }
        return xor;
    }
}
        // n = len(nums)
        // xor = 0
        
        // # XOR all numbers from 0 to n
        // for i in range(n + 1):
        //     xor ^= i
        
        // # XOR with all array elements
        // for num in nums:
        //     xor ^= num
        
        // return xor