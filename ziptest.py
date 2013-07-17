#!/usr/bin/env python



def Zip(*a1):

  iters = [iter(it) for it in a1]
  res = []
  while iters:
      lt = iters[0]
      for i in iters:
        elem = i
        res.append(i)
  yield res
  
def ziptest(a, b):
  tmp = Zip(a, b)
  tmp = Zip()
  for it in tmp:
    print(it)
    
ziptest([1, 2, 3, 4, 5], [4, 5, 6])
print(zip([1, 2, 3], [1, 2, 3], [1, 2]))
