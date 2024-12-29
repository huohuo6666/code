from python_cypher.classical_cipher import jiafa,Vigenere,hill_password
from python_cypher.classical_cipher import permutation
from python_cypher.classical_cipher.playfair_cipher import playfair
pfa=playfair()
from python_cypher.classical_cipher.fs_cipher import fangshe as fs
fs=fs()
from python_cypher.classical_cipher import dbdt_cipher as db
from python_cypher.DES import DES as des
from python_cypher.pubkey_cipher_6 import RSA
from python_cypher.AES.AES import aes_alg as aa
a_instance=aa()
from python_cypher.RC4 import rc4
from python_cypher.SM4 import SM4
from python_cypher.SHA1 import sha1
from python_cypher.ELGMAN.elgman import Web
x=Web()
from python_cypher.pubkey_cipher_6 import RSA as rl
from python_cypher.pubkey_cipher_6 import RSA_random as rr
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # 允许跨域访问

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        # 从用户网页端请求中获取 JSON 数据
        data = request.json['data']  # 用户输入的明文
        # algorithm=request.json['algorithm'] 
        # key= request.json['key'] # 用户输入的密钥
        # 根据算法确定密钥数量
        single_key_algorithms = ['AES', 'DES', 'PlayFair', '单表代替','加法密码','Vigenere','Hill','SM4','RC4','permutation']
        double_key_algorithms = ['仿射密码','Elgman','RSA_lizi'] 
        thr_key_algorithms= ['RSA']
        algorithm = request.json['algorithm']  # 算法，默认为 AES
        if algorithm in single_key_algorithms:
            key1 = request.json['key1']  # 单个密钥
        elif algorithm in double_key_algorithms:
            key1 = request.json['key1']  # 第一个密钥
            key2 = request.json['key2']  # 第二个密钥
        elif algorithm in thr_key_algorithms:
            key1 = request.json['key1']  # 第一个密钥
            key2 = request.json['key2']
            key3 = request.json['key3']
        elif algorithm=='SHA1':
            data = request.json['data']
        else:
            return jsonify({'error': 'Unsupported algorithm'}), 400
        # 根据算法调用加密函数（这里只实现了 AES)
        if algorithm == '加法密码': 
            result = jiafa.encrypt(data,key1)
        elif algorithm == '单表代替':
            result = db.encrypt(data, key1)
        elif algorithm == '仿射密码':
            result = fs.encrypt(data,key1,key2)
        elif algorithm == 'PlayFair':
            result = pfa.encrypt(data, key1)
        elif algorithm == 'Vigenere': 
            result = Vigenere.encrypt(data,key1)
        elif algorithm == 'Hill':
            result = hill_password.hill_encrypt(data, key1)
        elif algorithm == 'permutation':
            result = permutation.encrypt(data, key1)
        elif algorithm == 'DES':
            result = des.encrypt(data, key1)
        elif algorithm == 'AES':
            result = a_instance.aes_encrypt(data,key1)
        elif algorithm == 'RSA':
            result = rl.encrypt(data, key1, key2,key3) 
        elif algorithm == 'SHA1': 
            result = sha1.encrypt(data)
        elif algorithm == 'SM4': 
            result = SM4.encrypt(data,key1)
        elif algorithm == 'RC4':
            result = rc4.rc4_encrypt(key1,data)
         # 假设RSA加密函数接受三个密钥
        elif algorithm == 'Elgman': 
            result = x.encrypt_web(data,key1,key2)      
        else:
            return jsonify({'error': 'Unsupported algorithm'}), 400

        # 返回加密结果
        return jsonify({'result': result})
    except Exception as e:
        # 如果发生错误，返回错误信息
        return jsonify({'error': str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json['data']
        # key = request.json['key']
        single_key_algorithms = ['AES', 'DES', 'PlayFair', '单表代替','加法密码','Vigenere','Hill','SM4','RC4','permutation']
        double_key_algorithms = ['仿射密码','RSA_lizi']  
        thr_key_algorithms= ['RSA']
        algorithm = request.json['algorithm']
        if algorithm in single_key_algorithms:
            key1 = request.json['key1']  # 单个密钥
        elif algorithm in double_key_algorithms:
            key1 = request.json['key1']  # 第一个密钥
            key2 = request.json['key2']  # 第二个密钥
        elif algorithm in thr_key_algorithms:
            key1 = request.json['key1']  # 第一个密钥
            key2 = request.json['key2']
            key3 = request.json['key3']
        elif algorithm=='SHA1':
            data = request.json['data']
        else:
            return jsonify({'error': 'Unsupported algorithm'}), 400
        if algorithm == '加法密码': 
            result = jiafa.decrypt(data,key1)
        elif algorithm == '单表代替':
            result = db.decrypt(data, key1)
        elif algorithm == '仿射密码':
            result = fs.decrypt(data,key1,key2)
        elif algorithm == 'PlayFair':
            result = pfa.decrypt(data, key1)
        elif algorithm == 'Vigenere': 
            result = Vigenere.decrypt(data,key1)
        elif algorithm == 'Hill':
            result = hill_password.hill_decrypt(data, key1)
        elif algorithm == 'permutation':
            result = permutation.decrypt(data, key1)
        elif algorithm == 'DES':
            result = des.decrypt(data, key1)
        elif algorithm == 'AES':
            result = a_instance.aes_decrypt(data, key1)
        elif algorithm == 'RSA':
            result = rl.decrypt(data, key1, key2,key3) 
        elif algorithm == 'SHA1': 
            result = '骗你的嘻嘻，SHA1还想解密想屁吃呢哈哈……'
        elif algorithm == 'SM4': 
            result = SM4.decrypt(data,key1)
        elif algorithm == 'RC4':
            result = rc4.rc4_decrypt(key1,data)
         # 假设RSA加密函数接受三个密钥
        elif algorithm == 'Elgman': 
            result = x.decrypt_web(data,key1) 
        else:
            return jsonify({'error': 'Unsupported algorithm'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    #hill: 8,6,9,5;6,9,5,10;5,8,4,9;10,6,11,4
    # sm4:01 23 45 67 89 ab cd ef  fe dc ba 98 76 54 32 10
    # sha1:abc
    #  aes:m_list=0x3243f6a8885a308d313198a2e0370734
    #        key=0x2b7e151628aed2a6abf7158809cf4f3c