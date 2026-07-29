class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            count += (n >> i) & 1;
        }
        return count;
    }
}

// class Solution:
//     def hammingWeight(self, n: int) -> int:
//         count = 0
//         for i in range(32):
//             count += (n >> i) & 1
//         return count
        