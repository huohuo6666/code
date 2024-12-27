# 扩展欧几里得算法

def exgcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = exgcd(b % a, a)
        return gcd, y - (b // a) * x, x

# 求逆元

def inv(a, b):
    gcd,x, y = exgcd(a, b)
    if gcd != 1:
        return False  
    else:
        return x % b  


if __name__ == "__main__":
    a,b = map(int,input("请输入两个数：").split())
    gcd, x, y = exgcd(a, b)
    if gcd==1:
        print(f"逆元是{inv(a,b)}")
    else :print(f"最大公因子是{gcd}")