class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = tank = total_gas = 0
        for i in range(len(gas)):
            net = gas[i] - cost[i]
            tank += net
            total_gas += net
            if tank < 0:
                start = i + 1
                tank = 0
        if total_gas < 0:
            return -1
        return start
