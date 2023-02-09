##
#  Implement multiset operations using dictionaries.
#

def main() :
   a = {"A" : 3, "B" : 5}
   b = {"B" : 3, "C" : 1}

   print("a is", a)
   print("b is", b)
   print("The union of a and b is", union(a, b))
   print("The intersection of a and b is", intersection(a, b))
   print("The difference of a and b is", difference(a, b))

## Perform a multiset union.
#  @param s the first multiset
#  @param t the second multiset
#  @return the multiset union of s and t
def union(s, t) :
   retval = dict(s)
   for k in t :
      if k in retval :
         retval[k] = retval[k] + t[k]
      else :
         retval[k] = t[k]

   return retval   

## Perform a multiset intersection.
#  @param s the first multiset
#  @param t the second multiset
#  @return the multiset intersection of s and t
def intersection(s, t) :
   retval = {}
   for k in list(s.keys()) + list(t.keys()) :
      if k in s and k in t :
         retval[k] = min(s[k], t[k])

   return retval

## Perform a multiset difference.
#  @param s the first multiset
#  @param t the second multiset
#  @return the multiset difference of s and t
def difference(s, t) :
   retval = {}
   for k in s :
      if k in t and s[k] > t[k] :
         retval[k] = s[k] - t[k]
      elif k not in t :
         retval[k] = s[k]

   return retval

# Call the main function.
main()

