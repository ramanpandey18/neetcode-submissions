class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequency of each task
        freq = Counter(tasks)
        print(f"Frequencies: {dict(freq)}")

        # Step 2: Find the maximum frequency
        max_freq = max(freq.values())
        print(f"Max frequency: {max_freq}")

        # Step 3: Count how many tasks share the max frequency
        tasks_with_max_freq = sum(1 for f in freq.values() if f == max_freq)
        print(f"Tasks with max frequency: {tasks_with_max_freq}")

        # Step 4: Apply the formula
        # (max_freq - 1) gaps, each of size (n + 1), plus the final max-freq tasks
        idle_slots = (max_freq - 1) * (n + 1) + tasks_with_max_freq
        print(f"Idle slots formula result: {idle_slots}")
        print(f"Total tasks: {len(tasks)}")

        # Step 5: Return whichever is larger
        return max(len(tasks), idle_slots)
        