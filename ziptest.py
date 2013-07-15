#!/usr/bin/env python


#-----------
#zip testing
#-----------

assert(zip([1,2,3]) == [(1,),(2,),(3,)])
assert(zip([],[], []) == [])
assert(zip([1,2,3], [1,2,3]) == [(1,1), (2,2), (3,3)])
assert(zip(zip([1, 2, 3]), [0, 0 ,0]) == [((1,), 0),((2,), 0), ((3,), 0)])

#print zip(1, 2, 3) doesnt work but be things of iterable
#print  zip((1,2),[3], [4, 4], (4,4,4,4))



def my_zip (*args):
  a = []
  size = min(len(temp) for temp in args)
  if size == 0 :
   return a

  elif len(args) == 1 : 
    for it in args:
      for tup in it:
        a.append((tup, ))
      return a
  else :
    temp = () 
    for it in args:
      for tup in it:
        temp += (tup,)
        break
      a.append(temp)
    return a
  
print my_zip((), ())
print my_zip([1,2,3])
print my_zip([1,2,3], [1,2,3])

