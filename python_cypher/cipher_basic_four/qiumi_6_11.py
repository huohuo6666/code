def mod_exp(base, exp, mod):
    result = 1
    base = base % mod  # 先对 base 取模，防止 base 初始值过大
    while exp > 0:
        # 如果 exp 是奇数
        if exp % 2 == 1:
            result = (result * base) % mod
        # exp 翻半，base 翻倍
        exp = exp // 2
        base = (base * base) % mod
    return result

# 计算 16^15 mod 4731
base = 16
exp = 15
mod = 4731

result = mod_exp(base, exp, mod)

# 输出结果
print(result)
