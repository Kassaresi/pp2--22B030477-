n = int(input())
list = list(map(int,input().strip().split()))[:n]
h = []
i = 0
while i < n:
    if list[i] >= 0:
        h.append(list[i])
    i += 1
h.sort()
j = 0
k = 0
answer = []
while k < n:
    if list[k] >= 0:
        answer.append(h[j])
        j += 1
    else:
        answer.append(list[k])
    k += 1
print(answer)