class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = tank = total_gas = 0
        for i in range(n):
            net = (gas[i] - cost[i])
            tank += net
            total_gas += net
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total_gas >= 0 else -1
            