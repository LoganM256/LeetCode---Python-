class Solution():
    def twoSum(self, nums, target):
        hashmap = {} #creates an empty dictionary (hashmap)
        for i in range(len(nums)): #creates a list from 0 to the length of the list nums with i as the iteration var
            complement = target - nums[i] #complement var set to target val minus the value in the list at the index of i
            if complement in hashmap: #if the complement is a key in the hashmap
                return [i, hashmap[complement]] #return the index of the both numbers in the list
            hashmap[nums[i]] = i #if it's not in the hashmap as a key, then add the value in the list as the key and the iteration variable as the value. so example would be ["6":0]

answer = Solution()

numbers = [16,5,36,7,3]
targetnum = 43

printable = answer.twoSum(numbers,targetnum)

print(printable)