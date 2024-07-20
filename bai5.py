n = int(input("Nhap so n : "))
print(f"Cac so Armstrong bac 3 tu 1den  {n} la:")
for n in range(1, n + 1):
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(n))
    if sum_of_cubes == n:
        print(n)
