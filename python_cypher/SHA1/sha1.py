def K_t(t):
    if 0 <= t <= 19:
        K = '5A827999'
    elif t <= 39:
        K = '6ED9EBA1'
    elif t <= 59:
        K = '8F1BBCDC'
    else:
        K = 'CA62C1D6'
        
    return int(K, 16)

def ZUO(num, k):
    num_bin = bin(num)[2:].zfill(32) 
    out = num_bin[k % len(num_bin):] + num_bin[:k % len(num_bin)] 
    return int(out, 2)

def W_S(x, t):
    # print(w[t])
    return int(w[t], 16)

def FF14(t, x, y, z):
    if 0 <= t <= 19:
        a = (int(x, 16) & int(y, 16)) | ~((int(x, 16) & int(z, 16)))
    elif t <= 39:
        a = int(x, 16) ^ int(y, 16) ^ int(z, 16)
    elif t <= 59:
        a = (int(x, 16) & int(y, 16)) | (int(x, 16) & int(z, 16)) | (int(y, 16) & int(z, 16))
    else:
        a = int(x, 16) ^ int(y, 16) ^ int(z, 16)
        
    return a

def ft(b, c, d, t):
    if t >= 0 and t <= 19:
        return ((b & c) | (~b & d))
    elif t >= 20 and t <= 39:
        return (b ^ c ^ d)
    elif t >= 40 and t <= 59:
        return ((b & c) | (b & d) | (d & c))
    elif t >= 60 and t <= 79:
        return (b ^ c ^ d)

def encrypt(zifu):
    zifu_list = []
    for i in zifu:
        zifu_list.append(str(bin(ord(i))[2:].zfill(8)))
    # print(zifu_list)

    zifu_str = ''.join(zifu_list)
    # print(zifu_str)

    len_zifu = len(zifu_str)
    # print(len_zifu)

    if len_zifu % 512 != 448:
        zifu_str += '1'
        for i in range(423):
            zifu_str += '0'
    # print(zifu_str, len(zifu_str))

    j = ''
    zifu_str_hex = ''
    for i in zifu_str:
        j += str(i)
        if len(j) == 4:
            zifu_str_hex += str(int(j, 2))
            j = ''
    # print(zifu_str_hex)

    kuai = (hex((len(zifu) * 8))[2:].zfill(16))
    # print(kuai)

    zifu_str_hex += str(kuai)
    # print(zifu_str_hex)

    w = []
    for i in range(0, 80):
        w.append(None)
    count = 0
    a = ''
    for i in zifu_str_hex:
        count += 1
        a += str(i)
        if count % 8 == 0:
            w[(count // 8) - 1] = a
            a = ''
        while count == 128:
            break

    for i in range(16, 80):
        temp = int(w[i - 3], 16) ^ int(w[i - 8], 16) ^ int(w[i - 14], 16) ^ int(w[i - 16], 16)
        w[i] = hex(ZUO(temp, 1))[2:].zfill(8)
    # print(w)
            
    A, B, C, D, E = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
    A_0, B_0, C_0, D_0, E_0 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0  

    for t in range(80):
        B_B = B
        B = A
        A = ((((E + ft(B_B, C, D, t)) % (2**32) + ZUO(A, 5)) % (2**32) + int(w[t], 16)) % (2**32) + K_t(t)) % (2**32)
        E = D
        D = C
        C = ZUO(B_B, 30)
        print(t, hex(A), hex(B), hex(C), hex(D), hex(E))

    A, B, C, D, E = (A_0 + A) % (2**32), (B_0 + B) % (2**32), (C_0 + C) % (2**32), (D_0 + D) % (2**32), (E_0 + E) % (2**32)
    cipher_text = ''
    cipher_text += hex(A)[2:]
    cipher_text += hex(B)[2:]
    cipher_text += hex(C)[2:]
    cipher_text += hex(D)[2:]
    cipher_text += hex(E)[2:]
    print(f'密文是:{cipher_text}')
    return cipher_text
    # print('密文是:', hex(A)[2:], hex(B)[2:], hex(C)[2:], hex(D)[2:], hex(E)[2:])

if __name__ == "__main__":
    zifu = input("请输入你想加密的数据:")
    c=encrypt(zifu)