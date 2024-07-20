def sum_of_digits():
    n= int(input("Nhap mot so nguyen duong: "))
    x = 0
    while n > 0:
        digit = n % 10
        x += digit
        n = n // 10
    print(f"Tong cac chu so la: {x}")

sum_of_digits()
