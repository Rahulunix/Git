
n = int(input())
for i in range(n):
    for j in range(i):
        print("*",end = "")
    print()

for i in reversed(range(n)):
    for j in reversed(range(i)):
        print("*",end = "")
    print()
 
