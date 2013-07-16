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
  if len(args) == 0:
      return a
  size = min(len(temp) for temp in args)
  if size == 0 :
   return a

  else :
    i = 0
    t = 0
    while t < size:
        temp = ()
        while i < len(args) :
            temp += (args[i][t],)
            i += 1
        t += 1
        i = 0
        a.append(temp)
    return a


assert zip((), ()) == my_zip((),())
assert zip([1, 2, 3]) == my_zip([1,2,3])
assert zip((1, 2, 3), [1, 2, 3]) == my_zip((1, 2, 3), [1, 2, 3])
assert zip(()) == my_zip(())
assert zip() == my_zip()
print zip(set([1, 2, 3]))
