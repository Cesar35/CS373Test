#!/usr/bin/env python

#question 1
def f () :
    print "f1",
    yield f()
    print "f2",

def fq():
  print "m1",
  x = f()
  print "m2",
  y = x.next()
  print "m3",
  z = y.next()
  print "m4"
  
  
#question 2
def listq1():
  t = [1, 2, 3]
  for a in t:
    a = [1, 1]
  print t
  
#question 2
def listq2():
  t = [[1], [2], [3]]
  for a in range(len(t)) :
      t[a] = [1, 1]
  print t

#question 3
def listq3():
  t = [[1], [2], [3]]
  for a in range(len(t)) :
      t[a] = [1, 1]
  print t
  
print "answer #1 = ",
fq()
print "answer #2 = ",
listq1()
print "answer #3 = ",
listq2()
print "answer #4 = ",
listq3()
