# %%
M = int(input('Nhap M:'))
N = int(input('Nhap N:'))

tong = 0
so = M
while so <= N:
    if so % 3 == 0 and so % 5 == 0:
        tong = tong + so
        pass 
    so = so + 1
    pass

print(tong)


