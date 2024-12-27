import math

# 判断一个数是否为素数

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

#筛法筛选一个数以内的素数，并输出他们和素数总个数

def Eratosthenes(n):
    sqrt_number = int(math.sqrt(n))+1 
    prime = [True for _ in range(n+1)]
    i = 2
    for i in range(i,sqrt_number,1):  # 从小于根号n的数开始找素数
        if is_prime(i):
            for i in range(i*2,n+1,i):
                prime[i] = False
        continue

    count = 0
    for i in range(2,n+1,1):
        if prime[i]:
            print(i,end=' ')
            count += 1
            if count%5 == 0: print()
    print(f"\n{n}以内素数总数是{count}")

if __name__ == "__main__":
    n = int(input("please input a int number:"))
    if is_prime(n):
        print(f"{n}是素数")
    else :
        print(f"{n}不是素数")
    Eratosthenes(n)   







