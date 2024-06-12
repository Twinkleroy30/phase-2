'''Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Example 1:

Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.'''

def findNextGreaterElement(nums):
    stack=[]
    n=len(nums)
    result=[-1]*n
    for index in range(n-1,-1,-1):
        while len(stack)>0 and stack[0]<nums[index]:
            stack.pop(0)
        if len(stack)>0:
            result[index]=stack[0]
        stack.insert(0,nums[index])
    return result
nums=[12,10,4,15,9,200,121,154,12]
result=findNextGreaterElement(nums)
print(result)