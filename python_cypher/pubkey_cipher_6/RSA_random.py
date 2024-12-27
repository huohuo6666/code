# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:59:06 2024

@author: 31447
"""

from math import sqrt as sq
import random
import base64

def eg(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = eg(b % a, a)
        return gcd, y - (b // a) * x, x

def inv(a, b):
    gcd, x, y = eg(a, b)
    if gcd != 1:
        return False
    else:
        return x % b

# 判断是否为素数
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sq(n)) + 1, 2):  # 直接跳过偶数了哈哈
        if n % i == 0:
            return False
    return True

# 生成指定位数的大素数
def ge_prime(n):
    while True:
        min_value = 10 ** (n - 1)
        max_value = (10 ** n) - 1
        num = random.randint(min_value, max_value)
        if is_prime(num):
            return num

# 生成私钥
def ge_key(p1, q1):
    p = ge_prime(p1)
    q = ge_prime(q1)

    n = p * q
    n_oula = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, n_oula)
        gcd = eg(e, n_oula)[0]
        if gcd == 1:
            break

    d = inv(e, n_oula)
    return (e, n), (d, n)

# 加密
# 输出为16进制字符串或者Base64编码
def encrypt(m, p1,q1, mode="hex"):
    e, n = ge_key(p1, q1)[0]
    ciphertext = [pow(ord(ch), e, n) for ch in m]  # 密文生成
        # 转换为16进制
    hex_ciphertext = ''.join(format(ch, 'x') for ch in ciphertext)
    return hex_ciphertext
    

# 解密
# 从16进制字符串或者Base64解码为密文后，再解密
def decrypt(ciphertext, p1,q1, mode="hex"):
    d, n = ge_key(p1, q1)[1]

        # 解析16进制字符串为数字列表
    chunk_size = len(format(n, 'x'))  # 每个密文字母对应的16进制位数
    ciphertext_nums = [int(ciphertext[i:i+chunk_size], 16) for i in range(0, len(ciphertext), chunk_size)]

    # 解密
    m = [chr(pow(ch, d, n)) for ch in ciphertext_nums]
    return ''.join(m)
# 加密
# 输出为16进制字符串或者Base64编码
def encrypt_bendi(m, public_key, mode="hex"):
    e, n = public_key
    ciphertext = [pow(ord(ch), e, n) for ch in m]  # 密文生成

    if mode == "hex":
        # 转换为16进制
        hex_ciphertext = ''.join(format(ch, 'x') for ch in ciphertext)
        return hex_ciphertext
    elif mode == "base64":
        # 转换为Base64
        bytes_ciphertext = b''.join(ch.to_bytes((ch.bit_length() + 7) // 8, 'big') for ch in ciphertext)
        base64_ciphertext = base64.b64encode(bytes_ciphertext).decode('utf-8')
        return base64_ciphertext
    else:
        raise ValueError("Unsupported mode. Use 'hex' or 'base64'.")

# 解密
# 从16进制字符串或者Base64解码为密文后，再解密
def decrypt_bendi(ciphertext, private_key, mode="hex"):
    d, n = private_key

    if mode == "hex":
        # 解析16进制字符串为数字列表
        chunk_size = len(format(n, 'x'))  # 每个密文字母对应的16进制位数
        ciphertext_nums = [int(ciphertext[i:i+chunk_size], 16) for i in range(0, len(ciphertext), chunk_size)]
    elif mode == "base64":
        # 解析Base64字符串为字节，再转数字列表
        bytes_ciphertext = base64.b64decode(ciphertext)
        ciphertext_nums = []
        byte_size = (n.bit_length() + 7) // 8
        for i in range(0, len(bytes_ciphertext), byte_size):
            ciphertext_nums.append(int.from_bytes(bytes_ciphertext[i:i+byte_size], 'big'))
    else:
        raise ValueError("Unsupported mode. Use 'hex' or 'base64'.")

    # 解密
    m = [chr(pow(ch, d, n)) for ch in ciphertext_nums]
    return ''.join(m)

if __name__ == "__main__":
    m = input("请输入一个明文_eng:")
    p1, q1 = map(int, (input("请输入想生成的两个大整数素数因子的位数_num: ")).split())

    public_key, private_key = ge_key(p1, q1)
    
    print("公钥:", public_key)
    print("私钥:", private_key)

    # 加密为16进制
    ciphertext_hex = encrypt_bendi(m, public_key, mode="hex")
    print("密文(16进制):", ciphertext_hex)
    decrypted_plaintext_hex = decrypt_bendi(ciphertext_hex, private_key, mode="hex")
    print("解密后明文:", decrypted_plaintext_hex)

    # 加密为Base64
    ciphertext_base64 = encrypt_bendi(m, public_key, mode="base64")
    print("密文(Base64):", ciphertext_base64)
    decrypted_plaintext_base64 = decrypt_bendi(ciphertext_base64, private_key, mode="base64")
    print("解密后明文:", decrypted_plaintext_base64)
