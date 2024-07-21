def tongcacuoc(num):
    return sum(i for i in range(1, num) if num % i == 0)
N = int(input("Nhap so N la : "))
print(f"Cac cap so amicable tu 1 den {N} la :")
for a in range (1, N+1):
    b = tongcacuoc(a)
    if a < b <= N and tongcacuoc(b) == a:
        print(f"({a}, {b})")
