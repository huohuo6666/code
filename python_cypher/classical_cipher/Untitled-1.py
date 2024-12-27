def weijiniya_decode(ciphertext,key):
    ciphertext,alphabet = ciphertext.lower(),[chr(i+ord('a')) for i in range(26)]
    # while True:
    #     key = input('请输入秘钥:\n').lower()
    #     if key.isalpha():break
    #     else:print('秘钥错误，请重输')
    key = [key[i%len(key)] for i in range(len(ciphertext))]
    i,j,text,dic = 0,0,'',{chr(i+ord('a')):i for i in range(26)}
    while j < len(ciphertext):
        if ciphertext[j] in dic:text += alphabet[(dic[ciphertext[j]] - dic[key[i]]) % 26];i += 1
        else: text += ciphertext[j]
        j += 1
    return text
    return plain_text

m=weijiniya_decode('Y2w9Iobe_v_Ufbm0ajI05bfzvTP1b_c}{lr','responsibility')
print(m)
responsibility
H2s9Qznr_d_Met    b0sq    K05kbh   gFc1j_  u}{kj
HgsyQznr_d_Met