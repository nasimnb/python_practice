


def top1(arr):

      result = []
      value = {}
      f_val = 0

      for i in arr:
            if i in value:
                  value[i] += 1
            else:
                  value[i] = 1
      
      f_val = max(value.values())


      for i in value.keys():
            if value[i] == f_val:
                  result.append(i)
            else:
                  continue
      
      return result


print(top1([1,1,2,2,3,4,4,5]))









