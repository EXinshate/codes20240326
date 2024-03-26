lst = list(map(int, input().split()))
for i in range(3):
    for j in range(3):
        print("{:4d}".format(lst[i+j*3]), end="")
    print()