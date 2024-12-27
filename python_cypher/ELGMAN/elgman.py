

import random
from sympy import isprime, mod_inverse



#为了适配网页的
class Web:
#========================================================================
# 实现的是书上的第一个例子
#========================================================================
    def __init__(self, p=2579, g=2):  # 提供默认值
        self.p = p
        self.g = g
    def generate_keys_web(self, x):
        # 公钥
        y = pow(self.g, x, self.p)
        return y

    def encrypt_web(self, data, x,k):
        y = self.generate_keys_web(x)
        a = pow(self.g, k, self.p)
        b = (pow(y, k,self.p) * data) % self.p
        return a, b

    def decrypt_web(self, ciphertext, x):
        a, b = ciphertext
        s = pow(a, x, self.p)
        plaintext = (b * mod_inverse(s, self.p)) % self.p
        return plaintext
    



#这是小皮同学的
def generate_keys(p, g):
    # 私钥
    x = random.randint(1, p - 2)
    # 公钥
    y = pow(g, x, p)
    return (p, g, y), x

def encrypt(public_key, plaintext):
    p, g, y = public_key
    k = random.randint(1, p - 2)    
    a = pow(g, k, p)
    b = (pow(y, k, p) * plaintext) % p
    return a, b

def decrypt(private_key, ciphertext, p):
    a, b = ciphertext
    x = private_key
    s = pow(a, x, p)
    plaintext = (b * mod_inverse(s, p)) % p
    return plaintext


# 示例使用
if __name__ == "__main__":
    #选择一个大素数p和一个生成元g
    p = 2579
    g = 2

    # 生成公钥和私钥
    public_key, private_key = generate_keys(p, g)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # 加密
    plaintext = 123  # 明文
    ciphertext = encrypt(public_key, plaintext)
    print("Ciphertext:", ciphertext)

    # 解密
    decrypted_text = decrypt(private_key, ciphertext, p)
    print("Decrypted Text:", decrypted_text)
    # shili=Web()
    # c=shili.encrypt_web(1299, 765, 853)
    # print(c)
    # m=shili.decrypt_wb(c, 765)
    # print(m)