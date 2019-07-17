n = int(input())
l = list(map(int, input().split()))
b = l[::-1]
print("->".join(map(str, b)))
