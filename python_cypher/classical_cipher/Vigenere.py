import re


#Vigenere密码

#加密

def encrypt(m,key):
    m=m.lower()
    m=re.sub(r'[^a-z]','',m)
    key=key.lower()
    key=re.sub(r'[^a-z]','',key)
    cipher_list=[]
    flag=0
    for i in m:
        cipher=(ord(i)-ord('a')+(ord(key[flag%len(key)])-ord('a')))%26
        cipher=chr(cipher+ord('a'))
        cipher_list.append(cipher)
        flag+=1
    return ''.join(cipher_list)

#解密

def decrypt(c,key):
    key=key.lower()
    key=re.sub(r'[^a-z]','',key)
    m_list=[]
    flag=0
    for i in c:
        m=(ord(i)-ord('a')-(ord(key[flag%len(key)])-ord('a')))%26
        m=chr(m+ord('a'))
        m_list.append(m)
        flag+=1
    return ''.join(m_list)    
    
    
if __name__=="__main__":
    # m=input("请输入明文_eng:")
    key=input("请输入密钥_eng:")
    # cipher_list=encrypt(m,key)
    cipher_list=input("请输入明文_eng:")
    print(f'密文：{cipher_list}')
    m_list=decrypt(cipher_list,key)
    print(f'明文：{m_list}')
    
    
    
    
    
    
    


    
