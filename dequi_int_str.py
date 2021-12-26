# %%
#  dùng recursion để biến 1 biến int thành str
#  mà không dùng str() 

def de_qui(n):
    # N == 0
    if n == 0:
        return '0'
    # chia lay du
    du = n % 10
    # chia lay phan nguyen
    phan_nguyen = n // 10
    # 48 la 0 trong bang ASCCI
    # du = 3 thi du + 48 = 51
    # chr(51)  thi no cho ky tu 3
    chuoi = chr(du + 48)    
    if phan_nguyen == 0:
        if n < 10:
            return chuoi
    return de_qui(phan_nguyen) + chuoi

kiem_tra = de_qui(65654646546)
print(type(kiem_tra))
print(kiem_tra)




