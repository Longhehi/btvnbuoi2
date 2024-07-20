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
