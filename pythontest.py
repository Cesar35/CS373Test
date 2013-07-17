#!/usr/bin/env python
#-----
#globals for questions
#-----

l = [1, 2, 3]
t = (1, 2, 3)
a = [1, 2, 3]

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
  
#question 3
def listq2():
  t = [[1], [2], [3]]
  for a in range(len(t)) :
      t[a] = [1, 1]
  print t

#question 4
def listq3():
  t = [[1], [2], [3]]
  for a in t :
      a = [1, 1]
  print t
  
#question 5
def listq4():
    l = [2, "abc", 3.45]
    print type(l)is type,
    print type(list)is list
    
def argq1(l, t, a):
    l += (5,)
    t += (5,)
    a += (5,)
    
def fancyif(n):
    return -1 if (n < 0) else (-9 if (n == 1) else (1 if(n > 0) else 0))
     
#----------
#questions
#----------
print "answer #1 = ",
fq()
print "answer #2 = ",
listq1()
print "answer #3 = ",
listq2()
print "answer #4 = ",
listq3()
print "answer #5 = ",
listq4()
print "answer #6 = ",
argq1(l, t, a[:])
print l,
print t,
print a
print "answer #7 = ",
print fancyif(-1),
print fancyif(0),
print fancyif(1)