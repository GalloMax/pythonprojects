import random

a = []
for i in range(1, random.randint(2, 10)):
    a.append(random.randint(1, 10))

b = []
for i in range(1, random.randint(2, 10)):
    b.append(random.randint(1, 10))

print(sorted(a))
print(sorted(b))
print(sorted(set([aa for aa in a if (aa in b)])))
