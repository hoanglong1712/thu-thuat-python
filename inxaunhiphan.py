# %%
# cho xau nhi phan trong do khong co 3 so 0 lien tiep
# tim cac xau co do dai n = 6


def xau_de_qui(n, do_dai_so_0, ket_qua):
    if n <= 0:
        ba_khong = '0' * do_dai_so_0
        if len(ket_qua) > 0 and ba_khong not in ket_qua:
            print(ket_qua)
        pass    
    else:
        xau_de_qui(n - 1, do_dai_so_0, ket_qua + '0')
        xau_de_qui(n - 1, do_dai_so_0, ket_qua + '1')
        pass
    pass

def xau(n, do_dai_so_0):
    ket_qua = ""
    xau_de_qui(n, do_dai_so_0, ket_qua)
    pass
xau(4, 3)


