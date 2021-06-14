n = list(map(int, input().split()))
max = n[0]
for i in n:
    if i > max:
        max = i
    else:continue
print(max)