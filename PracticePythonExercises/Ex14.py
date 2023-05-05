def remove_duplicates(a):
    return list(set(a))

def remove_duplicates1(a):
    return [a[i] for i in range(0, len(a)) if (a[i] not in a[0:i])]

a = [10,10,10,10,10]

print(remove_duplicates(a))
print(remove_duplicates1(a))
