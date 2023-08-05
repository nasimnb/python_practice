"""
      [False, 2, 1, 0, 4, 0]  =>  [False, 2, 1, 4, 0, 0]
"""

def move_zero(seq):

      result = []
      zero = 0

      for i in seq:
            if i == 0 and type(i) != bool:
                  zero += 1