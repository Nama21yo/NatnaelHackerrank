class Solution:
  def findRLEArray(self, encoded1: list[list[int]],
                   encoded2: list[list[int]]) -> list[list[int]]:
    prodNums = []

    l = 0
    r = 0

    while l < len(encoded1) and r < len(encoded2):
      multiple = encoded1[l][0] * encoded2[r][0]
      minFreq = min(encoded1[l][1], encoded2[r][1])
      if prodNums and multiple == prodNums[-1][0]:
            prodNums[-1][1] += minFreq
      else:
         prodNums.append([multiple, minFreq])
      encoded1[l][1] -= minFreq
      encoded2[r][1] -= minFreq
      if encoded1[l][1] == 0:
        l += 1
      if encoded2[r][1] == 0:
        r += 1
    return prodNums

t1 = Solution()
print(t1.findRLEArray([[1,3],[2,3]], [[6,3], [3,3]]))
print(t1.findRLEArray([[1,3],[2,1], [3,2]], [[2,3], [3,3]]))
