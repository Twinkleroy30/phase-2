def findPreviousSmallerElement(nums):
    stack = []
    n = len(nums)
    result = [-1] * n
    for index in range(n):
        while len(stack) > 0 and stack[-1] >= nums[index]:
            stack.pop()
        if len(stack) > 0:
            result[index] = stack[-1]
        stack.append(nums[index])
    return result
nums = [12, 10, 4, 15, 9, 200, 121, 154, 12]
result = findPreviousSmallerElement(nums)
print(result) 