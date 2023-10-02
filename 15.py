N, K = map(int, input().split())
kegels = ["I"] * N

for _ in range(K):
    li, ri = map(int, input().split())
    kegels[li - 1:ri] = ["."] * (ri - li + 1)

result = "".join(kegels)
print(result)