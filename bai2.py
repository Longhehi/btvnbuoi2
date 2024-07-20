def sum_of_digits():
    n = int(input("Nhap mot so nguyen duong: "))
    y = 0

    for i in range(1, n + 1):
        if n % i == 0:
             y += i
    print(f"tong cac uoc so {n} la: {y}")

sum_of_digits()
