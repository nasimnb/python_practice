
def search_insert(arr,val):
      high=len(arr)-1
      mid=high // 2
      low = 0

      while low <= high:
            if val > arr[mid]:
                  mid += 1
                  low = mid 
            else:
                  mid -= 1
                  high = mid
      return low


      
      
print(search_insert([1,3,5,6],3))
print(search_insert([1,3,5,6],4))
print(search_insert([1,3,5,6],7))             
print(search_insert([1,3,5,6],10))
