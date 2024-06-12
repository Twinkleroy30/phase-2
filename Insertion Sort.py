def performInsertionSort(nums):
    n=len(nums)
    for firstEleIndex in range(1,n):
        temp=nums[firstEleIndex]
        prevIndex=firstEleIndex-1
        while prevIndex>=0:
            if nums[prevIndex]>temp:
                nums[prevIndex+1]=nums[prevIndex]
            else:
                break
            prevIndex-=1
        nums[prevIndex+1]=temp

nums=[9,8,7,6,5,4,3,2,1]
print("Before sorting",nums)
performInsertionSort(nums)
print("after sorting",nums)