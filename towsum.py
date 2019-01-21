# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
class Solution:
	def hash_method(self,nums,target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		#构造一个哈希表, key是nums, value是nums的位置(因为要返回nums的位置)
		#通过检查当前的nums和target-nums在不在哈希表里就可以判断答案
		hash = {}
		for i in range(len(nums)):
			if target - nums[i] in hash:
				return hash[target-nums[i]],i
			else:
				#当前遇到nums[i]时,我不知道target-nums[i]是否在hash里面, 所以我把nums[i]放进去, 以后朋友target-nums[i]的时候就能发现
				#target - (target-nums[i]) = nums[i]在hash里面就能判断了
				hash[nums[i]] = i
		return None
	def search_all(self,nums,target):
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i]+nums[j] == target:
					return i,j
		return None
	def twoSum(self, nums, target):
		return self.search_all(nums,target)
print(Solution().twoSum([1,2,5,6,7],7))