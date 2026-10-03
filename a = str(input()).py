a = str(input())
slov = []

while len(a)>1:
    slov.append(a[:1])
    a = a[1:]

slov.append(a)

count = {}

for i in slov:
    count[i] = count.get(i, 0) + 1

print(count)