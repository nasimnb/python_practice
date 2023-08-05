
def binary_search(array,element):
      low,high=0,len(array)-1

      while low<high:
            mid=(low+high)//2

            if element == array[mid]:
                  return mid
            elif element > array[mid]:
                  low=mid+1
            else:
                  high=mid-1
      return -1

print(binary_search([1,2,3,4,5,6,7,11],7))