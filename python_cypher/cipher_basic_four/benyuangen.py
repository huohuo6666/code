#   求一个数的所有本原根

# 求最大公因子

def gcd(a,b):
    r=a%b
    while (r!=0):
        a=b
        b=r
        r=a%b
    return b

# 欧拉函数

def oula(a):
    count=0
    for i in range(1,a):
        if gcd(a,i)==1:
            count+=1
    return count


def order(b,ol,n):               #o是n的欧拉函数值，n是要求所有本原根的数
    p=1                         #排除p=0这种情况  
    while (p<=ol and (b**p%n!=1)):
        p+=1
    if p<=n and p==ol:           #保证只有在p=o时才b**pmodn=1；b 的阶 p 必须是 𝜑(𝑛)才满足本原根的条件
        return p
    else:
        return -1

# 求任意数原根
def benyuangen(n):
    o=oula(n)
    print(f'{n}的欧拉函数值为{o}')
    benyuangen=[]
    for b in range(2,n):
        if gcd(b,n) ==1:  #b必须与n互素，不然阶就小于n的欧拉函数了，也就不是本原根了
            if order(b,o,n)==o:
                benyuangen.append(b)
    print(f"{n}所有本原根:",benyuangen)
    
    
if __name__ == "__main__":
    n=int(input("请输入一个数字:"))
    benyuangen(n)
    
    
    
    