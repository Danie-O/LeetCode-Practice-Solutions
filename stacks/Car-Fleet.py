class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     combined = sorted(zip(position, speed))
    #     prev_time = 0
    #     num_fleets = 0

    #     for pos, speed in combined[: : -1]:
    #         curr_time = (target - pos) / speed
    #         if curr_time > prev_time:
    #             num_fleets += 1
    #             prev_time = curr_time
    #     return num_fleets

    # using a stack
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos, speed) for pos, speed in zip(position, speed)])
        stack = []

        for pos, speed in cars[: : -1]:
            time = (target - pos) / speed
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
