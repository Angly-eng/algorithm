def bubble_sort(nums):
    for i in range(len(nums)):
        flag1 = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                flag1 = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if not flag1:       #若一趟中任意两个相邻元素未发生位置交换，则可以确定剩余的元素已按升序排列
            break
    return nums


# -*- coding = utf-8 -*-
nums = [1,5,3,6,78,66,154]
# 冒泡排序
sortednums = bubble_sort(nums[:])

print(sortednums)
print(nums)
