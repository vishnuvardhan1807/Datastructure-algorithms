names = []
occurances = {}
n = int(input())
for i in range(n):
    name = input()
    names.append(name)

for name in names:
    if name in occurances:
        occurances[name] += 1
    else:
        occurances[name] = 1

counts = []
for i in occurances.keys():
    counts.append(occurances[i])
#print(counts)

max_ = max(counts)
print(max_)

names = []
for i in occurances.keys():
    if max_ == 1:
        break
    if occurances[i] == max_:
        names.append(i)

for i in names:
    print("The names are")
    print(i)
                