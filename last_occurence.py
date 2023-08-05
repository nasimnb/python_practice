



def last_occurence(array, element):

      low, high = 0, len(array) - 1
      
      while low <= high:
            mid=(low + high) // 2
            
            if (array[mid] == element and mid == len(array)-1) or \
                  (array[mid +1] > element and array[mid] == element):
                  return mid
            elif array[mid] <= element:
                  low = mid + 1
                 
            else:
                  high = mid - 1

print(last_occurence([2,2,3,4,4,4,5,5,6],4))