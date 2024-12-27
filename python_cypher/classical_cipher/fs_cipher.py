# 仿射密码p47
import re
# from  ..cipher_basic_four import exgcd as eg
# import sys 
# sys.path.append(r'D:\python_cypher\cipher_basic_four')

class fangshe:
    
    def exgcd(self,a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.exgcd(b % a, a)
            return gcd, y - (b // a) * x, x

# 求逆元
    
    def inv(self,a, b):
        gcd,x, y = self.exgcd(a, b)
        if gcd != 1:
            return False  
        else:
            return x % b  
    def encrypt(self,m,k1,k2):
        gcd = self.inv(k1,26)         #导入的exgcd模块
        if gcd  is False:
            return '请重新输入一个符合规范的k1,必须要跟26互素'
        cipher_list = []  
        for i in m :
            if 'a'<=i<='z':
                num = k1*(ord(i)-ord('a'))+k2
                num = num%26
                cipher_list.append(chr(num+ord('a')))
            elif 'A'<=i<='Z':
                num = k1*(ord(i)-ord('A'))+k2
                num = num%26
                cipher_list.append(chr(num+ord('A')))
            else : cipher_list.append(i)
        return ''.join(cipher_list)
        
    def decrypt(self,c,k1,k2):
        gcd = self.inv(k1,26)         #导入的exgcd模块
        if gcd  is False:
            return '请重新输入一个符合规范的k1,必须要跟26互素'
        m_list = []
        inv_k1 = self.inv(k1,26)
        for i in c:
            if 'a'<=i<='z':
                num = inv_k1*(ord(i)-ord('a')-k2)
                num %= 26
                m_list.append(chr(num+ord('a')))
            elif 'A'<=i<='Z':
                num = inv_k1*(ord(i)-ord('A')-k2)
                num %= 26
                m_list.append(chr(num+ord('A')))
            else : m_list.append(i)
            
           
        return ''.join(m_list)

if __name__ == "__main__":
    m = input("请输入一个明文_eng:")
    k1,k2 = map(int,input("请输入数字密钥:").split())
    x=fangshe()
    gcd = x.inv(k1,26)         #导入的exgcd模块
    if gcd  is False:
        k1=int(input("请重新输入一个符合规范的k1,必须要跟26互素:"))  #保证k1有逆元，保证能解密
    
    # m = m.lower()
    # m=re.sub(r'[^a-z]','',m)

    cipher_list = x.encrypt(m,k1,k2)
    print(f'密文:{cipher_list}')
    m_list = x.decrypt(cipher_list,k1,k2)
    print(f'明文:{m_list}')
    
    


