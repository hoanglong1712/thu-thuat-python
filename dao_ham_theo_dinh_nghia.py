# %%
import sympy

# %%
def dao_ham_c(c):
    x = sympy.symbols('x')
    expr =(c - c) / x
    return sympy.limit(expr, x, 0)

print(dao_ham_c(4))

# %%
def dao_ham_x(x):
    dx = sympy.symbols('dx')
    expr = (x + dx - x) / dx
    return sympy.limit(expr, dx, 0)

print(dao_ham_x(5))


# %%

def dao_ham_sin(x):
    dx = sympy.symbols('dx')
    expr = (sympy.sin(x + dx) - sympy.sin(x)) / dx
    return sympy.limit(expr, dx, 0)

print(dao_ham_sin(1))

# %%
def dao_ham_e(x):
    dx = sympy.symbols('dx')
    expr = (sympy.exp(x + dx) - sympy.exp(x)) / dx
    return sympy.limit(expr, dx, 0)

print(dao_ham_e(2))

# %%
print(dao_ham_c(6))
print(dao_ham_x(6))
print(dao_ham_sin(6))
print(dao_ham_e(6))


# %%



