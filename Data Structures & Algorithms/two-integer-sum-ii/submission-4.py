class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        p1 = 0
        p2 = n-1

        while p1 <= p2:
            sum = numbers[p1] + numbers[p2]
            if sum == target:
                return [p1+1, p2+1]
            elif sum < target:
                p1 += 1
            else:
                p2 -= 1
        