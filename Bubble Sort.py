def performBubbleSort(nums):
    n=len(nums)
    fixThisPosition=n-1
    while fixThisPosition>0:
        for index in range(0,fixThisPosition):
            if nums[index]>nums[index+1]:
                nums[index],nums[index+1]=nums[index+1],nums[index]
        print(nums)
        fixThisPosition-=1

nums=[9,8,7,6,5,4,3,2,1]
print("Before sorting",nums)
performBubbleSort(nums)
print("after sorting",nums)


# output
# Before sorting [9, 8, 7,6, 5, 4, 3, 2, 1]
# [8, 7.6, 5, 4, 3, 2, 1, 9]
# [7.6, 5, 4, 3, 2, 1, 8, 9]
# [5, 4, 3, 2, 1, 7.6, 8, 9]
# [4, 3, 2, 1, 5, 7.6, 8, 9]
# [3, 2, 1, 4, 5, 7.6, 8, 9]
# [2, 1, 3, 4, 5, 7.6, 8, 9]
# [1, 2, 3, 4, 5, 7.6, 8, 9]
# after sorting [1, 2, 3, 4, 5, 7.6, 8, 9]