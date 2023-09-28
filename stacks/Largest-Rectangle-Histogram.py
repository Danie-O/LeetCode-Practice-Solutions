from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    left_smallest_index = [0] * len(heights)
    stack = []
    right_smallest_index = [0] * len(heights)

    # populate left_smallest_index
    for index in range(len(heights)):
        while stack and heights[stack[-1]] > heights[index]:
            stack.pop()
        left_smallest_index[index] = stack[-1] if stack else (index - 1)
        stack.append(index)
    print(left_smallest_index)

    # populate right_smallest_index
    stack = []
    for index in range(len(heights)):
        while stack and heights[stack[-1]] > heights[index]:
            j = stack.pop()
            right_smallest_index[j] = index
        stack.append(index)
    while stack:
        j = stack.pop()
        right_smallest_index[j] += j + 1 if j != len(heights) -1 else 0
    print(right_smallest_index)
    
    max_area = float('-inf')
    for i in range(len(heights)):
        area = (right_smallest_index[i] - left_smallest_index[i] - 1) * heights[i]
        max_area = max(max_area, area)
    print(max_area)


largestRectangleArea([2, 1, 5, 6, 2, 3])
largestRectangleArea([2, 4])
        