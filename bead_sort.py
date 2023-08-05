"""
      bead sort 

      [2, 5, 3, 2, 8, 6, 9] => [2, 2, 3, 5, 6, 8, 9]
      1(2,5) 2(5,3) 3(3,2)
"""

def bead_sort(s):

      if any(not isinstance(x,int) or x<0 for x in s):
            raise TypeError("sequence must be list of non-negative integer.")

      for _  in range(len(s)):
            for i, (rod_upper, rod_lower) in enumerate(zip(s,s[1:])):
                  if rod_upper > rod_lower:
                        s[i] -= rod_upper - rod_lower
                        s[i+1] += rod_upper - rod_lower

      return s


print(bead_sort([2,5,3,2,8,6,9]))























