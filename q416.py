class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    s = sum(nums)
    if s % 2 != 0: return False

    dp = [[False for j in range(s + 1)] for i in range(len(nums))]
    
    # return self.knapsackRecursive(nums, s // 2, 0)
    # return self.knapsackRecursiveTopDown(nums, s // 2, 0, dp)
    return self.bottomUp(nums, s // 2, dp)
    
  def knapsackRecursive(self, nums, s, index):
    if s == 0: return True
    if len(nums) == 0 or index >= len(nums): return False

    if s >= nums[index]:
      if self.knapsackRecursive(nums, s - nums[index], index + 1): return True
    
    return self.knapsackRecursive(nums, s, index + 1)
  
  def knapsackRecursiveTopDown(self, nums, s, index, dp):
    if s == 0: return 1
    if len(nums) == 0 or index >= len(nums): return 0

    if dp[index][s] == -1:
      if s >= nums[index]:
        dp[index][s] = self.knapsackRecursiveTopDown(nums, s - nums[index], index + 1, dp)
        if dp[index][s] == 1: return 1
    
    dp[index][s] = self.knapsackRecursiveTopDown(nums, s, index + 1, dp)
    
    return dp[index][s]

  def bottomUp(self, nums, sm, dp):
    if len(nums) == 0: return False
    if sm == 0: return True

    for i in range(len(nums)): dp[i][0] = True
    for s in range(0, sm + 1):
      if s == nums[0]: dp[0][s] = True
    
    for i in range(1, len(nums)):
      for s in range(1, sm + 1):
        if dp[i - 1][s] == True: dp[i][s] = dp[i - 1][s] 
        elif s >= nums[i]: dp[i][s] = dp[i - 1][s - nums[i]]

    return dp[len(nums) - 1][sm]
