def busqueda_Binaria(nums: list[int], target: int):

    left, right = 0, len(nums) -1

    while left <= right:

        mid = (left + right)  // 2
        
        if nums[mid] == target:
            #print(mid)
            return mid 
        elif nums[mid] < target:
            #print(nums[mid])
            print(left)
            left = mid + 1
            print(left)
        else:
            #print(mid)
            right = mid - 1
            #print(mid)

    return -1

busqueda_Binaria(nums = [-1,0,3,5,9,12], target=9)



    