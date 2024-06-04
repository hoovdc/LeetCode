class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create the for loop to run for x cycles where x is length of input list
        for list_position in range(len(nums)):
            #create a for loop to cycle through each value in the list following 
            #the index value from the parent for loop
            for second_val in range(list_position+1,len(nums)):
                if nums[list_position] + nums[second_val] == target:
                    return [list_position, second_val]

#create an instance of the class
mySolutionInstance = Solution()

#Call a moethod of the instance.  
#maybe unneeded because twoSum method seems to performing the inputting and outputting
#mySolutionInstance.twoSum([2,7,11,15], target = 9)