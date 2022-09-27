def array_front9(nums):
    nine = 0
    for numberrs in nums[0:4]:
        if numberrs == 9:
            nine = nine + 1        
    if nine > 0:
        return True
    else:
        return False
