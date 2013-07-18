

def f(x, y, z):
    return [x, y, x+z]

def g(x, y = 3, z = 10):
    return [y, z, x]
    
t = (5, 4)
s = set([3, 7])
r = (8)
d = {"x" : 5, "y" : 20, "z": 9}

#Which one is a valid function call
#f(t)
#f(4, t)
#f(*t, 4)
print("d. f(4, *t)")

#Which one is a valid function call
#f(t, r)
print("b. f(4, t, r)")
#f(*t, 4, r)
#f(4, *t, r)

#Which one is a valid function call
print("a. g(*t)")
#g(4, t)
#g(t, 4)
#g(*t, 4)

#Which one is a valid function call
#g(t)
#g(s)
print("c. g(*d)")
#g(*r)

#Which is not a valid function call
print("a. f(t, 4, s)")
f(4, t, 5)
f(r, *t)
f(r, t, 8)

#Which is not a valid function call
f(t, 4, ())
print("b. f(4, *t, 5)")
f(r, 4, 5)
f(r, s, 8)

#Which is not a valid function call
g(*t)
print("b. g(1, *d)")
g(*s)
g(t, s, d)

#Which is not a valid function call
g(r)
g(1, d)
g(s)
print("d. g(t, s, *d)")

def f2(x, y, *z):
    return [x, y, z]

def g2(x = 1, z = 3, *y):
    return [x, y, z]
    
#What would be output of following call
f2(s, t, *d)
[(3, 7), (5, 4), {'y': 20, 'x': 5, 'z': 9}]
[set([3,7]), (5, 4), {'y': 20, 'x': 5, 'z': 9}]
print("c. [set([3,7]), (5, 4), ('x', 'y', 'z'))]")
[set([3,7]), (5, 4), (5, 9, 20)]

#What would be output of following call
#f2(s, t, **d)
[(3, 7), (5, 4), {'y': 20, 'x': 5, 'z': 9}]
[set([3,7]), (5, 4), ('x', 'z', 'y')]
[set([3,7]), (5, 4), (5, 9, 20)]
print("d. Does not compile")

#What would be output of following call
g2(s, d)
[set([3,7]), {'y': 20, 'x': 5, 'z': 9}, 3]
print("b. [set([3, 7]), (), {'y': 20, 'x': 5, 'z': 9}]")
[(3, 7), {'y': 20, 'x': 5, 'z': 9}, ()]
[set([3,7]), 3, ('x', 'z', 'y')]

#What would be output of following call
f2(s, *d)
[set([3,7]), {'y': 20, 'x': 5, 'z': 9}, 3]
[set([3, 7]), (), {'y': 20, 'x': 5, 'z': 9}]
print("c. [(3, 7), 'z', ('x', 'y')]")
[set([3,7]), 'z', ('x', 'y')]

def f3((x, y), *z):
    return [x, y, z]

def g3(x, z, **y):
    return [x, y, z]

t = (5, 4)
l = [3, 4, 5]
s = set([3, 7])
r = (8)
d = {"a" : 5, "b" : 20, "c": 9}

#What would be output of following call   
f3(t, *l)
print("a. [5, 4, (3, 4, 5)]")
[5, 4, 3, 4, 5]
[5, 4, ([3, 4, 5],)]
[4, 5, ([3, 4, 5],)]

#What would be output of following call
f3(t, l)
[5, 4, (3, 4, 5)]
[5, 4, 3, 4, 5]
print("c. [5, 4, ([3, 4, 5],)]")
[4, 5, ([3, 4, 5],)]

#What would be output of following call   
g3(t,l, **d)
print("a. [(5, 4), {'a': 5, 'c': 9, 'b': 20}, [3, 4, 5]]")
[5, 4, {'a': 5, 'c': 9, 'b': 20}, [3, 4, 5]]
[(5, 4), {'a': 5, 'b': 20, 'c' : 9}, 3, 4, 5]
[5, 4, [3, 4, 5], {'a': 5, 'c': 9, 'b': 20}]

#What would be output of following call
g3(t, l, a = 5, b = 20)
[(5, 4), 5, 20, [3, 4, 5]]
print("b. [(5, 4), {'a': 5, 'b': 20}, [3, 4, 5]]")
[5, 4, {'a': 5, 'b': 20}, 3, 4, 5]
#Does not Compile

#Which one is valid
print("a. a, b = 2, 3")
#a, b = 2
#b = (a = 2)
#(a = b) = 2

#Which one is not valid
a, b = 2, 3
a, b = [2, 3]
print("c. (a, b) = 2")
a = b = c = 2


#What are a and b respectively after this: a, b = b, a =[d, e] = 4, 5?

print("a. a = 4, b = 5")
#a = 5, b = 4

#What are a and b respectively after this: a, b = b, a =[e, d] = 4, 5?
#a = 4, b = 5
print("b. a = 5, b = 4")



