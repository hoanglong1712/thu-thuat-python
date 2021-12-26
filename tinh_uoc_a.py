# %%
def tinh_tong(bat_dau, khac_biet, ket_thuc):
    ket_qua = 0
    gia_tri = bat_dau

    while gia_tri <= ket_thuc:        
           
        ket_qua += 1 / gia_tri  
        gia_tri += khac_biet
        pass
    return ket_qua

print(tinh_tong(2, 2, 200))
print(tinh_tong(1, 2, 101))
    


