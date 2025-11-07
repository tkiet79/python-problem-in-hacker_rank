from itertools import groupby
S = input()

# 2. Dùng groupby để duyệt qua chuỗi
#    Với "1222311", vòng lặp sẽ chạy 4 lần:
#    - Lần 1: key = '1', group = ['1']
#    - Lần 2: key = '2', group = ['2', '2', '2']
#    - Lần 3: key = '3', group = ['3']
#    - Lần 4: key = '1', group = ['1', '1']
for key, group in groupby(S):
    
    # 3. Đây là logic chính xác của bạn:
    #    Biến 'group' (iterator) thành một 'list' và lấy độ dài (len) của nó.
    X = len(list(group))
    
    # 4. In ra tuple (X, c) theo định dạng.
    #    'key' chính là ký tự c.
    #    'end=" "' để in mọi thứ trên cùng một dòng, cách nhau bằng dấu cách.
    print(f"({X}:{key})", end="\n")




