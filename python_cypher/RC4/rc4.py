# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:53:03 2024

@author: lenovo
"""

def rc4_ksa(key,n=8):
    """密钥调度算法 (KSA)

    得到初始置换后的S表
    """
    # 种子密钥key若为字符串，则转成字节串
    length=2**n
    if isinstance(key, str):  
        key = key.encode()
    S = list(range(length))  # 初始化S表
    # 利用K表，对S表进行置换
    j = 0
    for i in range(length):
        j = (j + S[i] + key[i % len(key)]) % length
        S[i], S[j] = S[j], S[i]  # 置换
    return S  


def rc4_prga(S, text,n=8):
    """伪随机生成算法 (PRGA)

    利用S产生伪随机字节流,
    将伪随机字节流与明文或密文进行异或,完成加密或解密操作
    """
    # 待处理文本text若为字符串，则转成字节串
    length=2**n
    if isinstance(text, str):  
        text = text.encode()
        
    i = j = 0 
    result = []  
    
    for byte in text:
        i = (i + 1) % length
        j = (j + S[i]) % length
        S[i], S[j] = S[j], S[i]  # 置换
        t = (S[i] + S[j]) % length
        k = S[t]  # 得到密钥字k
        # 将明文或密文与k进行异或,得到处理结果
        result.append(byte ^ k)  
    return bytes(result)


def rc4_encrypt(key, text,n=8):
    """RC4加密"""
    # 将处理结果由字节串转为16进制字符串并返回
    return rc4_prga(rc4_ksa(key,n=8), text,n=8).hex()  


def rc4_decrypt(key, text,n=8):
    """RC4解密"""
    # 将处理结果由字节串转为字符串并返回
    return rc4_prga(rc4_ksa(key,n=8), bytes.fromhex(text),n=8).decode()  


def rc4_start():
    """RC4启动界面"""
    flag = True
    while flag:
        print("=" * 3, "RC4加密解密算法", "=" * 3)
        print("[1]加密")
        print("[2]解密")
        print("[0]退出")
        choice = input("请输入你的选择:")
        match choice:
            case "0":
                flag = False
            case "1":
                key = input("请输入种子密钥:")
                plaintext = input("请输入明文:")
                ciphertext = rc4_encrypt(key, plaintext,n=8)
                print("密文:", ciphertext)
            case "2":
                key = input("请输入种子密钥:")
                ciphertext = input("请输入密文:")
                plaintext = rc4_decrypt(key, ciphertext,n=8)
                print("明文:", plaintext)
            case _:
                print("输入错误，请重新输入")
    print("=" * 6, "退出成功", "=" * 6)


if __name__ == '__main__':
    rc4_start()