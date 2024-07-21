N = int(input("Nhập vào số N: "))
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
print(f"Tam giác Pascal có {N} hàng:")
for i in range(N):
    row = [binomial_coefficient(i, k) for k in range(i + 1)]
    print(" ".join(map(str, row)))
