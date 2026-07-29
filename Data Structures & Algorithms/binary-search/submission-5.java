class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        if (n == 1 && target == nums[0]) {
            return 0;
        }
        int start = 0;
        int end = n - 1;
        while (start <= end) {
            int mid = ((start + end) / 2);
            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]){
                end = mid - 1;
            } else {
                start = mid + 1;
            }

        }
        return -1;
        // n = len(nums)
        // if n == 1 and target == nums[0]:
        //     return 0
        // start = 0
        // end = n - 1
        // while start <= end:
        //     mid = (start + end) // 2
        //     if target == nums[mid]:
        //         return mid
        //     elif target < nums[mid]:
        //         end = mid - 1
        //     else:
        //         start = mid + 1
        // return -1
    }
}
