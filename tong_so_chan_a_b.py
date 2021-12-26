# %%
a = int(input('Nhap a:'))
b = int(input('Nhap b:'))
so_cac_so_chan = 0
tong = 0
so = a
while so <= b:
    if so % 2 == 0:
        so_cac_so_chan = so_cac_so_chan + 1
        tong = tong + so
        pass
    so = so + 1
    pass

print('SO cac so chan:', so_cac_so_chan)
print('Tong: ', tong)

# 3 -> 12
# 4 6 8 10 12


