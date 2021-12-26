# %%
n = int(input('Nhap n'))

# tinh tong s = 1 + 2 + .. + n
# cap so cong
# s = n(n + 1)/ 2

print(int( n * (n + 1) / 2))

so = 1
tong = 0

while so <= n:
    tong += so   
    so += 1
    pass
#####

so_le = 0
so = 1
while so < n:    
    if so % 2 != 0:
        so_le += 1
    so += 1
    pass

# dem so tu nhien nho nho hon n va le

# neu n chan thi ta co n / 2 so le thoa man yeu cau
# neu n le thi ta co (n-1) / 2 so le thoa man yeu cau


if n % 2 == 0:
    print(int(n/2))
else:
    print(int((n-1)/2))

print(tong)
print(so_le)
    




