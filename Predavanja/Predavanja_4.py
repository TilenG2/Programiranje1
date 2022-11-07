#Spremenlivke in =
x = 7 # x kaže na škatlico 7
y = x # y kaže na isto škatlico 7

s = [1, 2, 3]
t = s
u = [1, 2, 3]

print(s, t, u)

print(s == t) # .equals() Java
print(s == u)

print(s is t) # == Java
print(s is u)

s.remove(2) #vse kar se zdodi s se tudi t
del s[:]

s = [[]] * 10
s[0].append(1)
print(s) #lol

s = [1, 2, 3]
s.append(s)

print(list(s))

def f(x, y):
    x.append(2)
    y = 4

a = []
b = 2
f(a, b)
print(a, b) # Prenosi enaki kot v Javi