# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:59:06 2024

@author: 31447
"""

from math import sqrt as sq
import random


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
#判断是否为素数

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sq(n)) + 1, 2):   #直接跳过偶数了哈哈
        if n % i == 0:
            return False
    return True

# 生成指定bit位数的大素数

def ge_prime(n):
    while True:
        min_value = 10 ** (n - 1)
        max_value = (10 ** n) - 1
        num=random.randint(min_value, max_value)
        if is_prime(num):
            return num

#生成私钥

def ge_key(e,p,q):
    
    # p = ge_prime(p1)
    # q = ge_prime(q1)
    # p,q=map(int,(input("请输入想生成的两个大整数素数因子的位数_dadian:")).split())

    n=p*q
    n_oula=(p-1)*(q-1)

    # while True:
    #     e= random.randint(2, n_oula)
    #     gcd=eg(e,n_oula)[0]
    #     if gcd ==1:
    #         break
    # e=13
    d = inv(e,n_oula)
    # print(d)
    # print(e)
    # print(p,q,e,d)
    return d


def encrypt(m,p,q,e):
    n=p*q
    cipher_list=pow(m,e,n)
    return cipher_list

def decrypt(c,p,q,e):
    d=ge_key(e,p,q)
    n=p*q
    m=pow(c,d,n)
    return m


if __name__ == "__main__":
    m = int(input("请输入一个明文_eng:"))
    
    p,q=map(int,(input("请输入想生成的两个大整数素数因子_num:")).split())
 
    e=int(input("请输入公钥e_num:"))
    c = encrypt(m,p,q,e)
    # print(fs.encrypt('nihao',7,3))
    m = decrypt(c,p,q,e)
    print(f'密文:{c}\n解密后的明文:{m}')
        