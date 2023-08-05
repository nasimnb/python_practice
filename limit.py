


def limit(arr,min_lim=None,max_lim=None):

      if len(arr) == 0:
            return arr
      if min_lim == None:
            min_lim=min(arr)
      if max_lim==None:
            max_lim = max(arr)

      return list(filter( lambda x:(min_lim <= x <= max_lim),arr))

print(limit([1,2,3,4,5,6],None,3))