
"""
      search_range
      [1,2,2,8,8,8],11 => [None, None]
      [1,2,2,8,8,8],8  => [3,5]

"""


def search_range(s,n):
      
      if n not in s:
            return [None,None]
      
      m=s.count(n)-1
      
      for i in s:
            if i == n:
                  a=s.index(i)
                  break
      
      return [a, a+m]
            


print(search_range([1,2,2,8,8,8],8))

















