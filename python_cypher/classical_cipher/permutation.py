import re


def encrypt(plain_text, key):
    # 确定密钥的长度
    plain_text.lower()
    plain_text=re.sub(r'[^a-z]','',plain_text)
    key_length = len(key)
    
    # 计算每行的字符数，分组数等
    # 补齐明文，不足的字符用填充字符（如 'z'）补充
    num_columns = key_length
    num_rows = (len(plain_text) + num_columns - 1) // num_columns  # 计算行数，需要向上取整
    padded_text = plain_text.ljust(num_rows * num_columns, 'z')  # 用 'z' 填充不足的字符
    
    # 创建一个矩阵来存储分组后的字符
    matrix = [list(padded_text[i:i+num_columns]) for i in range(0, len(padded_text), num_columns)]
    
    # 创建一个字典来确定密钥的排序顺序
    key_order = sorted([(char, idx) for idx, char in enumerate(key)], key=lambda x: x[0])
    # 提取排序后的索引
    sorted_key_indexes = [idx for char, idx in key_order]
    
    # 根据排序后的密钥列顺序构建密文
    cipher_text = ''.join(''.join(matrix[row][col] for row in range(num_rows)) for col in sorted_key_indexes)
    
    return cipher_text
def decrypt(cipher_text, key):
    # 获取密钥长度
    cipher_text.lower()
    cipher_text=re.sub(r'[^a-z]','',cipher_text)
    key_length = len(key)
    
    # 计算每行和每列的数目
    num_columns = key_length
    num_rows = len(cipher_text) // num_columns  # 行数等于密文长度除以密钥长度
    
    # 创建一个矩阵来恢复分组后的字符
    # 通过列优先的方式将密文填充回矩阵中
    matrix = [[''] * num_columns for _ in range(num_rows)]
    
    # 创建一个字典来确定密钥的排序顺序
    key_order = sorted([(char, idx) for idx, char in enumerate(key)], key=lambda x: x[0])
    # 获取排序后的密钥的索引
    sorted_key_indexes = [idx for char, idx in key_order]
    
    # 按照解密过程的顺序将密文填入矩阵
    cipher_index = 0
    for col in sorted_key_indexes:
        for row in range(num_rows):
            matrix[row][col] = cipher_text[cipher_index]
            cipher_index += 1
    
    # 按照行优先的顺序拼接字符来恢复明文
    decrypted_text = ''.join(''.join(matrix[row]) for row in range(num_rows))
    
    # 去除填充字符（如果有的话）
    return decrypted_text.rstrip('z')



if __name__=="__main__":
    plain_text = "cryptography is an applied science"
    key = "encry"
    cipher_text = encrypt(plain_text, key)
    print(f"密文: {cipher_text}")
    decrypted_text = decrypt(cipher_text, key)
    print(f"解密后的明文: {decrypted_text}")
