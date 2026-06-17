class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        tasks_with_max_freq = sum(1 for f in freq.values() if f == max_freq)
        idle_slots = (max_freq - 1) * (n + 1) + tasks_with_max_freq
        return max(len(tasks), idle_slots)
        freq = Counter(tasks)
        max_freq = max(freq.values())
        tasks_with_max_freq = sum(1 for f in freq.values() if f == max_freq)
        idle_slots = (max_freq - 1 ) * (n + 1) + tasks_with_max_freq
        return max(len(tasks), idle_slots)
        