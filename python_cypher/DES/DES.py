import re

#=========
#子密钥生成
#=========

# PC1,64—>56,subkey_1

PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
        ]

#  移位次数表,subkey_2

shift_num = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# PC2,56->48,subkey_3

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
        ]

# PC1,subkey_1

def pchoice_1(bin_key):
    return [bin_key[i - 1] for i in PC_1]  

# shift_cycle,subkey_2

def shift_left(bin_key, num):
    return bin_key[num:] + bin_key[:num]

# PC2，subkey_3

def pchoice_2(bin_key):
    return ''.join([bin_key[i - 1] for i in PC_2])  # 列表转字符串

# 生成子密钥列表

def get_subkey(bin_key):
    subkey_list = []  
    # subkey_1,permutation choice，去除了八位奇偶校验位
    temp = pchoice_1(bin_key)
    # subkey_2,shift_circle，每一轮循环左移位数在表中
    for i in shift_num:
        temp[:28] = shift_left(temp[:28], i)  # C部分循环左移
        temp[28:] = shift_left(temp[28:], i)  # D部分循环左移
         # subkey_3,PC2
        subkey_list.append(pchoice_2(temp))  # 生成子密钥
    return subkey_list    # 返回子密钥列表


# ====================
# 二、des_en && des_de
# ====================

# 初始置换表

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7
      ]

# 最后一步逆置换表

INV_IP = [40, 8, 48, 16, 56, 24, 64, 32, 39,
       7, 47, 15, 55, 23, 63, 31, 38, 6,
       46, 14, 54, 22, 62, 30, 37, 5, 45,
       13, 53, 21, 61, 29, 36, 4, 44, 12,
       52, 20, 60, 28, 35, 3, 43, 11, 51,
       19, 59, 27, 34, 2, 42, 10, 50, 18,
       58, 26, 33, 1, 41, 9, 49, 17, 57, 25
       ]

# 扩展置换表E 32->48，轮函数第一步

E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1

     ]

# S盒 48->32，轮函数第三步

S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
      0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
      4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
      15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13

      ]
S2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
      3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
      0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
      13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9

      ]
S3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
      13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
      13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
      1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
      ]
S4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
      13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
      10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
      3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
      
      ]
S5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
      14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
      4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
      11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
      ]
S6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
      10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
      9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
      4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
      ]
S7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
      13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
      1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
      6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
      ]
S8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
      1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
      7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
      2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
      ]
S = [S1, S2, S3, S4, S5, S6, S7, S8]

# P盒

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25
     ]

#==========
# encrypt
#==========
#"""初始置换""" 加密第一步
def ip_change(bin_text):
    return [bin_text[i - 1] for i in IP]

# S盒替换 轮函数第三步 48->32
def s_box(bin_result):
    int_result = []
    result = ''
    for i in range(8):
        bin_row = bin_result[i][0] + bin_result[i][5] #第一位和最后一位行号
        bin_col = ''.join(bin_result[i][j] for j in range(1, 5))#中间四位列号
        int_result.append(S[i][16 * int(bin_row, 2) + int(bin_col, 2)]) #去取第几个S盒中几行几列
        result += bin(int_result[-1])[2:].zfill(4)
    return result

# P盒置换 轮函数最后一步
def p_box(result):
    
    return ''.join(result[i - 1] for i in P)

# 轮函数    加密第二步
def f(R, bin_key):
    # 1.E扩展，将R由32位扩展成48位
    R_ext = [R[i - 1] for i in E]
    # 2.与子密钥进行逐位异或
    bin_temp = [str(int(r) ^ int(k)) for r, k in zip(R_ext, bin_key)]  #返回一个包含元组的迭代器
    # 6个字符为一组，共8组
    bin_result = [''.join(bin_temp[i:i + 6]) for i in range(0, len(bin_temp), 6)]
    # 3.S盒替换 48->32
    result = s_box(bin_result)
    # 4.P盒置换 32->32
    return p_box(result)

#"""进行IP-1逆置换""" 加密第三步
def inv_ip_change(bin_text):
    return ''.join(bin_text[i - 1] for i in INV_IP)


# 书上例子,十六进制编码，十六进制转二进制
def hex_bin(hex_string):
    return ''.join(bin(int(char,16))[2:].zfill(4) for char in hex_string)
def bin_hex(bin_string):
    groups = re.findall(r'.{4}', bin_string)
    hex_string = ''.join(hex(int(group, 2))[2:] for group in groups)
    return hex_string

# utf_8编码：字符转二进制
def str_bin(text):
    return ''.join(bin(byte)[2:].zfill(8) for byte in text.encode()) #默认是使用utf_8编码的，编码成字节型数据，不够8bit往前面填充0
# utf_8解码：二进制转字符
def bin_str(bin_text):
    # 将二进制字符串按8位分割，并转换为字节数组
    byte_array = bytearray(int(i, 2) for i in re.findall(r'.{8}', bin_text) if int(i, 2) != 0)  #为什么这里要有个!=0条件
    # 将字节序列解码为字符串
    return byte_array.decode()

# 判断输入密钥位数的合法性
def is_valid_key(key):
    return len(key.encode()) == 8
# """DES加解密通用函数"""  
def des_cipher(bin_text, bin_key, reverse_keys=False):
   #=============== 
    # 初始置换IP
  #================
    bin_text = ip_change(bin_text)
    #hex_iptext=bin_hex(bin_text)
    # print(f'ip置换后{hex_iptext}')
    #=============== 
    # 16轮迭代加解密
    #================
    # 1. 分成左右两部分L、R
    L, R = bin_text[:32], bin_text[32:]
    # 2. 获得16轮子密钥
    subkey_list = get_subkey(bin_key)
    # for sub_key in subkey_list:
    #     sub=''
    #     sub_key=re.findall(r'.{4}',sub_key)
    #     for chr in sub_key:
    #         sub += format(int(chr,2),'x')
    #     print(sub)
    #     sub=''
    if reverse_keys:
        subkey_list = subkey_list[::-1]  # 解密时反转子密钥列表
    # hex_rtext=''
    # hex_ltext=''
    # count=1
    # 3. 进行16轮迭代
    for sub in subkey_list:
        R_temp = R    #用于交换变量
        # 轮函数f()结果和L进行异或
        R = ''.join(str(int(r) ^ int(l)) for r, l in zip(f(R, sub), L))
        L = R_temp
        #下面是我测试书上的例子用的
        # L=''.join(L)
        # L_1 = re.findall(r'.{4}', L)
        # R=''.join(R)
        # R_1 = re.findall(r'.{4}', R)
        # for g in R_1:
        #     hex_rtext += format(int(g, 2), 'x')
        # for g in L_1:
        #     hex_ltext += format(int(g, 2), 'x')
        # print(f'轮序{count}    L和R的值,{hex_ltext}  :  {hex_rtext}')#第十六轮的时候我没交换位置，但在输出那里我交换了
        # count+=1
        # hex_ltext=''
        # hex_rtext=''
    # 5. 进行IP-1逆置换 64->64
    return inv_ip_change(R + L)  # 抵消最后一轮互换的效果，第十六轮迭代是不互换的，输出二进制字符串



def encrypt_hex(plaintext, key):
    key=hex_bin(key)
    # 明文转成二进制字符串, 0填充至64的倍数
    bin_plaintext = hex_bin(plaintext)    
    padding_len = (64 - (len(bin_plaintext) % 64)) % 64         
    bin_padding_plaintext = bin_plaintext + '0' * padding_len   
    # 进行64位分组加密
    bin_group_64 = re.findall(r'.{64}', bin_padding_plaintext)
    bin_ciphertext = ''
    print("-----------加密--------\n")
    for g in bin_group_64:
        bin_ciphertext += des_cipher(g, key)
    # 3.密文转为16进制输出
    hex_ciphertext=bin_hex(bin_ciphertext)
    return hex_ciphertext
def decrypt_hex(hex_ciphertext, key):  
    key=hex_bin(key)
    bin_ciphertext = hex_bin(hex_ciphertext)
    # bin_ciphertext =str_bin(ciphertext)      同样理解，密文有可能utf_8编码是不可以的，因为一个字节的utf_8编码跟ascii编码一样只用7位
    # ecb模式，将明文分成64为一组进行加解密
    bin_group_64 = re.findall(r'.{64}', bin_ciphertext)
    bin_deciphertext = ''
    print("-----------解密--------\n")
    for g in bin_group_64:
        bin_deciphertext += des_cipher(g, key, reverse_keys=True)     
    # 将解密密文转为字符串输出
    # print(bin_deciphertext,type(bin_deciphertext))
    hex_plaintext=bin_hex(bin_deciphertext)
    return hex_plaintext
    # return bin_str(bin_ciphertext) 直接用utf_8解码是不可以的，因为一个字节的utf_8编码跟ascii编码一样只用7位
# 0001001000110100010101101010101111001101000100110010010100110110
# 1010101010111011000010010001100000100111001101101100110011011101

def encrypt(plaintext, key):
    if not is_valid_key(key):
        print('密钥长度错误_请输入八个字符的密钥')
        return False
    key=str_bin(key)
    #字符型明文转换和填充
    bin_plaintext = str_bin(plaintext)     #键盘上输入的字符都在utf_8编码范围内
    padding_len = (64 - (len(bin_plaintext) % 64)) % 64         
    bin_padding_plaintext = bin_plaintext + '0' * padding_len   
    # 64为一组加密
    bin_group_64 = re.findall(r'.{64}', bin_padding_plaintext)
    bin_ciphertext = ''
    for g in bin_group_64:
        bin_ciphertext += des_cipher(g, key)
    # 3.密文转为16进制输出
    hex_ciphertext=bin_hex(bin_ciphertext)
    return hex_ciphertext

def decrypt(hex_ciphertext, key):
    if not is_valid_key(key):
        print('密钥长度错误_请输入八个字符的密钥')
        return False   
    key=str_bin(key)
    # 16进制密文转为2进制字符串
    bin_ciphertext=hex_bin(hex_ciphertext)
    # bin_ciphertext =str_bin(ciphertext)      同样理解，密文有可能utf_8编码是不可以的，因为一个字节的utf_8编码跟ascii编码一样只用7位
    # ecb模式，将明文分成64为一组进行加解密
    bin_group_64 = re.findall(r'.{64}', bin_ciphertext)
    bin_deciphertext = ''
    for g in bin_group_64:
        bin_deciphertext += des_cipher(g, key, reverse_keys=True)     
    # 将解密密文转为字符串输出
    return bin_str(bin_deciphertext)

def des_initial():
    plaintext = input('请输入明文_utf_8编码:')
    key = input('请输入密钥(64bit)_utf_8编码:')
    ciphertext = encrypt(plaintext, key)       
    plaintext=decrypt(ciphertext,key)
    print(f'加密后密文:{ciphertext}\n解密后明文:{plaintext}')
    #书上例子:
    # plaintext_book='123456ABCD132536'
    # key_book='AABB09182736CCDD'
    # ciphertext_book=encrypt_hex(plaintext_book, key_book)
    # plaintext_book=decrypt_hex(ciphertext_book, key_book)
    # print(f'加密后密文:{ciphertext_book}\n解密后明文:{plaintext_book}')


if __name__ == '__main__':
    des_initial()
