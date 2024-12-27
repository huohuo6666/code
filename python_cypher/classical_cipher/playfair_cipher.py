
import numpy as np
import re


class playfair:
    def __init__(self):
        self.flag_list = []   #用于填充字符后还原原明文
    
    #创建密钥矩阵5*5

    def create_key(self,key):
        key=key.lower()
        key=re.sub(r'[^a-z]','',key)    #利用正则表达式剔除不属于英文字母的其他字符，例如空格
        key_list=[]
        for i in key:
            if i=='j':
                i='i'         #i/j为同一个字母
            if i in key_list:
                continue #避免字符重复
            key_list.append(i)
        for i in range(26):         #把26个字母中剩余的加进来
            number=chr(i+ord('a'))
            if number=='j':number='i'
            if number in key_list: continue
            key_list.append(number)
        key_mar=np.array(key_list).reshape((5,5)) #转换为二维数组，resize**

        return key_mar

    #加密

    def encrypt(self,m,key):
        key_mar=self.create_key(key)
        m=m.lower()
        m=re.sub(r'[^a-z]','',m)         #去除非英文字符
        if len(m)%2 != 0:               #不是字符长度不是偶数，则自动在后面补齐一个z
            m = ''.join([m,'z'])
            self.flag_list.append(-1)
        m_list=[]
        for i in range(0,len(m),2):   #如果有两个同样的字符两在一块则在中间加一个z
            m1,m2=m[i:i+2]
            if m1==m2:
                m_list.append(m1)
                m_list.append('z')
                m_list.append(m2)
                self.flag_list.append(i+1)
                continue
            m_list.append(m1)
            m_list.append(m2)
        m=''.join(m_list)
        if len(m)%2 != 0:               #填充完后字符长度不是偶数，则自动在后面补齐一个z
            m = ''.join([m,'z'])
            self.flag_list.append(-2)
        
        cipher_list=[]
        #遍历明文，两两分组找出横纵坐标
        for i in range(0,len(m),2):
            m1,m2=m[i:i+2]
            if m1=='j': m1='i'
            if m2 == 'j': m2='i'
            for j in range(5):   #找出两个字符的横纵坐标
                for k in range(5):
                    if key_mar[j][k] ==m1:
                        row1,col1=j,k
                    if key_mar[j][k]==m2:
                        row2,col2=j,k
            #开始真正加密
            if row1==row2:
                c1,c2=key_mar[row1][(col1+1)%5],key_mar[row2][(col2+1)%5] #同行
            if col1==col2:
                c1,c2=key_mar[(row1+1)%5][col1],key_mar[(row2+1)%5][col2] #同列
            if row1!=row2 and col1!=col2: 
                c1,c2=key_mar[row1][col2],key_mar[row2][col1] #不同行不同列
            cipher_list.append(c1)
            cipher_list.append(c2)
        return ''.join(cipher_list)
        
    #解密
    
    def decrypt(self,c,key):
        key_mar=self.create_key(key)
        m_list=[]
        #遍历密文，两两分组找出横纵坐标
        for i in range(0,len(c),2):
            c1,c2=c[i:i+2]
            for j in range(5):
                for k in range(5):
                    if key_mar[j][k] ==c1:
                        row1,col1=j,k
                    if key_mar[j][k]==c2:
                        row2,col2=j,k
            if row1==row2:m1,m2=key_mar[row1][(col1-1)%5],key_mar[row2][(col2-1)%5]
            if col1==col2:m1,m2=key_mar[(row1-1)%5][col1],key_mar[(row2-1)%5][col2]
            if row1!=row2 and col1!=col2:m1,m2=key_mar[row1][col2],key_mar[row2][col1]
            m_list.append(m1)
            m_list.append(m2)
           
        #剔除为了加密而填充的字符
        for i in self.flag_list:
            if i<0:
                self.flag_list[self.flag_list.index(i)]=i%len(m_list)
                continue
        self.flag_list.sort(reverse=True)
                
        for i in self.flag_list:        
            m_list.pop(i)
        return ''.join(m_list)
    

if __name__=="__main__":
    m=input("请输入长度为偶数的明文，不然我们就要在后面加一个字符z喽_eng:")
    key=input("请输入密钥_eng:")
    x=playfair()
    cipher_list=x.encrypt(m, key)
    print(f'密文：{cipher_list}')
    m=x.decrypt(cipher_list,key)
    print(f'明文：{m}')
    
    
    
    
    
    
    
    
    
    