n=int(input("Nhap day fibonacci :"))
s0 = 0
s1 = 1
Fibonacci =[s0,s1]
for i in range(2,n):
   tong = s0 + s1
   Fibonacci.append(tong)
   s0 = s1
   s1 = tong
print("day so do la:",n,f"day can tim  : {Fibonacci}")

