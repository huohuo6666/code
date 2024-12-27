import numpy as np
from sympy import Matrix

# 检查矩阵是否可逆（模 modulus）。
def is_invertible(matrix, modulus=26):
    det = int(round(np.linalg.det(matrix)))  # 计算行列式
    gcd = np.gcd(det, modulus)  # 判断 gcd 是否为 1
    return gcd == 1

    # 计算模 modulus 下的逆矩阵。
    # 使用 sympy.Matrix 的整数逆矩阵方法。
def modular_inverse_matrix(matrix, modulus=26):

    det = int(round(np.linalg.det(matrix)))
    if np.gcd(det, modulus) != 1:
        raise ValueError("矩阵不可逆，无法进行解密！")
    adj_matrix = Matrix(matrix).adjugate()  # 求伴随矩阵
    det_inv = pow(det, -1, modulus)  # 计算行列式的模逆
    inv_matrix = (det_inv * adj_matrix) % modulus
    return np.array(inv_matrix).astype(int)

    # 对输入文本进行预处理，去掉非字母字符，转换为小写。
def preprocess_text(text):

    text = text.lower()
    return ''.join(filter(str.isalpha, text))  #或者text=re.sub(r'[^a-z],'',text)
    
    # 将文本转换为数字矩阵，按密钥阶数 n 填充。
def text_to_matrix(text, n):
    numbers = [ord(char) - ord('a') for char in text]
    while len(numbers) % n != 0:  # 填充字符
        numbers.append(ord('x') - ord('a'))
    return np.array(numbers).reshape(-1, n)

def matrix_to_text(matrix):
    """
    将数字矩阵转换为文本。
    """
    numbers = matrix.flatten()
    return ''.join(chr(num + ord('a')) for num in numbers)

def hill_encrypt(plaintext, key):
    """
    Hill 加密算法。
    """
    key=np.array(key)
    plaintext = preprocess_text(plaintext)  # 文本预处理
    n = key.shape[0]  # 获取密钥矩阵的阶数
    if key.shape[0] != key.shape[1]:
        raise ValueError("密钥矩阵必须是方阵！")
    if not is_invertible(key):
        raise ValueError("密钥矩阵不可逆，无法进行加密！")
    
    plaintext_matrix = text_to_matrix(plaintext, n)  # 转换为明文矩阵
    cipher_matrix = np.dot(plaintext_matrix, key) % 26  # 计算密文矩阵
    cipher_text = matrix_to_text(cipher_matrix)  # 转换为密文
    return cipher_text

def hill_decrypt(ciphertext, key):
    """
    Hill 解密算法。
    """
    key=np.array(key)
    n = key.shape[0]
    if key.shape[0] != key.shape[1]:
        raise ValueError("密钥矩阵必须是方阵！")
    if not is_invertible(key):
        raise ValueError("密钥矩阵不可逆，无法进行解密！")
    
    key_inv = modular_inverse_matrix(key)  # 计算模逆矩阵
    ciphertext_matrix = text_to_matrix(ciphertext, n)  # 转换为密文矩阵
    plaintext_matrix = np.dot(ciphertext_matrix, key_inv) % 26  # 计算明文矩阵
    plaintext = matrix_to_text(plaintext_matrix)  # 转换为明文
    return plaintext

if __name__ == "__main__":
    plaintext = input("请输入明文：")
    key_size = int(input("请输入密钥矩阵的阶数："))
    print("请输入密钥矩阵：")
    key = []
    for _ in range(key_size):
        row = list(map(int, input().split()))
        key.append(row)
    key = np.array(key)
    cipher_text = hill_encrypt(plaintext, key)
    print(f"加密后的密文：{cipher_text}")
    decrypted_text = hill_decrypt(cipher_text, key)
    print(f"解密后的明文：{decrypted_text}")
    # key=[[8, 6, 9, 5],
    # [6, 9 ,5, 10],
    # [5 ,8 ,4 ,9],
    # [10, 6 ,11, 4]]
    # c=hill_encrypt('HILL', key)
    # print(c)
    # m=hill_decrypt(c, key)
    # print(m)
