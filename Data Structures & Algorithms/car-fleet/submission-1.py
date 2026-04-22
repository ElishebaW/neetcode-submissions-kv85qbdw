class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in pairs:
            arrival_time = (target - pos) / spd

            if stack and arrival_time <= stack[-1]:
                continue

            stack.append(arrival_time)

        return len(stack)




        