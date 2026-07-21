class Solution(object):
    def twoSum(self, nums, target): #function likhna
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}#kali dictionary(isme mai hum valu dale gee)
        for i in range(len(nums)):
            complement = target - nums[i]#ek hi loop ek num pe khade hoo kar socho (agar nums =[2,7,11,15]hai aur target = 9 hai , aur hume i =0 pe hai num [0]=2 to joo complement = 9 - 2 =7) {matlab = muje 7 chiye taa ki array m,ai 2+7 = 9 bane }
            if complement in seen:
                return [seen[complement], i]#chack karne ke liye humne if statement kaa use kiya ki kya yee complement pele dekha tha
            seen[nums[i]] = i
