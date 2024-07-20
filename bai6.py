n = int(input("Nhập vào số n: "))
print(f"Các số hoàn hảo từ 1 đến {n} là:")
for num in range(1, n + 1):
       sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
       if sum_of_divisors == num:
        print(num)
