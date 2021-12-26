# %%
import numpy as np

# %%
mat_tran = np.array([[1,2,1,1], [2,3,2,6],[-3, -1,0, 5], [1,1,1,5]])

# %%
print(np.linalg.det(mat_tran))
print(np.linalg.inv(mat_tran))

# %%
def phu_dai_so(mt, i, j):
    psd = mt.copy()
    psd = np.delete(psd, i, 0);
    psd = np.delete(psd, j, 1); 
    return psd
    pass

#mat_tran = np.array([[1, 2, 3], [-4, 5,6], [7, -8,9]])
#mat_tran = np.array([[3,4,2], [6,8, 4], [9, 12, 10]])
#mat_tran = np.array([ [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]])
#mat_tran = np.array([ [3,1,1,1], [1,3,1,1], [1,1,3,1], [1,1,1,3]])

#mat_tran = np.array([ [1,1,1,1], [1,2,3,4], [1,4,9,16], [1,8,27,64]])
#mat_tran = np.array([ [1,1,1,1], [1,2,3,4], [1,3,6,10], [1,4,10,20]])

#mat_tran = np.array([[3,4,2], [6,8, 4], [9, 12, 2]])

#mat_tran = np.array([[1,2,1,1], [2,3,2,6],[-3, -1,0, 5], [1,1,1,5]])
#mat_tran = np.array([[246, 427,327], [1014, 543, 443],[-342, 721, 621]])

mat_tran = np.array([[1,2,3], [2,5,3],[1, 0 ,8]])
def tinh_dinh_thuc(mt):
    so_chieu = mt.shape[1]

    if so_chieu <= 1:
        return mt[0][0]
    
    ket_qua = 0
    j = 0
    while j < so_chieu:
        psd = phu_dai_so(mt, 0, j)
        ket_qua += ((-1)** j) * mt[0][j] * tinh_dinh_thuc(psd)
        j = j + 1
        pass
    return ket_qua
    pass

print(tinh_dinh_thuc(mat_tran))
print(mat_tran)

# %%
def nghich_dao(mt):
    a = np.zeros(shape=(mt.shape[0],mt.shape[1]))
    i = 0
    while i < mt.shape[0]:
       
        j = 0
        while j < mt.shape[1]:
            psd = phu_dai_so(mt, i, j)
            a[i][j] = ((-1) ** (j + i)) * tinh_dinh_thuc(psd)
            j = j + 1
            pass
         
        i = i + 1
        pass
    return a
    pass

nghich_dao(mat_tran).transpose()


