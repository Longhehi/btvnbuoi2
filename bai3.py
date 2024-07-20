n = int(input("Nhap n: "))
z = 0
for i in range(1, 2 * n + 2):
    if i % 2 == 0:
        z -= i
    else:
        z += i
print("tong_s1:", z)



n = int(input(" nhap n:"))
x = 0
for i in range(1, n+1):
    x += 1/i
print("tong _s2:", x)
