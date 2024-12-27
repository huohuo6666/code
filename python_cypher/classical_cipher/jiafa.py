


def encrypt(m,key):
    cipher_list = []  
    for i in m :
        if 'a'<=i<='z':
            num = ord(i)-ord('a')+key
            num = num%26
            cipher_list.append(chr(num+ord('a')))
        elif 'A'<=i<='Z':
            num = ord(i)-ord('A')+key
            num = num%26
            cipher_list.append(chr(num+ord('A')))
        else : cipher_list.append(i)
    return ''.join(cipher_list)



def decrypt(c,key):
    m_list = []
    for i in c:
        if 'a'<=i<='z':
            num = ord(i)-ord('a')-key
            num %= 26
            m_list.append(chr(num+ord('a')))
        elif 'A'<=i<='Z':
            num = ord(i)-ord('A')-key
            num %= 26
            m_list.append(chr(num+ord('A')))
        else :  m_list.append(i)
            
    return ''.join(m_list)




if __name__ == "__main__":
    m = input("请输入一个明文_eng:")
    key = int(input("请输入数字密钥:"))
    cipher_list = encrypt(m,key)
    print(f'密文:{cipher_list}')
    m_list = decrypt(cipher_list,key)
    print(f'明文:{m_list}')