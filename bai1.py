def sum_of_digits():
    n= int(input("Nhap mot so nguyen duong: "))
    x = 0
    while n > 0:
        digit = n % 10
        x += digit
        n = n // 10
    print(f"Tong cac chu so la: {x}")

sum_of_digits()


def sum_of_digits():
    n = int(input("Nhap mot so nguyen duong: "))
    y = 0

    for i in range(1, n + 1):
        if n % i == 0:
             y += i
    print(f"tong cac uoc so {n} la: {y}")

sum_of_digits()


def triangle():
 a = int(input("Nhap canh thu nhat: "))
 b = int(input("Nhap canh thu hai: "))
 c = int(input("nhap canh thu ba: "))
 if a+b>c and a+c>b and b+c>a:
     print("Ba canh nay tao thanh mot tam giac ")
     if a == b == c:
         print("Ba canh nay tao thanh mot tac giac deu ")
     elif a==b or a==c or c==b:
             print("Ba canh nay tao thanh mot tam giac can")
     elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
        print("Day la tam giac vuong ")
     else:
         print("Day la tam giac thuong")
 else:
     print("ba canh tren khong the tao thanh mot tam giac")
triangle()
