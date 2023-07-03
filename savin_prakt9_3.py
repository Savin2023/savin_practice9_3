print("Введите последовательность чисел через пробел")
m=input().split()
rez=set()
for i in range(len(m)):
    print(m[i])
    if m[i] in rez:
        print("YES")
    else:
        print("NO")
    rez.add(m[i])
