
"""
      linear search 
      [2,4,5,6,11,34,5],11  => 4
"""

def linear_search(array,element):
      for i in range(len(array)):
            if array[i] == element:
                  return i
      return -1

print(linear_search([2,4,5,6,11,34,5],11))