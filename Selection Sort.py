def performSelectionSort(nums):
    n=len(nums)
    fixThisPosition=n-1
    while fixThisPosition>0:
        maxEleIndex=fixThisPosition
        for index in range(0,fixThisPosition-1):
            if nums[maxEleIndex]>nums[index]:
                maxEleIndex=index
        if maxEleIndex!=fixThisPosition:
            temp=nums[maxEleIndex]
            nums[maxEleIndex]=nums[fixThisPosition]
            nums[fixThisPosition]=temp
        fixThisPosition-=1

nums=[9,8,7,6,5,4,3,2,1]
print("Before sorting",nums)
performSelectionSort(nums)
print("after sorting",nums)