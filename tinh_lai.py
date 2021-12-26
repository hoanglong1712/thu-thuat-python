# %%
A = int(input('Nhap A:'))
B = int(input('Nhap B:'))

so_nam = 0
so_lai = A * 0.06
while A < B:
    A = A + so_lai
    so_nam = so_nam + 1
    pass

print(so_nam)


