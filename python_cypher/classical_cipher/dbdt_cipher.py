# 使用密钥的单表代替算法 p47


def encrypt(m,key):
    key_list = []
    cipher_list = []
    key = key.lower()
    m = m.lower()
    for i in key:
        if i not in key_list:
            key_list.append(i)
    for i in range(26):
        if chr(i + ord("a")) not in key_list:
            key_list.append(chr(i + ord("a")))
    for i in m:
        cipher_list.append(key_list[(ord(i)-ord("a"))])
    return ''.join(cipher_list)
def decrypt(c,key):
    key_list = []
    m_list = []
    key = key.lower()
    c=c.lower()
    for i in key:
        if i not in key_list:
            key_list.append(i)
    for i in range(26):
        if chr(i + ord("a")) not in key_list:
            key_list.append(chr(i + ord("a")))
    for i in c:
        num=key_list.index(i)
        m_list.append(chr(num+ord('a')))
    return ''.join(m_list)
        
if __name__ == "__main__":
    m = input("请输入明文_eng:")
    key = input("please input a word key:")
    print(f'密文:{encrypt(m,key)}')
    print(f'明文{decrypt(encrypt(m,key),key)}')
