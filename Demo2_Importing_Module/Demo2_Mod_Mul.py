from Demo2_Mod_Add import add

def mul(x, y):
    res = 0
    for i in range(x):
        res = add(res, y)
    
    return res


# 34:35