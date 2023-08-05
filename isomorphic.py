


def is_isomorphic(s,t):
      
      if len(s) != len(t):
            return False
      
      dict_val={}
      set_val=set()

      for i in range(len(s)):
            if s[i] not in dict_val:
                  if t[i] in set_val:
                        return False
                  dict_val[s[i]]=t[i]
                  set_val.add(t[i])
            else:
                  if dict_val[s[i]] != t[i]:
                         return  False

      return True


print(is_isomorphic("foo","bee"))




















