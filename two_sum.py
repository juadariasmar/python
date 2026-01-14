def two_sum_brute_force(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
            
    return []

print(two_sum_brute_force([2,7,11,15], 9))


def two_sum_hash_map(nums, target):

    hashmap = {}

    for i in range(len(nums)):

        complement = target - nums[i]

        if complement in hashmap:
            
            return [hashmap[complement], i]
        
        hashmap[nums[i]] = i

    return []

print(two_sum_hash_map([2,7,11,15], 9))