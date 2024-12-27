def extended_gcd(a, b):
    """扩展欧几里得算法，返回 (gcd, x, y)，使得 a*x + b*y = gcd"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def chinese_remainder_theorem(a, m):
    """
    使用中国剩余定理求解同余方程组
    a: 余数列表 [a1, a2, ..., ak]
    m: 模数列表 [m1, m2, ..., mk]
    返回 x，使得 x ≡ ai (mod mi) 对每个 i 成立
    """
    # 计算所有模数的乘积 M
    M = 1
    for mi in m:
        M *= mi
    
    # 计算每个 xi
    x = 0
    for ai, mi in zip(a, m):
        Mi = M // mi  # M / mi
        # 使用扩展欧几里得算法计算 Mi 的模逆
        gcd, inverse, _ = extended_gcd(Mi, mi)
        
        # 如果 gcd != 1，则不存在解
        if gcd != 1:
            raise ValueError(f"模 {mi} 和 {Mi} 不是互质的，无法求解")
        
        # 计算当前项的贡献
        x += ai * inverse * Mi
    
    # 返回 x mod M
    return x % M

# 示例：求解以下同余方程组
# x ≡ 2 (mod 3)
# x ≡ 3 (mod 5)
# x ≡ 1 (mod 7)

a = [2, 3, 1]
m = [3, 5, 7]

x = chinese_remainder_theorem(a, m)

print(f"解为: {x}")
                              