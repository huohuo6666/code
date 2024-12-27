def char_ord(n):
    n_list=[]
    for i in n:
        number=ord(i)-ord('a')
        n_list.append(number)
    return n_list

def ord_char(n):
    n_list=[]
    for i in n:
        number=chr(ord('a')+i)
        n_list.append(number)
    return ''.join(n_list)

        