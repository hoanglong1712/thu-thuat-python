# %%
# - Tính tổng mảng 2 chiều 
# - Tính tích mảng 2 chiều  
#- Tìm giá trị lớn nhất  
#- Tìm giá trị nhỏ nhất

def tong(mang):
    gia_tri = 0
    for hang in mang:
        for so in hang:
            gia_tri += so
            pass
        pass
    return gia_tri

def tich(mang):
    gia_tri = 1
    for hang in mang:
        for so in hang:
            gia_tri *= so
            pass
        pass
    return gia_tri

def sol_lon_nhat(mang):
    gia_tri = mang[0][0]
    for hang in mang:
        for so in hang:
            if gia_tri < so:
                gia_tri = so
                pass
            pass
        pass
    return gia_tri

def sol_nho_nhat(mang):
    gia_tri = mang[0][0]
    for hang in mang:
        for so in hang:
            if gia_tri > so:
                gia_tri = so
                pass
            pass
        pass
    return gia_tri

mot_mang = [[ 1, 2 ,3 ,4 ,5] , [ 4 ,5 ,6 ,7, 8] ]


# %%
print(mot_mang)

# %%
print(tich(mot_mang))
print(tong(mot_mang))
print(sol_lon_nhat(mot_mang))
print(sol_nho_nhat(mot_mang))


