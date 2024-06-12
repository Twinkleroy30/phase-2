def findNextSmallestElement(nums):
    stack=[]
    n=len(nums)
    result=[-1]*n
    for index in range(n-1,-1,-1):
        while len(stack)>0 and stack[0]>=nums[index]:
            stack.pop(0)
        if len(stack)>0:
            result[index]=stack[0]
        stack.insert(0,nums[index])
    return result
nums=[12,10,4,15,9,200,121,154,12]
result=findNextSmallestElement(nums)
print(result)