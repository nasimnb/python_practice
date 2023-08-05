

"""
      rotate
      "hello",3  =>  "lohel"

"""

def rotate(s,k):

      if k == len(s):
            return s
      elif k > len(s):
            k = k - len(s)
      
      s=s[k:]+s[:k]
      
      return s
      

print(rotate("hello",3))
