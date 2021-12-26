# %%
import numpy as np

# %%
mat_tran = np.array([[3,4,2],[6,8,4],[9, 12, 2]])
print(mat_tran)

# %%
def ma_tran_con(mt, i, j):
    mtc = mt.copy()
    mtc = np.delete(mtc, i, 0);
    mtc = np.delete(mtc, j, 1); 
    return mtc 

# %%
def dinh_thuc(mt):
    so_chieu = mt.shape[1]
    if so_chieu <= 1:
        return mt[0][0]
    
    ket_qua = 0
    j = 0
    while j < so_chieu:
        pds = ma_tran_con(mt, 0, j)
        ket_qua += ((-1) ** j) * mt[0][j] * dinh_thuc(pds)
        j = j + 1
        pass
    return ket_qua    



# %%
def nghich_dao(mt):

    d_mt = dinh_thuc(mt)
    if d_mt == 0:        
        return None        

    so_hang = mt.shape[0]
    so_cot =  mt.shape[1]

    c = np.zeros(shape=( so_hang, so_cot))
    i = 0
    while i < so_hang:
        
        j = 0
        while j < so_cot:
            pds = ma_tran_con(mt, i, j)
            c[i][j] = ((-1) ** (i + j)) * dinh_thuc(pds)
            j = j + 1
            pass
        i = i + 1
        pass

    k = -1 / d_mt
    c_t = c.transpose()
    ket_qua = np.multiply(c_t, k)
    return ket_qua

# %%
ma_tran = np.array([[1,2,3], [2,5,3], [1,0, 8]])

print(nghich_dao(ma_tran))

# %%
mat_tran = np.array([[3,4,2],[6,8,4],[9, 12, 2]])
print(mat_tran)
print(nghich_dao(mat_tran))


